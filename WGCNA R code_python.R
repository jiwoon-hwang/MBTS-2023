#Adopted from Pei G., Chen L., Zhang W.. WGCNA Application to Proteomic and Metabolomic Data Analysis. Methods Enzymol. 2017, 585:135-158. https://pubmed.ncbi.nlm.nih.gov/28109426/

#=====================================================================================
#
#  Code chunk 1	Load Metabolome data for missing imputation
#
#=====================================================================================

# Display the current working directory
getwd();
workingDir = "/Users/jiwoonhwang/Desktop/MBTS/WGCNA/norm to PE_sf_oxi_TAG/";
setwd(workingDir); 

library(gdata) 

MetData <- read.csv(paste(workingDir,"div_log.csv", sep=""), row.names=1) 

# load metabolomic data set
dim(MetData);names(MetData)

# determine whether data set are complete
complete.cases(MetData)			
md.pattern(MetData)	

#replace the missing value by a minimum value of the metabolite quantified
Pre.MetData=MetData
Pre.MetData[is.na(Pre.MetData)]=0
# Pre.MetData
Min.replace=apply(Pre.MetData,1,min)
Replace.matrix=matrix(rep(matrix(Min.replace),ncol(MetData)),nrow(MetData))
index=is.na(MetData)
MetData[index]=Replace.matrix[index]
MetData[index]

# save the data set after miss value imputation
write.csv(MetData,file=paste(Sys.Date(),"_foldchange_imputed_data.csv", sep=""))

#=====================================================================================
#
#  Code chunk 2	Load WGCNA package 
#
#=====================================================================================

# Load the WGCNA package
library(WGCNA);
# The following setting is important, do not omit.
options(stringsAsFactors = FALSE);
# Read in the metabolic data set			
MetData = as.data.frame(t(MetData))
# Take a quick look at what is in the data set:
dim(MetData);names(MetData);


##Plot sample tree to find outliers 
sampleTree = hclust(dist(MetData), method = "average");
# Plot the sample tree: Open a graphic output window of size 12 by 9 inches
# The user should change the dimensions if the window is too large or too small.
sizeGrWindow(12,9)
pdf(file=paste(Sys.Date(),"_sampleClustering.pdf", sep=""),  width = 12, height = 9);
par(cex = 0.6);
par(mar = c(0,4,2,0))
plot(sampleTree, main = "Sample clustering to detect outliers", sub="", xlab="", cex.lab = 1.5,
     cex.axis = 1.5, cex.main = 2)
dev.off()

#=====================================================================================
#
#  Code chunk 3	Load traits data
#
#=====================================================================================

datTraits<- read.csv("/Users/jiwoonhwang/Desktop/MBTS/WGCNA/metadata_metabolic_proxy_traits_chemtax.csv", row.names=1)
#rownames(datTraits)=datTraits[,1];datTraits=datTraits[,-1]
dim(datTraits);names(datTraits)

#=====================================================================================
#
#  Code chunk 4 SoftThreshold chosen
#
#=====================================================================================

# Choose a set of soft-thresholding powers
powers = c(c(1:10), seq(from = 12, to=40, by=4))
# Call the network topology analysis function
sft = pickSoftThreshold(MetData, powerVector = powers, verbose = 5)
# Plot the results:
pdf(paste(Sys.Date(),"_Example-2 Metabolome Figure 1.pdf", sep=""),10,5)
# sizeGrWindow(9, 5)
par(mfrow = c(1,2));
cex1 = 0.9;
# Scale-free topology fit index as a function of the soft-thresholding power
plot(sft$fitIndices[,1], -sign(sft$fitIndices[,3])*sft$fitIndices[,2],
     xlab="Soft Threshold (power)",ylab="Scale Free Topology Model Fit R^2",type="n",
     main = paste("Scale independence"));
text(sft$fitIndices[,1], -sign(sft$fitIndices[,3])*sft$fitIndices[,2],
     labels=powers,cex=cex1,col="red");
# this line corresponds to using an R^2 cut-off of h
abline(h=0.80,col="red")
# Mean connectivity as a function of the soft-thresholding power
plot(sft$fitIndices[,1], sft$fitIndices[,5],
     xlab="Soft Threshold (power)",ylab="Mean Connectivity", type="n",
     main = paste("Mean connectivity"))
text(sft$fitIndices[,1], sft$fitIndices[,5], labels=powers, cex=cex1,col="red")
dev.off()

write.csv(sft$fitIndices,file=paste(Sys.Date(),"_pickSoftThreshold.csv", sep=""))

#=====================================================================================
#
#  Code chunk 5	WGCNA construction
#
#=====================================================================================

softPower = 30;
net = blockwiseModules(MetData, power = softPower, networkType = "signed",
                       TOMType = "signed", minModuleSize = 10,
                       reassignThreshold = 0, mergeCutHeight = .12,
                       numericLabels = TRUE, pamRespectsDendro = FALSE,
                       saveTOMs = TRUE,
                       saveTOMFileBase = "Example-2 MetDataTOM", 
                       verbose = 3)
table(net$colors)

#=====================================================================================
#
#  Code chunk 6	Clustering dendrograms for metabolites
#
#=====================================================================================

# open a graphics window
pdf("Example-2 Metabolome Figure 2 - threshold=30, mch0.12, min10.pdf",150,30)
# sizeGrWindow(12, 9)
# Convert labels to colors for plotting
mergedColors = labels2colors(net$colors)
# Plot the dendrogram and the module colors underneath
plotDendroAndColors(net$dendrograms[[1]], mergedColors[net$blockGenes[[1]]],
                    "Module colors",
                    dendroLabels = names(MetData), hang = 0.03,
                    addGuide = TRUE, guideHang = 0.05)
dev.off()				


#=====================================================================================
#
#  Code chunk 7 Modules analysis
#
#=====================================================================================

moduleLabels = net$colors
moduleColors = labels2colors(net$colors)
MEs = net$MEs;
geneTree = net$dendrograms[[1]];


geneInfo0 = data.frame(Metabolites = names(MetData),
                       moduleColor = moduleColors)
geneOrder = order(geneInfo0$moduleColor);
geneInfo = geneInfo0[geneOrder, ]
write.csv(geneInfo, file = "WGCNA result-30, mch0.12.csv", row.names = FALSE)
# save(MEs, moduleLabels, moduleColors, geneTree, file = "MetData-networkConstruction-auto.RData")

table = moduleEigengenes(MetData, moduleColors)$varExplained
colnames(table) = colnames(moduleEigengenes(MetData, moduleColors)$eigengenes)
write.csv(table, file = "WGCNA var explained.csv", row.names = FALSE)

write.csv(moduleEigengenes(MetData, moduleColors)$eigengenes, file = "eigengenes.csv")
write.csv(moduleEigengenes(MetData, moduleColors)$averageExpr, file = "average_expression.csv")


#=====================================================================================
#
#  Code chunk 9	Module-trait relationships
#
#=====================================================================================

# open a graphics window
pdf("Example-2 Metabolome Figure 3.pdf",10,6)
#sizeGrWindow(10,6)
# Will display correlations and their p-values
textMatrix =  paste(signif(moduleTraitCor, 2), "\n(",
                           signif(moduleTraitPvalue, 1), ")", sep = "");
dim(textMatrix) = dim(moduleTraitCor)
par(mar = c(6, 8.5, 3, 3));
# Display the correlation values within a heatmap plot
labeledHeatmap(Matrix = moduleTraitCor,
               xLabels = names(datTraits),
               yLabels = names(MEs),
               ySymbols = names(MEs),
               colorLabels = FALSE,
               colors = blueWhiteRed(50),
               textMatrix = textMatrix,
               setStdMargins = FALSE,
               cex.text = 0.5,
               zlim = c(-1,1),
               main = paste("Module-trait relationships"))
dev.off()		   
			   
write.csv(moduleTraitCor, file = "Module-trait correlation.csv")
write.csv(moduleTraitPvalue, file = "Module-trait Pvalue.csv")



# Create the starting data frame
geneInfo0 = data.frame(Metabolites = names(MetData),
                      moduleColor = moduleColors
              )
# Order modules by their significance for Astaxanthin
modOrder = order(-abs(cor(MEs, Astaxanthin, use = "p")));
# Add module membership information in the chosen order
  oldNames = names(geneInfo0)
geneInfo0 = data.frame(geneInfo0, geneModuleMembership, 
                         MMPvalue);
  #names(geneInfo0) = c(oldNames, paste("MM.", modNames[modOrder[mod]], sep=""),
                       #paste("p.MM.", modNames[modOrder[mod]], sep=""))

# Order the genes in the geneInfo variable first by module color, then by geneTraitSignificance
#geneOrder = order(geneInfo0$moduleColor, -abs(geneInfo0$GS.Astaxanthin));
#geneInfo = geneInfo0[geneOrder, ]
#save WGCNA results
write.csv(geneInfo, file = "Example-2 Metabolome Table 2 WGCNA result.csv", row.names = FALSE)

