from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

root=Path('/mnt/data/sitev5')

index = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Kevin (Cheng-Chieh) Zheng | Statistics Portfolio</title>
  <meta name="description" content="Academic portfolio of Kevin (Cheng-Chieh) Zheng, an NDHU statistics student preparing for graduate study in statistics." />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header class="site-header"><div class="container nav"><div class="brand"><a href="index.html">Kevin Zheng</a></div><nav><a href="index.html">Home</a><a href="cv.html">CV</a><a href="index.html#projects">Projects</a><a href="index.html#contact">Contact</a><a href="https://github.com/kevinzheng0509/Kevinzheng" target="_blank">GitHub</a></nav></div></header>
  <main>
    <section class="hero">
      <div class="container hero-grid">
        <div>
          <p class="eyebrow">Statistics Portfolio</p>
          <h1>Kevin (Cheng-Chieh) Zheng</h1>
          <p class="lead">Statistics student at National Dong Hwa University and aspiring graduate student in statistics. My work focuses on statistical modeling, time series analysis, mathematical statistics, experimental design, and clear research communication.</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="#projects">View Projects</a>
            <a class="btn btn-secondary" href="cv.html">View CV</a>
            <a class="btn btn-secondary" href="kevin-zheng-cv.pdf" target="_blank">Download CV (PDF)</a>
          </div>
        </div>
        <div class="hero-card">
          <h3>Academic Focus</h3>
          <ul>
            <li>Regression analysis and inference</li>
            <li>Likelihood-based statistical theory</li>
            <li>ARIMA and volatility modeling</li>
            <li>Design of experiments and ANOVA</li>
            <li>R, Python, LaTeX, and reproducible reporting</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section alt highlight-section">
      <div class="container">
        <p class="section-label">Highlight Project</p>
        <div class="highlight-card">
          <div>
            <span class="tag">Featured Work</span>
            <h2>MediaTek Stock Time Series Analysis</h2>
            <p class="lead compact">A final project applying log-return transformation, stationarity testing, ARIMA model selection, residual diagnostics, and forecast evaluation to a real financial series.</p>
            <div class="bullet-row">
              <span>ARIMA modeling</span>
              <span>ADF testing</span>
              <span>Forecast evaluation</span>
              <span>Financial time series</span>
            </div>
          </div>
          <div class="stack-actions">
            <a class="btn btn-primary" href="project-timeseries.html">View Details</a>
            <a class="btn btn-secondary" href="mediatek-time-series-report.pdf" target="_blank">Open Report</a>
          </div>
        </div>
      </div>
    </section>

    <section id="about" class="section">
      <div class="container two-col">
        <div>
          <p class="section-label">About Me</p>
          <h2>Building a graduate-school-ready statistics portfolio</h2>
          <p>I am a senior statistics student at National Dong Hwa University with strong interests in statistical modeling, time series analysis, and applied data analysis.</p>
          <p>My academic work aims to connect statistical theory with real-world data problems, including regression modeling, experimental design, likelihood-based inference, and financial time series analysis.</p>
          <p>I am preparing for graduate study in statistics and use this site as a professional portfolio to present selected coursework, reports, and technical communication.</p>
        </div>
        <div class="callout">
          <h3>Current Direction</h3>
          <p class="muted">Preparing for graduate study in a statistics-related field with an emphasis on analytical rigor, reproducible workflows, and interpretable modeling.</p>
          <div class="stack-actions">
            <a class="mini-btn" href="cv.html">Academic CV</a>
            <a class="mini-btn" href="kevin-zheng-cv.pdf" target="_blank">Download CV</a>
            <a class="mini-btn" href="https://github.com/kevinzheng0509/Kevinzheng" target="_blank">GitHub Profile</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <p class="section-label">Snapshot</p>
        <h2>What this portfolio highlights</h2>
        <div class="stats-grid">
          <div class="stat-box"><strong>6+</strong><span class="muted">core statistical areas represented in coursework and presentations</span></div>
          <div class="stat-box"><strong>3</strong><span class="muted">project detail pages structured around motivation, methods, findings, and reflection</span></div>
          <div class="stat-box"><strong>R / Python</strong><span class="muted">programming tools used for analysis, modeling, and reproducible reporting</span></div>
        </div>
      </div>
    </section>

    <section id="projects" class="section">
      <div class="container">
        <p class="section-label">Selected Work</p>
        <h2>Projects and coursework highlights</h2>
        <div class="cards">
          <article class="card featured-outline">
            <span class="tag">Regression Analysis</span>
            <h3>ACT and GPA Prediction</h3>
            <p class="meta">Coursework project</p>
            <p>Analyzed the relationship between ACT scores and GPA using simple linear regression, confidence intervals, prediction intervals, and coefficient interpretation.</p>
            <div class="stack-actions"><a class="mini-btn" href="project-regression.html">View Details</a><a class="mini-btn" href="https://github.com/kevinzheng0509/Kevinzheng" target="_blank">GitHub Code</a></div>
          </article>

          <article class="card">
            <span class="tag">Mathematical Statistics</span>
            <h3>Likelihood Ratio Test Derivations</h3>
            <p class="meta">Theory-based assignment</p>
            <p>Derived likelihood ratio tests under different distributional assumptions, emphasizing proof structure, model assumptions, and asymptotic reasoning.</p>
          </article>

          <article class="card featured-outline">
            <span class="tag">Time Series</span>
            <h3>MediaTek Stock Time Series Analysis</h3>
            <p class="meta">Final report · forecasting and diagnostics</p>
            <p>Applied log-return transformation, ADF testing, ARIMA model selection, residual diagnostics, and forecast evaluation to MediaTek stock data.</p>
            <div class="stack-actions"><a class="mini-btn" href="project-timeseries.html">View Details</a><a class="mini-btn" href="mediatek-time-series-report.pdf" target="_blank">Report PDF</a><a class="mini-btn" href="https://github.com/kevinzheng0509/Kevinzheng" target="_blank">GitHub Code</a></div>
          </article>

          <article class="card featured-outline">
            <span class="tag">Experimental Design</span>
            <h3>Latin Square and BIBD Presentation</h3>
            <p class="meta">Final presentation · design of experiments</p>
            <p>Presented Latin square, Graeco-Latin square, replication structures, and balanced incomplete block design with ANOVA-based interpretation.</p>
            <div class="stack-actions"><a class="mini-btn" href="project-experimental.html">View Details</a><a class="mini-btn" href="latin-square-bibd-presentation.pdf" target="_blank">Slides PDF</a><a class="mini-btn" href="https://github.com/kevinzheng0509/Kevinzheng" target="_blank">GitHub Code</a></div>
          </article>

          <article class="card">
            <span class="tag">Weighted Least Squares</span>
            <h3>Heteroscedasticity and WLS</h3>
            <p class="meta">Applied statistics problem set</p>
            <p>Compared OLS and WLS under heteroscedastic error structures and interpreted weighted estimates in a student time-cost dataset.</p>
          </article>

          <article class="card">
            <span class="tag">Statistical Computing</span>
            <h3>R-Based Analytical Workflows</h3>
            <p class="meta">Programming and reproducibility</p>
            <p>Built R workflows for simulation, inference, data visualization, and report preparation with an emphasis on transparent and reproducible analysis.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <p class="section-label">Skills</p>
        <h2>Methods and tools</h2>
        <div class="skill-grid">
          <div class="skill-box">
            <h3>Statistical Topics</h3>
            <p>Regression, hypothesis testing, likelihood methods, time series, experimental design, ANOVA, weighted least squares, and statistical inference.</p>
          </div>
          <div class="skill-box">
            <h3>Programming</h3>
            <p>R, Python, reproducible analysis workflows, report generation, and project organization for academic portfolios.</p>
          </div>
          <div class="skill-box">
            <h3>Technical Writing</h3>
            <p>LaTeX, Beamer slides, academic report writing, and English presentation preparation for coursework and graduate applications.</p>
          </div>
        </div>
      </div>
    </section>

    <section id="contact" class="section">
      <div class="container narrow">
        <p class="section-label">Contact</p>
        <h2>Professional links</h2>
        <div class="contact-box">
          <p><strong>Email:</strong> <a href="mailto:kevinzheng0509@gmail.com">kevinzheng0509@gmail.com</a></p>
          <p><strong>GitHub:</strong> <a href="https://github.com/kevinzheng0509/Kevinzheng" target="_blank">github.com/kevinzheng0509/Kevinzheng</a></p>
          <p><strong>CV:</strong> <a href="cv.html">Open CV page</a> · <a href="kevin-zheng-cv.pdf" target="_blank">Download PDF</a></p>
        </div>
      </div>
    </section>
  </main>
  <footer class="site-footer"><div class="container footer-row"><span>© 2026 Kevin (Cheng-Chieh) Zheng</span><span>Statistics Portfolio</span></div></footer>
</body>
</html>'''

cv='''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>CV | Kevin Zheng</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header class="site-header"><div class="container nav"><div class="brand"><a href="index.html">Kevin Zheng</a></div><nav><a href="index.html">Home</a><a href="cv.html">CV</a><a href="index.html#projects">Projects</a><a href="index.html#contact">Contact</a><a href="https://github.com/kevinzheng0509/Kevinzheng" target="_blank">GitHub</a></nav></div></header>
  <main>
    <section class="page-hero">
      <div class="container narrow">
        <p class="breadcrumb"><a class="inline-link" href="index.html">Home</a> / CV</p>
        <p class="eyebrow">Curriculum Vitae</p>
        <h1>Kevin (Cheng-Chieh) Zheng</h1>
        <p class="lead">Statistics student at National Dong Hwa University preparing for graduate study in statistics and related quantitative fields.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="kevin-zheng-cv.pdf" target="_blank">Download CV (PDF)</a>
          <a class="btn btn-secondary" href="mailto:kevinzheng0509@gmail.com">Email</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container cv-grid">
        <div class="cv-block">
          <h3>Contact</h3>
          <ul>
            <li>Email: <a class="inline-link" href="mailto:kevinzheng0509@gmail.com">kevinzheng0509@gmail.com</a></li>
            <li>GitHub: <a class="inline-link" href="https://github.com/kevinzheng0509/Kevinzheng" target="_blank">github.com/kevinzheng0509/Kevinzheng</a></li>
          </ul>
        </div>
        <div class="cv-block">
          <h3>Education</h3>
          <ul>
            <li>National Dong Hwa University</li>
            <li>B.S. in Statistics</li>
            <li>Expected graduation: 2026</li>
          </ul>
        </div>
        <div class="cv-block">
          <h3>Research Interests</h3>
          <ul>
            <li>Statistical modeling</li>
            <li>Regression analysis</li>
            <li>Time series analysis</li>
            <li>Experimental design</li>
            <li>Applied data analysis</li>
          </ul>
        </div>
        <div class="cv-block">
          <h3>Technical Skills</h3>
          <ul>
            <li>Programming: R, Python</li>
            <li>Tools: LaTeX, Git, GitHub</li>
            <li>Methods: LRT, ANOVA, WLS, ARIMA, GARCH, regression inference</li>
          </ul>
        </div>
        <div class="cv-block">
          <h3>Selected Projects</h3>
          <ul>
            <li>ACT and GPA Regression Analysis</li>
            <li>Likelihood Ratio Test Derivations</li>
            <li>MediaTek Time Series Analysis</li>
            <li>Latin Square and BIBD Experimental Design Presentation</li>
          </ul>
        </div>
        <div class="cv-block">
          <h3>Leadership & Activities</h3>
          <ul>
            <li>Class representative for three years</li>
            <li>Science competition event organizer</li>
            <li>Volleyball team captain</li>
          </ul>
        </div>
      </div>
    </section>
  </main>
  <footer class="site-footer"><div class="container footer-row"><span>© 2026 Kevin (Cheng-Chieh) Zheng</span><span>Statistics Portfolio</span></div></footer>
</body>
</html>'''

pts='''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Time Series Project | Kevin Zheng</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header class="site-header"><div class="container nav"><div class="brand"><a href="index.html">Kevin Zheng</a></div><nav><a href="index.html">Home</a><a href="cv.html">CV</a><a href="index.html#projects">Projects</a><a href="index.html#contact">Contact</a><a href="https://github.com/kevinzheng0509/Kevinzheng" target="_blank">GitHub</a></nav></div></header>
  <main>
    <section class="page-hero">
      <div class="container narrow">
        <p class="breadcrumb"><a class="inline-link" href="index.html">Home</a> / Project</p>
        <p class="eyebrow">Time Series Analysis</p>
        <h1>MediaTek Stock Time Series Analysis</h1>
        <p class="lead">A financial time series project that applies standard diagnostic and forecasting tools to MediaTek stock data, with emphasis on stationarity, model adequacy, and interpretability.</p>
      </div>
    </section>

    <section class="section">
      <div class="container project-layout">
        <div>
          <div class="project-panel project-section">
            <h2>Problem Motivation</h2>
            <p>This project examines how time series methods can be used to model and evaluate the dynamics of a real stock series. The goal is not only to fit a model, but also to understand whether the transformed series is suitable for inference and short-horizon forecasting.</p>
          </div>
          <div class="project-panel project-section">
            <h2>Methodology</h2>
            <ul class="list-tight">
              <li>Log-return transformation to stabilize the series</li>
              <li>ADF testing for stationarity assessment</li>
              <li>ARIMA(p,d,q) model selection</li>
              <li>Residual diagnostics for adequacy checking</li>
              <li>Forecast evaluation over a 60-day horizon</li>
            </ul>
          </div>
          <div class="project-panel project-section">
            <h2>Key Findings</h2>
            <p>The project demonstrates a full workflow from transformation through model validation. The ARIMA stage focuses on the mean structure, while diagnostics are used to judge whether model assumptions remain plausible before forecasting is interpreted.</p>
          </div>
          <div class="project-panel project-section formula-box">
            <h2>Modeling Lens</h2>
            <p class="formula">ARIMA(p,d,q)</p>
            <p class="muted">Used as the main framework for mean-process modeling after transformation and stationarity checks.</p>
          </div>
          <div class="project-panel project-section">
            <h2>Reflection</h2>
            <p>One limitation of a univariate ARIMA-based analysis is that it ignores external market information and structural events. A natural next step would be to extend the study with volatility modeling or exogenous predictors to better represent financial uncertainty.</p>
          </div>
        </div>
        <aside>
          <div class="summary-list">
            <h3>Project Summary</h3>
            <ul>
              <li><strong>Topic:</strong> Financial time series</li>
              <li><strong>Methods:</strong> Log return, ADF, ARIMA, diagnostics</li>
              <li><strong>Format:</strong> Final report PDF</li>
            </ul>
            <div class="stack-actions">
              <a class="btn btn-primary" href="mediatek-time-series-report.pdf" target="_blank">Download Report</a>
              <a class="btn btn-secondary" href="https://github.com/kevinzheng0509/Kevinzheng" target="_blank">GitHub Profile</a>
            </div>
          </div>
        </aside>
      </div>
    </section>
  </main>
  <footer class="site-footer"><div class="container footer-row"><span>© 2026 Kevin (Cheng-Chieh) Zheng</span><span>Statistics Portfolio</span></div></footer>
</body>
</html>'''

pexp='''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Experimental Design Project | Kevin Zheng</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header class="site-header"><div class="container nav"><div class="brand"><a href="index.html">Kevin Zheng</a></div><nav><a href="index.html">Home</a><a href="cv.html">CV</a><a href="index.html#projects">Projects</a><a href="index.html#contact">Contact</a><a href="https://github.com/kevinzheng0509/Kevinzheng" target="_blank">GitHub</a></nav></div></header>
  <main>
    <section class="page-hero">
      <div class="container narrow">
        <p class="breadcrumb"><a class="inline-link" href="index.html">Home</a> / Project</p>
        <p class="eyebrow">Experimental Design</p>
        <h1>Latin Square and BIBD Presentation</h1>
        <p class="lead">A final presentation on classical design structures that control nuisance variation and support interpretable treatment comparison through balance and blocking.</p>
      </div>
    </section>

    <section class="section">
      <div class="container project-layout">
        <div>
          <div class="project-panel project-section">
            <h2>Problem Motivation</h2>
            <p>Experimental design asks how treatments should be assigned when nuisance sources of variability cannot be ignored. This project focuses on design structures that reduce bias and improve interpretability before data analysis even begins.</p>
          </div>
          <div class="project-panel project-section">
            <h2>Methodology</h2>
            <ul class="list-tight">
              <li>Latin square design structure</li>
              <li>Graeco-Latin square extension</li>
              <li>Replication concepts</li>
              <li>Balanced incomplete block design</li>
              <li>ANOVA-based interpretation of treatment effects</li>
            </ul>
          </div>
          <div class="project-panel project-section">
            <h2>Key Findings</h2>
            <p>The presentation shows how careful layout and blocking can separate treatment effects from nuisance variation. It also emphasizes that good design decisions directly affect the validity and efficiency of subsequent inference.</p>
          </div>
          <div class="project-panel project-section formula-box">
            <h2>Modeling Lens</h2>
            <p class="formula">ANOVA</p>
            <p class="muted">Used as the inferential framework for assessing treatment differences under structured blocking designs.</p>
          </div>
          <div class="project-panel project-section">
            <h2>Reflection</h2>
            <p>This project strengthened my understanding that statistical quality begins at the design stage. A useful next step would be to connect these classical designs with real experimental case studies or simulation-based comparisons of design efficiency.</p>
          </div>
        </div>
        <aside>
          <div class="summary-list">
            <h3>Project Summary</h3>
            <ul>
              <li><strong>Topic:</strong> Design of experiments</li>
              <li><strong>Methods:</strong> Blocking, Latin square, BIBD, ANOVA</li>
              <li><strong>Format:</strong> Final presentation PDF</li>
            </ul>
            <div class="stack-actions">
              <a class="btn btn-primary" href="latin-square-bibd-presentation.pdf" target="_blank">Download Slides</a>
              <a class="btn btn-secondary" href="https://github.com/kevinzheng0509/Kevinzheng" target="_blank">GitHub Profile</a>
            </div>
          </div>
        </aside>
      </div>
    </section>
  </main>
  <footer class="site-footer"><div class="container footer-row"><span>© 2026 Kevin (Cheng-Chieh) Zheng</span><span>Statistics Portfolio</span></div></footer>
</body>
</html>'''

preg='''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Regression Project | Kevin Zheng</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header class="site-header"><div class="container nav"><div class="brand"><a href="index.html">Kevin Zheng</a></div><nav><a href="index.html">Home</a><a href="cv.html">CV</a><a href="index.html#projects">Projects</a><a href="index.html#contact">Contact</a><a href="https://github.com/kevinzheng0509/Kevinzheng" target="_blank">GitHub</a></nav></div></header>
  <main>
    <section class="page-hero">
      <div class="container narrow">
        <p class="breadcrumb"><a class="inline-link" href="index.html">Home</a> / Project</p>
        <p class="eyebrow">Regression Project</p>
        <h1>ACT and GPA Prediction</h1>
        <p class="lead">A regression-focused coursework project centered on model interpretation, interval estimation, and prediction in an educational dataset.</p>
      </div>
    </section>

    <section class="section">
      <div class="container project-layout">
        <div>
          <div class="project-panel project-section">
            <h2>Problem Motivation</h2>
            <p>This project studies whether ACT scores can help explain GPA variation. The emphasis is not only on fitting a line, but on understanding what the estimated relationship means in context.</p>
          </div>
          <div class="project-panel project-section">
            <h2>Methodology</h2>
            <ul class="list-tight">
              <li>Simple linear regression fitting</li>
              <li>Confidence intervals for the mean response</li>
              <li>Prediction intervals for an individual response</li>
              <li>Hypothesis testing for regression coefficients</li>
              <li>Interpretation of slope, uncertainty, and prediction quality</li>
            </ul>
          </div>
          <div class="project-panel project-section">
            <h2>Key Findings</h2>
            <p>The project highlights how regression output should be interpreted carefully rather than reported mechanically. It also shows the distinction between uncertainty about the expected response and uncertainty about a new observation.</p>
          </div>
          <div class="project-panel project-section formula-box">
            <h2>Modeling Lens</h2>
            <p class="formula">y = \beta_0 + \beta_1 x + \varepsilon</p>
            <p class="muted">A simple linear regression framework used to connect explanatory variation with response prediction and inference.</p>
          </div>
          <div class="project-panel project-section">
            <h2>Reflection</h2>
            <p>A simple model is useful for interpretation, but it may miss nonlinear effects or additional explanatory variables. Future work could compare multiple-predictor extensions and assess model assumptions through broader diagnostic analysis.</p>
          </div>
        </div>
        <aside>
          <div class="summary-list">
            <h3>Project Summary</h3>
            <ul>
              <li><strong>Topic:</strong> Regression analysis</li>
              <li><strong>Methods:</strong> Estimation, intervals, coefficient tests</li>
              <li><strong>Status:</strong> Detail page ready for future report upload</li>
            </ul>
            <div class="stack-actions">
              <a class="btn btn-secondary" href="https://github.com/kevinzheng0509/Kevinzheng" target="_blank">GitHub Profile</a>
            </div>
          </div>
        </aside>
      </div>
    </section>
  </main>
  <footer class="site-footer"><div class="container footer-row"><span>© 2026 Kevin (Cheng-Chieh) Zheng</span><span>Statistics Portfolio</span></div></footer>
</body>
</html>'''

style = root.joinpath('style.css').read_text()
style += '''
.highlight-section{padding-top:28px}
.highlight-card{display:grid;grid-template-columns:1.2fr auto;gap:24px;align-items:center;background:linear-gradient(135deg,#ffffff 0%,#f1f6fb 100%);border:1px solid var(--line);border-radius:24px;box-shadow:var(--shadow);padding:28px}
.compact{max-width:680px}
.bullet-row{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px}
.bullet-row span{padding:8px 12px;border-radius:999px;background:var(--primary-soft);color:var(--primary);font-weight:600;font-size:.9rem}
.featured-outline{border-color:#c8d8ea}
.card{transition:transform .18s ease, box-shadow .18s ease, border-color .18s ease}
.card:hover{transform:translateY(-4px);box-shadow:0 16px 34px rgba(17,24,39,.12);border-color:#bfd1e3}
.formula-box{background:linear-gradient(180deg,#ffffff 0%,#f7fbff 100%)}
.formula{font-size:1.45rem;font-weight:800;letter-spacing:-.02em;color:var(--primary);margin-bottom:8px}
@media (max-width:900px){.highlight-card{grid-template-columns:1fr}}
'''

(root/'index.html').write_text(index)
(root/'cv.html').write_text(cv)
(root/'project-timeseries.html').write_text(pts)
(root/'project-experimental.html').write_text(pexp)
(root/'project-regression.html').write_text(preg)
(root/'style.css').write_text(style)
(root/'README.md').write_text('''# Kevin Statistics Portfolio (Version 6)\n\nThis package is prepared for GitHub Pages deployment.\n\n## Added in Version 6\n- Highlight project section on the homepage\n- About Me section with graduate-school positioning\n- Stronger project detail pages with motivation, methodology, findings, and reflection\n- CV download button and included PDF CV\n- Updated naming format: Kevin (Cheng-Chieh) Zheng\n\n## Included pages\n- index.html\n- cv.html\n- project-timeseries.html\n- project-experimental.html\n- project-regression.html\n- style.css\n\n## Included files\n- mediatek-time-series-report.pdf\n- latin-square-bibd-presentation.pdf\n- kevin-zheng-cv.pdf\n\n## Deploy to GitHub Pages\n1. Create a repository named `kevinzheng0509.github.io`\n2. Upload all files in this folder to the repository root\n3. Open **Settings → Pages**\n4. Set the source to `Deploy from a branch`\n5. Choose the `main` branch and `/root`\n6. Save and wait for deployment\n\nYour site URL should become:\n`https://kevinzheng0509.github.io`\n''')

# Create PDF CV
pdf_path = root/'kevin-zheng-cv.pdf'
doc = SimpleDocTemplate(str(pdf_path), pagesize=A4, leftMargin=42, rightMargin=42, topMargin=42, bottomMargin=42)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Name', fontName='Helvetica-Bold', fontSize=19, leading=24, textColor=colors.HexColor('#183b66')))
styles.add(ParagraphStyle(name='Section', fontName='Helvetica-Bold', fontSize=11.5, leading=14, textColor=colors.HexColor('#183b66'), spaceBefore=8, spaceAfter=6))
styles.add(ParagraphStyle(name='Body2', fontName='Helvetica', fontSize=10.2, leading=14, textColor=colors.HexColor('#16202a')))
styles.add(ParagraphStyle(name='SmallMuted', fontName='Helvetica', fontSize=9.4, leading=12, textColor=colors.HexColor('#5d6b7a')))

story=[]
story += [Paragraph('Kevin (Cheng-Chieh) Zheng', styles['Name']), Paragraph('Email: kevinzheng0509@gmail.com | GitHub: github.com/kevinzheng0509/Kevinzheng', styles['SmallMuted']), Spacer(1,12)]

def add_section(title, rows):
    story.append(Paragraph(title, styles['Section']))
    data=[]
    for k,v in rows:
        data.append([Paragraph(f'<b>{k}</b>', styles['Body2']), Paragraph(v, styles['Body2'])])
    t=Table(data, colWidths=[115, 370])
    t.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LINEBELOW',(0,0),(-1,-1),0.35,colors.HexColor('#d9e2ec')),
        ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),6)
    ]))
    story.append(t)
    story.append(Spacer(1,6))

add_section('Education', [('Institution','National Dong Hwa University'), ('Degree','B.S. in Statistics'), ('Expected Graduation','2026')])
add_section('Research Interests', [('Areas','Statistical modeling, regression analysis, time series analysis, experimental design, applied data analysis')])
add_section('Technical Skills', [('Programming','R, Python'), ('Tools','LaTeX, Git, GitHub'), ('Methods','Regression inference, likelihood ratio test, ANOVA, weighted least squares, ARIMA, GARCH')])
add_section('Selected Projects', [('Project 1','ACT and GPA Regression Analysis'), ('Project 2','Likelihood Ratio Test Derivations'), ('Project 3','MediaTek Stock Time Series Analysis'), ('Project 4','Latin Square and BIBD Experimental Design Presentation')])
add_section('Leadership and Activities', [('Leadership','Class representative for three years'), ('Activities','Science competition event organizer; volleyball team captain')])
add_section('Future Goal', [('Statement','To pursue graduate study in statistics and continue developing rigorous, data-driven research skills.')])

doc.build(story)
