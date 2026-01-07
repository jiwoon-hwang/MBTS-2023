<h1>MBTS-2023</h1>

<p>
This repository contains data, code, and supplemental materials associated with the paper:
</p>

<p>
<strong>Hwang, J., Hayward, A., Sofen, L. E., Pitz, K. J., Chavez, F. P., &amp; Edwards, B. R. (2025)</strong><br>
<em>Daily microbial rhythms of the surface ocean interrupted by the new moon — a lipidomic study</em><br>
ISME Communications<br>
DOI: <a href="https://doi.org/10.1093/ismeco/ycaf044">10.1093/ismeco/ycaf044</a>
</p>

<hr>

<h2>Overview</h2>

<p>
This repository supports analyses of a high–temporal-resolution lipidomic time series collected in the Monterey Bay coastal system. The code reproduces figures and analyses related to:
</p>

<ul>
  <li>Diel and tidal variability in the surface ocean lipidome</li>
  <li>Chemotaxonomic interpretation of lipid and pigment data</li>
  <li>Network-based clustering of lipid species using WGCNA</li>
  <li>Estimation of carbon flux from triacylglycerol (TAG) dynamics</li>
</ul>

<p>
The repository is intended for transparency and reproducibility of the published results.
</p>

<hr>

<h2>Repository Contents</h2>

<ul>
  <li>
    <strong>MBTS_dataset.csv</strong><br>
    Processed lipid and pigment concentration data used in the analyses.
  </li>
  <li>
    <strong>Lineplots_Pieplots_WGCNA.ipynb</strong><br>
    Jupyter notebook for visualization of lipid module trends, and WGCNA results.
  </li>
  <li>
    <strong>Normalization_Quantification.ipynb</strong><br>
    Data normalization, quality control, and absolute quantification workflows.
  </li>
  <li>
    <strong>WGCNA R code_python.R</strong><br>
    R script implementing Weighted Gene Correlation Network Analysis (WGCNA) adapted for metabolomics data.
  </li>
  <li>
    <strong>WGCNA clustering results.pdf</strong><br>
    Clustering dendrograms and module assignments used in the paper and supplemental figures.
  </li>
</ul>

<hr>

<h2>Software and Dependencies</h2>

<p>
Analyses were performed using a combination of Python and R.
</p>

<p><strong>Python (Jupyter notebooks):</strong></p>
<ul>
  <li>pandas</li>
  <li>numpy</li>
  <li>matplotlib / seaborn</li>
  <li>scipy</li>
</ul>

<p><strong>R:</strong></p>
<ul>
  <li>WGCNA</li>
  <li>tidyverse</li>
  <li>Additional dependencies noted in the R script header</li>
</ul>

<hr>

<h2>How to Use</h2>

<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/jiwoon-hwang/MBTS-2023.git</code></pre>
  </li>
  <li>Open the Jupyter notebooks to reproduce figures and exploratory analyses.</li>
  <li>Run the R script to reproduce WGCNA clustering and module assignments.</li>
</ol>

<p>
The notebooks and scripts are organized to mirror the analysis flow described in the Methods and Results sections of the paper.
</p>

<hr>

<h2>Data Availability</h2>

<p>
Raw mass spectrometry data are available via the <strong>MassIVE repository</strong>:<br>
<strong>MSV000096826</strong> (doi:10.25345/C54F1MW73)
</p>

<p>
This GitHub repository contains processed data and analysis scripts only.
</p>

<hr>

<h2>Citation</h2>

<p>
If you use data or code from this repository, please cite the paper listed above.
</p>

<hr>

<h2>Contact</h2>

<p>
For questions related to the data or analysis, please contact the corresponding author listed in the publication.
</p>
