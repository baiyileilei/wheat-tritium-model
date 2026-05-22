# Response surfaces and sensitivity analyses for an environmental model of dose calculations

**Authors**: Bertrand Iooss, François Van Dorpe, Nicolas Devictor

**Published in**: Reliability Engineering and System Safety, Volume 91, Issue 10-11, pp. 1241-1251 (2006)

**DOI**: (not provided, but journal is Elsevier)

**Available online**: 4 January 2006

**Keywords**: Radiological impact; Environmental transfer; Uncertainty analysis; Sensitivity analysis; Response surface

---

## Author Affiliations

- **Bertrand Iooss, Nicolas Devictor**: CEA Cadarache, DEN/DER/SESI/LCFR, 13108 Saint Paul lez Durance, Cedex, France
- **François Van Dorpe**: CEA Cadarache, DEN/DTN/SMTM/LMTE, 13108 Saint Paul lez Durance, Cedex, France

---

## Abstract

A parametric sensitivity analysis is carried out on GASCON, a radiological impact software describing the radionuclides transfer to the man following a chronic gas release of a nuclear facility. An effective dose received by age group can thus be calculated according to a specific radionuclide and to the duration of the release. In this study, we are concerned by 18 output variables, each depending of approximately 50 uncertain input parameters. First, the generation of 1000 Monte-Carlo simulations allows us to calculate correlation coefficients between input parameters and output variables, which give a first overview of important factors. Response surfaces are then constructed in polynomial form, and used to predict system responses at reduced computation time cost; this response surface will be very useful for global sensitivity analysis where thousands of runs are required. Using the response surfaces, we calculate the total sensitivity indices of Sobol by the Monte-Carlo method. We demonstrate the application of this method to one site of study and to one reference group near the nuclear research Center of Cadarache (France), for two radionuclides: iodine 129 and uranium 238. It is thus shown that the most influential parameters are all related to the food chain of the goat's milk, in decreasing order of importance: dose coefficient "effective ingestion", goat's milk ration of the individuals of the reference group, grass ration of the goat, dry deposition velocity and transfer factor to the goat's milk.

© 2005 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

The radiological impact evaluation of the nuclear facilities is one of the great challenge of the nuclear industry. Radiological exposure models due to severe nuclear accident or due to chronic releases have been extensively developed. In such complex models, it was recognized that many input variables are largely uncertain and that a rigorous procedure is required to arrive at realistic uncertainty distributions. Recently, uncertainty analysis techniques have been used in consequences investigation of different severe nuclear accident models [1-4].

This paper is devoted to the presentation of a global sensitivity analysis of a French radiological impact software called GASCON. GASCON is dedicated to chronic atmospheric releases and dosimetric impact, and is used for CEA facilities safety assessment. This software evaluates the doses received by a population (called reference group) exposed to the cloud of radionuclides and via the food ingestion pathways. It takes into account the interactions which exist between the man, the plant and the animal, the different pathways of transfer (wind, rain, ...), the distance between emission and observation, the time passed between emission and calculation, ...

Various stages in the analysis of a process (software, measurement, experiment,...) introduce potential errors, in particular, in the construction of the various models: real phenomenon with the physical model, physical model with the mathematical model, and mathematical model with the numerical model. The principal sources of uncertainties are in the approximation made by the modeling of the physical phenomenon, the approximations made on the parameterization of the model, the input data and the input parameters. The uncertainty analysis is used to evaluate the confidence interval or the probability distribution of the result. The global sensitivity analysis is used to quantify the influence of the input parameters uncertainties on the output variables uncertainties [5,6]. Recent studies have applied different methods of uncertainty and sensitivity analysis to environmental models for the radioactive waste management problem [7,8].

The results provided by GASCON are in the form of annual effective doses (Sv/year) received by a reference group, divided into three age compartments: adult, child and baby. We also distinguish three operating cycles of the gas release: one year, 10 years, 50 years. In our study the reference group is a village near the nuclear facility, and we consider two radionuclides $^{129}\text{I}$ and $^{238}\text{U}$. There is thus 18 output variables. The main ways of exposure taken into account in GASCON are:

- external exposures: radioactive cloud, soil deposits, groundshine;
- internal exposures: plume inhalation, ingestion of plants contaminated by direct pathway (foliar transfer by contact with the radioactive cloud) and indirect pathway (soil deposit then root transfer), ingestion of contaminated animal productions (animals having eaten plants contaminated by direct and indirect pathways).

Some input data are specific of the studied radionuclide or of the studied site (meteorological conditions, soils nature, feed rations, ...). We have deduced from the literature the variation ranges of parameters considered for the sensitivity analysis, which are:

- dose factors for external irradiation, effective ingestion, effective inhalation;
- transfer factors to animal productions (milk, meat of cow, ewe, goat, pig, ...);
- factors of soil-plant transfer (vegetables, cereals, fodder,...);
- translocation factors (fruits, vegetables, cereals, ...);
- sorption coefficients $K_d$ (sands, silts, clays and organic matter);
- dry deposition velocity for each radionuclide;
- local feed rations of the reference group for the various age compartments (vegetables, fruits, cereals, milk, meat, egg, ...), and animal feed rations (grass, hay, corn) related to the products eaten by the reference group.

The following section presents the four steps of our methodology: uncertainty analysis via Monte-Carlo calculations, sensitivity analysis by computations of correlation coefficients between input and output variables, construction of response surfaces requiring negligible computation times, final sensitivity analysis by calculations of Sobol sensitivity indices. In the third section this methodology is applied to the GASCON software using specific nuclear facility and reference group. We conclude this study with a summary in the last section.

---

## 2. Methodology

### 2.1. Uncertainty analysis

The general objective of an uncertainty analysis is to evaluate uncertainty on a computation result $Y$ taking into account uncertainties on the input parameters $X_j$ $(j = 1,\ldots,N_p)$. To do so, it is necessary to evaluate a probability density function for each input parameter (by expert opinion or by data statistical analysis). The results of the uncertainty analysis is conditioned with the choices of these probability densities. To propagate uncertainties, we use a simple Monte-Carlo strategy [9,10]: random generation of $N$ samples of input parameters, then software calculation for each sample. Therefore, we deduce output uncertainties by a statistical analysis of all software results.

The only information on the input parameters given by the experts of environmental radiological transfer are their variation bounds and their nominal values. There are no available measurements, nor complementary information on the input parameters. Therefore, for the distribution of each input parameter, we choose the uniform law which requires only the bounds of the parameter variation ranges. However, for the majority of the GASCON parameters, an order of magnitude separates the minimal and nominal values $(\min \sim \text{nominal}/10)$ and the nominal and maximal values $(\max \sim \text{nominal} \times 10)$. Thus, if we choose the uniform function on $[\min;\max]$, the majority of the simulated values will be included in the interval [nominal; max]. The triangular, log-normal or log-uniform laws would resolve this problem. However, because of their total lack of knowledge on the parameter distributions, the experts insist on the fact that all the values inside the variation ranges [min; nominal] and [nominal; max] have to be equiprobable (which is not the case for log-normal, log-uniform or triangular laws). Therefore, we find an heuristic (and arbitrary) way to respect such constraints. Each simulation proceeds in the following way:

- we simulate a uniform random variable $u$ on $[0;1]$
- if $u \leq 0.5$ the simulation value is $2u(\text{nominal} - \min) + \min \in [\min;\text{nominal}]$;
- if $u > 0.5$ the value is $(2u - 1)(\max - \text{nominal}) + \text{nominal} \in [\text{nominal};\max]$.

This procedure creates equiprobable random sampling on the intervals [min; nominal] and [nominal; max].

From the Monte-Carlo simulations, we obtain for each output variable its elementary statistical parameters (average, minimum, maximum, standard deviation, variation coefficient, skewness and Kurtosis coefficients) and its probability distribution. From the distributions, we can observe the spreading out of the output variables, the confidence intervals, the multiplicity of modes, ... Statistical comparison tests between output variables can also be made. In our study, we analyze nine output variables for each radionuclide, and we deduce by the Kolmogorov-Smirnov test [11] if there are or not statistically significant differences between their distributions with a certain degree of confidence. We also verify if the output variables are perfectly correlated. The linear correlation coefficient $\rho$ (or Pearson coefficient) between two random variables $X$ and $Y$ writes as follows:

$$\rho(X,Y) = \frac{\sum_{i=1}^{N}(X^{i} - \bar{X})(Y^{i} - \bar{Y})}{\sqrt{\sum_{i=1}^{N}(X^{i} - \bar{X})^{2}}\sqrt{\sum_{i=1}^{N}(Y^{i} - \bar{Y})^{2}}} \quad (1)$$

where $\bar{X}$ and $\bar{Y}$ are the averages of $X$ and $Y$ and $N$ is the number of $(X,Y)$ data. In summary, if two output variables are statistically similar with a correlation coefficient close to one, we conclude that the values taken by these variables (for each simulation) are very close and we study only one of these variables.

### 2.2. Sensitivity analysis with correlation coefficients

The global sensitivity analysis is used to quantify the contribution of each input parameter to the response variability. The Pearson coefficient $\rho$ (Eq. (1)) is the simplest sensitivity index. If $\rho$ is close to $+1$ or $-1$ the assumption of linearity between $X$ and $Y$ appears valid. If $Y$ is an output variable and if there are several input parameters $X_j$ $(j = 1,\ldots,N_p)$, the correlation coefficients between $Y$ and each $X_j$ is not a quantitative measure of their linearity degree, but it can reveal the linear character of some dominant parameters [11].

If the behavior of $Y$ compared to each parameter is overall linear, it is possible to obtain quantitative measurements of their influence from the regression coefficients $\alpha_j$ of the linear regression connecting $Y$ to the $\mathbf{X} = (X_1,\ldots,X_{N_p})$:

$$\hat{Y} = \alpha_0 + \sum_{j=1}^{N_p} \alpha_j X_j \quad (2)$$

where $\hat{Y}$ represents the estimation of $Y$ by the regression model. The standardized regression coefficients $\alpha_j^* = \alpha_j (\sigma_j / \sigma_Y)$ (where $\sigma_j$ and $\sigma_Y$ are the respective standard deviations of $X_j$ and $Y$) measures the variation of the response for a given variation of the parameter $X_j$. To obtain a measurement of the linearity of the relation between $Y$ and $X_j$, we use the partial coefficients of correlation $\rho_j$. In opposition to the standardized regression coefficients, the partial correlation coefficients allow to eliminate the influence from the other parameters [5].

In practice, we start by making the multiple linear regression between $Y$ and all the parameters $X_j$ (Eq. (2)) and we determine if their relation is approximately linear by calculating the coefficient of determination $R^2$ of this regression:

$$R^2(Y,\hat{Y}) = 1 - \frac{\sum_{i=1}^{N}(Y^{i} - \hat{Y}^{i})^{2}}{\sum_{i=1}^{N}(Y^{i} - \bar{Y})^{2}} \quad (3)$$

where $\bar{Y}$ is the average of $Y$ and $N$ is the number of $(\mathbf{X},Y)$ data. The coefficient $R^2$ represents the fraction of the variation compared to the average explained by the regression model, i.e. the variance percentage of output variables $Y$ explained by the regression model $\hat{Y}$. Therefore, if $R^2$ is close to one, the relation connecting $Y$ to all the parameters $X_j$ is almost linear and we can use the standardized regression coefficients $\alpha_j^*$ as sensitivity indices.

If the relation between two variables $X$ and $Y$ is not linear, the correlation coefficients of the ranks (or Spearman coefficients) can be used. By replacing the values $X^1,\ldots,X^N$ and $Y^1,\ldots,Y^N$ by their rank, the assumption of linearity is replaced by the assumption of a monotonic relation. The Spearman coefficient is calculated by [11]:

$$\rho^S(X,Y) = 1 - \frac{6\sum_{k=1}^{N}(\nu_X^k - \nu_Y^k)^2}{N(N^2 - 1)} \quad (4)$$

where $\nu_X^k$ is the rank of $X^k$ and $\nu_Y^k$ is the rank of $Y^k$. In the same way, one can calculate the standardized rank regression coefficients and the partial rank correlation coefficients (allowing to determine if the relation between $Y$ and each $X_j$ is monotonous) by carrying out the linear regressions on the ranks.

The regression or correlation coefficients are related to linear or monotonic assumptions. Moreover, these coefficients allow to study only the relations between the output variable and an input parameter independently of the other parameters. In real world, many problems are neither linear nor monotonous, and reveal physical dependences between parameters. Global sensitivity analyses more adapted to these conditions are available, but they are definitely much more expensive in computing times [5]. This requisite computation time makes impossible the application of these techniques to our study on the GASCON software (30 s by calculation, 50 input parameters, 18 output variables). If we want to use these techniques, it is necessary to simplify the GASCON software by replacing it by a surrogate model, that we call a response surface.

### 2.3. The response surface method

The response surface method [12] is used to build a function which simulates the behavior of a physical or chemical phenomenon in the field of variation of the influential parameters, starting from a certain number of experiments. It was originally proposed as a statistical tool, to find the operating conditions of a chemical process at which some response was optimized. Subsequent generalizations led to these methods being used to develop approximating functions that surrogate for long running computer codes [13-17]. These surrogate response surface models fit data that are generated by running the simulation model at selected points in the parameter space. Building such a response surface aims to obtain a mathematical model representative of the studied software, having good capacities of prediction, and for which computing time to evaluate an output variable is negligible. It will be thus efficient for the uncertainty and sensitivity analyses, requiring several thousands of simulations.

There are different issues involved in selecting runs for uncertainty analysis and correlation coefficients computation compared with selecting runs for building a response surface [12,18,19]. For this latter purpose, one can often do better than random selection by making hypothesis on the response surface model and on the interactions between parameters. We will not use a specific strategy here because we are not restricted to a specific response surface model. We choose to construct the response surface with all our available calculations, and we adapt our statistical analyses to this choice.

To build a response surface, it is necessary to have the following elements:

- the software $H$ which models the studied phenomenon;
- a sample $D$ of $N$ points $(\mathbf{X}^i, Y^i)$ where $\mathbf{X}^i$ is a vector of the $N_p$ random input parameters and $Y^i = H[\mathbf{X}^i]$ $(i = 1\ldots N)$ is the software response;
- a family $F$ of functions $f(\mathbf{X},\mathbf{c})$ where $\mathbf{c}$ is a vector of parameters (parametric regression) or indices (nonparametric regression), which makes possible the identification of the various elements of $F$.

In our application, we look for a response surface in the form of a polynomial without any restriction on its order. Therefore, $F$ is the polynomial family and $\mathbf{c}$ are the regression coefficients.

There are multiple response surface families [20,15]: polynomials, splines, interpolating radial functions, kriging, generalized linear models, partial least squares, neural networks, regression trees, support vector machines, ... Originally, the response surface method was developed for linear and quadratic functions [12]. For such function, input parameter values can be optimally selected by experimental design over the parameter space. We have not restricted our study to linear and quadratic functions because we know that there are strong interactions at multiple orders between input parameters in the equations of the GASCON software. Therefore, the random sampling strategy is useful: we construct the response surface with the $N$ Monte-Carlo simulations done in the first stage of our methodology (i.e. the uncertainty analysis).

In general, we use the technique of least squares to obtain the best representing function $f_0$ in the family $F$. We minimize the function $\sum_{i=1}^{N}[Y^i - f(\mathbf{X}^i,\mathbf{c})]^2$ in relation to the parameters $\mathbf{c}$, to obtain an optimal $\mathbf{c}_0$ and the response surface $f_0(\mathbf{X}) = f(\mathbf{X},\mathbf{c}_0)$. It is also possible to use a weighted least-squares method. The statistical accuracy of the response surfaces can be assessed by cross-validation or bootstrap techniques [20]. The cross-validation method allows to have a good estimation of the theoretical prediction error associated with the response surface, while the bootstrap method is especially useful when the size of the data sample is small.

In our study, due to the large size of our data sample (1000 calculations), we choose a simpler method: the approximation quality of the response surface is given from a statistical analysis on a construction database (used to construct the response surface), whereas the quality of prediction is deduced from a prediction database. The points in the prediction database are not used to construct the response surface. Therefore, we use the following steps to validate the response surface:

- We initially compare on the two databases some indicators obtained from the response surface $f_0$ with those obtained directly with software $H$: average, standard deviation, minimum and maximum.
- A regression analysis allows to determine the share of variability of the output variable explained by the fitted model. We particularly pay attention to two statistics which give global measurements of correlation between two data sets: the Pearson correlation coefficient $\rho$ given in Eq. (1) and the coefficient of determination $R^2$ given in Eq. (3). The coefficient $R^2$ represents the percentage of output variables explained by the response surface. In our case, we calculate these statistics between the software response $Y = H[\mathbf{X}]$ and the response surface $\hat{Y} = f_0(\mathbf{X})$. The values of these statistics have to be approximately equal using the points of the database of construction and those of the database of prediction.
- The previous criteria are global and it is possible that the data adjusted are not homogeneous. This is the case when the studied variable covers a broad range of variations with multiple orders of magnitude. In this case, the contributions of the low values to the $R^2$ measurement are negligible. To cure this problem, the study of residual statistics gives some indications of the regression accuracy. The residuals $\epsilon = Y - \hat{Y}$ have to follow a Gaussian distribution of mean zero, with a constant standard deviation $\sigma_{\epsilon}$ small compared to the GASCON standard deviation $\sigma_Y$. We also examine the average and the standard deviation of the relative residuals

$$\frac{\epsilon^i}{\hat{Y}^i} = \frac{Y^i - \hat{Y}^i}{\hat{Y}^i} \quad (5)$$

The response surface is valid on all the field of variation if the following average and standard deviation are weak: $(\epsilon/\hat{Y}) \ll 1$ and $\sigma(\epsilon/\hat{Y}) \ll 1$.

### 2.4. Global sensitivity analysis

We consider methods of variance analysis which aim at determining the weight of the variance of the response $Y = f(\mathbf{X})$, with $\mathbf{X} = (X_1,\ldots,X_{N_p})$, resulting from a variable or a group of variables [21,5]. For example, the first and second order global sensitivity indices are defined as

$$S_i = \frac{\text{Var}[\mathbb{E}(Y|X_i)]}{\text{Var}(Y)}, \quad S_{ij} = \frac{\text{Var}[\mathbb{E}(Y|X_i X_j)]}{\text{Var}(Y)} \quad (6)$$

Our final objective is to calculate the global sensitivity index $St_i$ defined as the sum of all the sensitivity indices in which $i$ appears as index:

$$St_i = \sum_{k \neq i} S_k \quad (7)$$

with $\sum_{k \neq i}$ the sum of all the terms in which $i$ appears as index. By a judicious variance decomposition, the Sobol method allows a relatively simple evaluation of the terms $S_i, S_{ij}, \ldots$ [22].

In practice, we can evaluate Sobol indices by the FAST method or the Monte-Carlo method [5]. The Monte-Carlo method requires a very significant number of simulations, typically $N_s = 10000$ to estimate an index $(S_i, S_{ij}, \ldots$ or $St_i$) for one input parameter and one output variable. This justifies the use of response surfaces to minimize the computing times. Although the calculation of Sobol indices with FAST method is definitely less expensive, we use the Monte-Carlo method because we obtain realistic (to the extent that the response surface is realistic) confidence intervals on the Sobol indices by repeating these index calculations. This information is essential if we want to rigorously classify the influence of the various input parameters. In our study, we carry out $N_{ci} = 200$ calculations of each Sobol index. Moreover, the Monte-Carlo method calculates all the Sobol indices $(S_i, S_{ij}, \ldots$ or $St_i$), which bring information on the interactions between the input parameters. In our study, we just calculate $S_i$ and $St_i$ to measure the influence of $X_i$ while acting alone. Saltelli [23] describes a Monte-Carlo method to calculate these two indices using the same $N_s$ simulations.

For the model $Y = f(\mathbf{X})$ where $\mathbf{X}$ is a vector of $N_p$ parameters, we need $N_{ci} \times N_s \times (N_p + 2)$ evaluations of $f$ to calculate the first order indices $S_i$ and total indices $St_i$ for all the parameters $X_i$, and to allocate a confidence interval to each estimation. In our study, $N_s = 10000$ and $N_{ci} = 200$. The value of $N_p$ depends on the model of response surface which is adjusted. For GASCON, we take into account approximately 10 parameters in each polynomial response surface. Therefore, for $N_p = 10$ there will be $2.4 \times 10^7$ calculations of $f$.

---

## 3. Results

The GASCON software has been applied to a particular facility on Cadarache, a French nuclear research center. The reference group is the population of a village, distant of a few kilometers of this facility. The gas release ($^{129}\text{I}$ and $^{238}\text{U}$) is fixed at a symbolic value of $1\ \text{Bq}$/year which does not represent a realistic release. This also induces nonrealistic effective dose rates. Three operating cycles are studied: one year, 10 years, and 50 years.

### 3.1. Uncertainty analysis

We perform 1000 random independent Monte-Carlo simulations of the GASCON software (30 s per simulation) with the methodology of Section 2.1. In Fig. 1, the distributions of 12 output variables are represented. It is noted immediately that the distributions for $^{238}\text{U}$ are much tightened than the distributions for $^{129}\text{I}$. This indicates that the variations of the input parameters for $^{238}\text{U}$ have less influence than the variations of the input parameters for $^{129}\text{I}$.

For a given radionuclide, the output variable distributions seem very similar. We carry out statistical tests between the coherent output variables (same radionuclide, same age compartment or same operating cycle) by the Kolmogorov-Smirnov test. This test evaluates if there are or not statistically significant differences between two distributions on the degree of confidence $95\%$. We also calculate the Pearson correlation coefficients between each couple of output variables.

For $^{129}\text{I}$, there is no difference at $95\%$ between all the distribution couples, except between (adult, operating cycle of 50 years) and (baby, operating cycle of 1 year), and between (adult, operating cycle of 50 years) and (baby, operating cycle of 10 years). Moreover, the Pearson correlation coefficients between each couple of output variables are approximately equal to one $(>0.99)$. For $^{238}\text{U}$, all distribution couples have differences at $95\%$, except between (adult, 1 year cycle) and (adult, 10 years cycle), between (child, 1 year cycle) and (child, 10 years cycle), and between (baby, 1 year cycle) and (baby, 10 years cycle). Furthermore, the Pearson correlation coefficient between each couple of output variables are approximately equal to one $(>0.99)$, except for couples involving (adult, 50 years cycle) and (child, 50 years cycle). The correlation between these two variables is equal to one.

In summary, the variables at 10 years have approximately the same distributions than the variables at one year, and for $^{129}\text{I}$ the variables "child" have the same distributions than the variables "adult". The Pearson correlation coefficients between each couple of variables are close to one except for the couples involving (adult, 50 years cycle) and (child, 50 years cycle). Thus, by using the rule given at the end of paragraph 2.1, we can consider that it is sufficient to study four output variables by radionuclide: (adult, 1 year cycle), (adult, 50 years cycle), (baby, 1 year cycle), and (baby, 50 years cycle).

### 3.2. Sensitivity analysis with correlation coefficients

**Table 1. Pearson correlation coefficients (in %) between the output and input variables (selected if $\rho$ is higher than 8%)**

| | $\rho$ (Pearson) | ineff | gmilk | ra_gmilk | grass_goat | dep | ra_cer | vegfr |
|---|---|---|---|---|---|---|---|---|
| Adult, $^{129}\text{I}$, 1 year | | 33 | 9 | 31 | 28 | 21 | | |
| Adult, $^{129}\text{I}$, 50 years | | 33 | 9 | 31 | 28 | 21 | | |
| Baby, $^{129}\text{I}$, 1 year | | 32 | 9 | 31 | 28 | 21 | | |
| Baby, $^{129}\text{I}$, 50 years | | 32 | 9 | 31 | 28 | 21 | | |
| Adult, $^{238}\text{U}$, 1 year | | 28 | 20 | 21 | 18 | 15 | 8 | |
| Adult, $^{238}\text{U}$, 50 years | | 36 | 17 | 18 | 15 | 20 | 10 | |
| Baby, $^{238}\text{U}$, 1 year | | 25 | 21 | 21 | 18 | 15 | 8 | |
| Baby, $^{238}\text{U}$, 50 years | | 27 | 20 | 21 | 18 | 16 | 8 | |

**Table 2. Spearman correlation coefficients (in %) $\rho^S$ between the output and input variables (for the same variables as in Table 1)**

| | $\rho^S$ (Spearman) | ineff | gmilk | ra_gmilk | grass_goat | dep | ra_cer | vegfr |
|---|---|---|---|---|---|---|---|---|
| Adult, $^{129}\text{I}$, 1 year | | 55 | 16 | 46 | 41 | 38 | | |
| Adult, $^{129}\text{I}$, 50 years | | 56 | 16 | 45 | 41 | 39 | | |
| Baby, $^{129}\text{I}$, 1 year | | 54 | 16 | 47 | 42 | 37 | | |
| Baby, $^{129}\text{I}$, 50 years | | 54 | 16 | 47 | 42 | 38 | | |
| Adult, $^{238}\text{U}$, 1 year | | 55 | 24 | 29 | 26 | 20 | 11 | |
| Adult, $^{238}\text{U}$, 50 years | | 62 | 19 | 21 | 20 | 29 | 19 | |
| Baby, $^{238}\text{U}$, 1 year | | 53 | 33 | 37 | 33 | 26 | 10 | |
| Baby, $^{238}\text{U}$, 50 years | | 59 | 29 | 32 | 28 | 21 | 8 | |

Tables 1 and 2 show the largest Pearson and Spearman correlation coefficients between input and output variables. These results allow to emphasize some input parameters which have a strong influence on the variability of the response. All the output variables reveal five important input parameters: the dose factor of effective ingestion ineff, the human feed ration of goat's milk ra_gmilk, the goat feed ration of grass_grass_goat, the dry deposition velocity of the radionuclide dep, and the transfer factor to the goat's milk gmilk. For $^{238}\text{U}$, some additional parameters appear: the human feed ration of cereals ra_cer and the transfer factor to the vegetables fruits vegfr. The parameters ineff, dep, gmilk and vegfr are related to a given radionuclide.

We have calculated the $R^2$ coefficient of the multiple linear regression connecting the output variables and all the input parameters. The results are the following:

- $R^2(\text{adult}, ^{129}\text{I}, 1\ \text{year}) = R^2(\text{adult}, ^{129}\text{I}, 50\ \text{years}) = 36\%$;
- $R^2(\text{baby}, ^{129}\text{I}, 1\ \text{year}) = R^2(\text{baby}, ^{129}\text{I}, 50\ \text{years}) = 36\%$;
- $R^2(\text{adult}, ^{238}\text{U}, 1\ \text{year}) = 26\%$;
- $R^2(\text{adult}, ^{238}\text{U}, 50\ \text{years}) = 31\%$;
- $R^2(\text{baby}, ^{238}\text{U}, 1\ \text{year}) = 25\%$;
- $R^2(\text{baby}, ^{238}\text{U}, 50\ \text{years}) = 26\%$.

We see that $R^2 \ll 100\%$ for all the output variables. It means that the relations between each output variable and the input parameters are not linear, and that interactions between input parameters have to be taken into account to explain output variables. Therefore, the linear sensitivity indices, like standardized regression coefficients, cannot be used in this context.

### 3.3. Response surface methodology

#### 3.3.1. Response surfaces construction

At present, we want to adjust a response surface for each output variable. In a first time, we look for a response surface in the family $F$ of the polynomial models (obtained by multiple polynomial regression). There are approximately 50 parameters for each output variable. The polynomials are constructed using the 1000 initial Monte-Carlo calculations of the GASCON software. For each output variable, we retain the best representing polynomial. Stepwise regression analysis is used to limit the terms number inside each polynomial and to avoid over-fitting phenomena.

The multiple regressions with a first order polynomial model (linear model) or with a second order polynomial model give very poor results with $R^2 < 50\%$. By selecting and combining the parameters found in Table 1, the best results are obtained when the regressions are made according to certain food chains, which are linear combinations of the various terms contributing in each food chain. For example, the food chain of the goat's milk writes as follows:

$$a_1 X_1 X_2 X_3 X_4 X_6 + a_2 X_1 X_2 X_3 X_4 X_6^2 + a_3 X_1 X_2 X_3 X_5 X_6 + a_4 X_1 X_2 X_3 X_5 X_6^2 \quad (8)$$

where $a_i\ (i=1\ldots 4)$ are the regression coefficients, and all the input factors $X_j$ have been defined in the previous paragraph:

- $X_1 = \text{ingeff}$,
- $X_2 = \text{gmilk}$,
- $X_3 = \text{ra\_gmilk}$,
- $X_4 = \text{grass\_goat}$,
- $X_5 = \text{hay\_goat}$ (the goat feed ration of hay), and
- $X_6 = \text{dep}$.

In the sixth order polynomial of Eq. (8), we can see the fifth order interactions between $X_1, X_2, X_3, X_4, X_6$ and between $X_1, X_2, X_3, X_5, X_6$. It is noticed that the dry deposition velocity $X_6 = \text{dep}$ operates linearly and quadratically in this food chain. This is due to the fact that the relations in GASCON utilize dep like a power of another factor.

For all the output variables in $^{129}\text{I}$, the best response surfaces obtained by multiple regression are polynomials based on the food chains of the goat's milk and the ewe's milk:

$$\begin{aligned}
f_1(\mathbf{X}) = & a_0 + a_1 X_1 X_2 X_3 X_4 X_6 + a_2 X_1 X_2 X_3 X_4 X_6^2 \\
& + a_3 X_1 X_2 X_3 X_5 X_6 + a_4 X_1 X_2 X_3 X_5 X_6^2 \\
& + a_5 X_1 X_7 X_8 X_9 X_6 + a_6 X_1 X_7 X_8 X_9 X_6^2 \\
& + a_7 X_1 X_7 X_8 X_{10} X_6 + a_8 X_1 X_7 X_8 X_{10} X_6^2 \quad (9)
\end{aligned}$$

where $a_i\ (i=0\ldots 8)$ are the regression coefficients, and with $X_1, X_2, X_6$ related to the radionuclide $^{129}\text{I}$, $X_7$ the $^{129}\text{I}$ transfer factor to the ewe's milk, $X_8$ the human feed ration of ewe's milk, $X_9$ the ewe feed ration of grass, $X_{10}$ the ewe feed ration of hay. For simplicity and because of space limitations, the values of the regression coefficients are not given in this paper.

We have the same result $f_1(\mathbf{X})$ (Eq. (9)) for the variables (baby, $^{238}\text{U}$, 1 year cycle) and (baby, $^{238}\text{U}$, 50 years cycle), with $X_1, X_2, X_6, X_7$ related to the radionuclide $^{238}\text{U}$. For the variable (adult, $^{238}\text{U}$, 1 year cycle), the obtained response surface is

$$f_2(\mathbf{X}) = f_1(\mathbf{X}) + a_9 X_{11} \quad (10)$$

where $a_i\ (i=0\ldots 9)$ are the regression coefficients and $X_{11}$ is the $^{238}\text{U}$ dose factor of effective inhalation. For (adult, $^{238}\text{U}$, 50 years cycle), we add the food chain of the pig's meat and the food chain of the vegetable fruits by indirect transfer and we obtain the following response surface:

$$\begin{aligned}
f_3(\mathbf{X}) = & f_2(\mathbf{X}) + a_{10} X_1 X_{12} X_{13} X_{14} X_6 \\
& + a_{11} X_1 X_{12} X_{13} X_{14} X_6^2 \\
& + a_{12} X_1 X_{15} X_{16} X_6 + a_{13} X_1 X_{15} X_{16} X_6^2 \quad (11)
\end{aligned}$$

where $a_i\ (i=0\ldots 13)$ are the regression coefficients, and with $X_{12}$ the $^{238}\text{U}$ transfer factor to the meat of the pig, $X_{13}$ the human feed ration of pig meat, $X_{14}$ the pig feed ration of corn, $X_{15}$ the $^{238}\text{U}$ soil-plant transfer factor to the vegetables fruits, $X_{16}$ the human feed ration of vegetable fruits.

The sixth order polynomials $f_1, f_2$ and $f_3$ have not been found via automatic regression procedure because of the important number of input parameters (50). To find such complex interactions, we have used our expert knowledge (related to the food chains) on the physical interactions between input parameters modelized in the GASCON software.

#### 3.3.2. Response surfaces validation

The statistical validity of each response surface is studied on a construction database (of size $\frac{2}{3}$ of the complete data base) and on a prediction database (of size $\frac{1}{3}$ of the complete data base). Points inside each database are chosen randomly. For $^{129}\text{I}$, the statistics of the $R^2$ and $\rho$ (Eqs. (3) and (1)) are excellent: they are equal to $99\%$ for all the variables and for the two databases. The responses in $^{129}\text{I}$ of the GASCON software are almost entirely explained by the terms of the food chain of the goat's milk. For $^{238}\text{U}$, by introducing in the model the food chains of the goat's milk, the ewe's milk, the pig's meat and the effective inhalation, the statistics $R^2$ and $\rho$ are also satisfactory (all higher than $92\%$). Sixth order polynomials would cause over-fitting by giving very good results on the construction database and very poor on the prediction database. However, there is no over-fitting in our case: the statistics on the prediction database and on the construction database are similar because we have limited the number of regression terms in our polynomials: eight terms in $f_1$, 9 in $f_2$, and 13 in $f_3$.

It thus seems that the response surfaces are relatively accurate in approximation and prediction; but the relative statistics balance our judgment: the relative standard deviations $\sigma_{\epsilon}/\sigma_Y$ (where $\sigma_{\epsilon}$ and $\sigma_Y$ are respectively the residuals and GASCON standard deviations) are worth roughly $10\%$ for $^{129}\text{I}$ and $20\%$ for $^{238}\text{U}$. This lets suppose that the adjustments are not good everywhere. The calculation of the averages and standard deviations of the relative residuals (Eq. (5)) confirms this judgment. For $^{129}\text{I}$, the relative inadequacy between GASCON and the response surface is on average of $-30\%$ with a $40\%$ standard deviation. For $^{238}\text{U}$, the relative inadequacy between GASCON and the response surface is on average of $-15\%$ with a $40\%$ standard deviation. The Fig. 2 makes it possible to locate the problem thanks to a comparison between GASCON and response surface in logarithmic scale. It is noted that the highest values $(>10^{-14}\ \text{Sv/year})$ obtained by GASCON are well adjusted, whereas the lowest values are completely overestimated by the response surface. However in absolute value, we remark that the overestimation is relatively small (approximately $10^{-14}\ \text{Sv/year}$).

**Figure 2. For the adult, $^{129}\text{I}$ and one year of release, comparisons between response surface and GASCON calculations (in Sv/year) for the two databases: (a) construction base; (b) prediction base. The response surface has been found by multiple polynomial regression on the raw input and output values.**

This problem of regression on a field of several orders of magnitude can be solved by using the technique of weighted least squares. In the minimization of the functional, allocating larger weights to smaller values leads to an homogeneous response surface on all the field of variation.

We can also use another classical solution: making the regression on the logarithmic values of the input parameters and output variables. By taking logarithmic values of input parameters, the regression becomes strictly linear. We choose all the input parameters as regression factors, and make a backward stepwise linear regression [20] to progressively eliminate all terms whose contribution is negligible inside the regression (with a probability threshold of 0.01). For example, for (adult, $^{129}\text{I}$, 1 year cycle), the retained input factors are the following: $X_1 = \text{ingeff}$, $X_2 = \text{gmilk}$, $X_3 = \text{ra\_gmilk}$, $X_4 = \text{grass\_goat}$, $X_5 = \text{hay\_goat}$, $X_6 = \text{dep}$, $X_7 = \text{emilk}$, $X_8 = \text{ra\_emilk}$, $X_9 = \text{grass\_ewe}$, $X_{10} = \text{hay\_ewe}$. All these factors appear in the polynomial response surface terms found by regression on raw data. The response surface writes

$$\log[f_4(\mathbf{X})] = -24 + 0.97\log(X_1) + 0.69\log(X_2) + 0.75\log(X_3) + 0.57\log(X_4) + 0.15\log(X_5) + 0.63\log(X_6) + 0.18\log(X_7) + 0.21\log(X_8) + 0.17\log(X_9) + 0.03\log(X_{10}) \quad (12)$$

For (adult, $^{129}\text{I}$, 1 year cycle), the result statistics are the following: $R^2 = 85\%$ and $\rho = 92\%$ for the construction and prediction databases. As shown by the adjustments presented in Fig. 3, the adequacy between GASCON and the response surface is relatively good in all the domain of variations. This is confirmed by the relative residuals statistics, much better than previously: the relative inadequacy between GASCON and the response surface is on average of $-10\%$ with a $50\%$ standard deviation.

**Figure 3. For the adult, $^{129}\text{I}$ and one year of release, comparisons between response surface and GASCON calculations (in Sv/year) for the two databases: (a) construction base; (b) prediction base. The response surface has been found by multiple polynomial regression on the logarithms of the input and output values.**

We have also used neural networks as response surfaces on the logarithmic values of input and output variables. Our best result is a two layers neural network with nine and ten nodes on each layer. Results are similar than the results with the log-linear model: $R^2 = 90\%$ for (adult, $^{129}\text{I}$, 1 year cycle), with average relative inadequacy of $-10\%$ with a $50\%$ standard deviation. In conclusion, we prefer to use the polynomial models for simplicity and computation time reason (neural network is a complex combination of sigmoid functions), and for the physics understanding that it provides: neural network is a "black box" while input parameters clearly appear in a polynomial model.

### 3.4. Global sensitivity analysis

At present, the GASCON software can be replaced by the response surface, which is used to calculate Sobol indices by extensive Monte-Carlo computations. As we are interested by largest annual effective dose values, we consider the sixth order polynomial models (Eqs. (9), (10) and (11)) as response surfaces (fitting on the raw values of input and output variables). These response surfaces have shown very good adequacy for the highest dose values.

**Figure 4. Sobol indices for each parameter. Uncertainty bar represents the minimum, average and maximum indices obtained with 200 Sobol calculations. The numbers 1 and 50 in the parentheses are the numbers of release years.**

Fig. 4 gives for each output variable the total Sobol indices of the most influential parameters, with their error bars (minimum and maximum). Having repeated 200 times the Sobol calculations, the average values are good estimates of the exact total Sobol indices. Of course, the error bars do not reflect uncertainty due to the use of the response surface rather than the true software GASCON. However, the prediction errors of the used response surface are not biased. Then, taking the average Sobol indices of a lot of Sobol calculations would lead to a correct estimation of the true Sobol index. It would be interesting to confirm this by a specific study in a future work.

We conclude that for $^{129}\text{I}$, the most influential parameters are the dose factor of effective ingestion and the feed ration of the goat's milk. For $^{238}\text{U}$, the most influential parameters are the dose factor of effective ingestion, the transfer factor to the goat's milk and the feed ration of the goat's milk. Another result (not shown here) is that the values of first order Sobol indices are negligible compared to the total Sobol indices. This shows that input parameters have no individual influence on the output variability.

By carrying out calculations of the Sobol indices on the response surface obtained after logarithmic transformation, we obtain similar results with small differences. For example, we obtain for (adult, $^{129}\text{I}$, 1 year cycle) in decreasing order:

- $St(\text{ingeff}) = 0.55 \pm 0.052$,
- $St(\text{grass\_goat}) = 0.452 \pm 0.047$,
- $St(\text{ra\_gmilk}) = 0.374 \pm 0.045$,
- $St(\text{hay\_ewe}) = 0.34 \pm 0.052$,
- $St(\text{emilk}) = 0.124 \pm 0.041$,
- $St(\text{ra\_emilk}) = 0.073 \pm 0.036$,

where the value after $\pm$ is the standard deviation of the average estimation. We see that the average ratio of hay and the transfer factor to the ewe's milk have stronger influence than previously. We conclude that the uncertainties on the ewe food chain parameters have some influence on the lowest annual effective dose values, but not on the highest annual effective dose values where the goat food chain parameters are pre-eminent. Furthermore, we see also in this case that the values of first order Sobol indices are negligible compared to the total Sobol indices.

---

## 4. Conclusion

The four steps of our methodology (Monte-Carlo simulation, correlation coefficients analysis, response surfaces construction, Sobol indices calculation) have allowed to quantify the influence of input parameters on the GASCON software response (annual effective dose received by the man), for a specific nuclear facility, a specific population, and for two radionuclides $^{129}\text{I}$ and $^{238}\text{U}$. During the correlation coefficient analysis, the calculations of standardized rank regression coefficients and partial rank correlation coefficients would bring more information on important input parameters. During the response surface construction, other statistical validation methods like cross-validation or bootstrap technique could also be useful [20]. In this work, the response surfaces found are in simple polynomial form explicit for the physicist understanding. For the approximation of software simulating more complex phenomena, more elaborated and not explicit response surfaces, like neural networks [24,16], can be used.

The methodology shown in this paper is efficient in a lot of applications of nuclear engineering, where processes are often huge and complex. In addition to the radiological impact application of this paper, let us mention the radioactive waste disposal [7], the severe accident computer codes [25], the irradiation monitoring of nuclear vessels (example illustrated in [26]), ....

---

## Acknowledgements

This work was supported by the MRIMP project of the "Risk Control Domain" which depends on CEA/Nuclear Energy Division/Nuclear Development and Innovation Division. We are grateful to P. Guetat (CEA/DAM/DASE) for providing the GASCON software.

---

## References (selected)

[1] Helton JC, Johnson JD, Shiver AW, Sprung JL. Uncertainty and sensitivity analysis of early exposure results with the MACCS reactor accident consequence model. Reliab Eng Syst Saf 1995;48:91-127.

[2] Helton JC, Johnson JD, Rollstin JA, Shiver AW, Sprung JL. Uncertainty and sensitivity analysis of food pathway results with the MACCS reactor accident consequence model. Reliab Eng Syst Saf 1995;49:109-44.

[3] Helton JC, Johnson JD, Rollstin JA, Shiver AW, Sprung JL. Uncertainty and sensitivity analysis of chronic exposure results with the MACCS reactor accident consequence model. Reliab Eng Syst Saf 1995;50:137-77.

[4] Ehrhardt J, Jones JA, Goossens LHJ. Probabilistic accident consequence uncertainty analysis of the whole program package COSYMA. Radiat Prot Dosim 2000;90(3):365-72.

[5] Saltelli A, Chan K, Scott EM, editors. Sensitivity analysis. Wiley series in probability and statistics. New York: Wiley; 2000.

[6] Campolongo F, Saltelli A. Sensitivity analysis of an environmental model: an application of different analysis methods. Reliab Eng Sys Saf 1997;57:49-69.

[7] Helton JC. Uncertainty and sensitivity analysis techniques for use in performance assessment for radioactive waste disposal. Reliab Eng Syst Saf 1993;42:327-67.

[8] Hedin A. Probabilistic dose calculations and sensitivity analyses using analytical models. Reliab Eng Syst Saf 2003;79:195-204.

[9] Liu JS. Monte Carlo strategies in scientific computing. Springer series in statistics. Berlin: Springer; 2003.

[10] Helton JC, Davis FJ. Latin hypercube sampling and the propagation of uncertainty in analyses of complex systems. Reliab Eng Syst Saf 2003;81:23-69.

[11] Saporta G. Probabilités, analyse des données et statistique. Editions Technip; 1990.

[12] Box G, Draper N. Empirical model building and response surfaces. New York: Wiley; 1987.

[13] Sacks J, Welch WJ, Mitchell TJ, Wynn HP. Design and analysis of computer experiments. Statist Sci 1989;4:409-35.

[14] Kleijnen J. Sensitivity analysis and related analyses: a review of some statistical techniques. J Statist Comput Simul 1997;57:111-42.

[15] Kleijnen J, Sargent RG. A methodology for fitting and validating metamodels in simulation. Europ J Oper Res 2000;120:14-29.

[16] Devictor N, Martinez J-M. Non linear regression methods in uncertainty and sensitivity studies and reliability computations. In: Proceedings of ESREL '2000, Edinburgh, UK; May 2000.

[17] Rutherford B. A response-modeling alternative to surrogate models for support in computational analyses. In: Proceedings of SAMO 2004, Santa-Fe, New Mexico, USA; March 2004.

[18] Santner TJ, Williams BJ, Notz WI. The design and analysis of computer experiments. Springer series in statistics. Berlin: Springer; 2003.

[19] Kleijnen J. An overview of the design and analysis of simulation experiments for sensitivity analysis. Europ J Oper Res 2005;164:287-300.

[20] Hastie T, Tibshirani R, Friedman J. The elements of statistical learning. Berlin: Springer; 2002.

[21] McKay MD. Non parametric variance-based methods of assessing uncertainty importance. Reliab Eng Syst Saf 1997;57:267-79.

[22] Sobol IM. Sensitivity estimates for non linear mathematical models. Math Modelling Comput Exp 1993;1:407-14.

[23] Saltelli A. Making best use of model evaluations to compute sensitivity indices. Comput Phys Commun 2002;145:280-97.

[24] Dreyfus G, Martinez J-M, Samuelides M, Gordon MB, Badran F, Thiria S, Hérault L. Réseaux de neurones - Méthodologie et applications, Eyrolles; 2002.

[25] Devictor N. Advances in methods for uncertainty and sensitivity analysis. International workshop on level 2 PSA and severe accident management, OCDE/AEN/CSNI/WGRISK, Cologne, Germany; March 2004.

[26] Jacques J, Lavergne C, Devictor N. Sensitivity analysis in presence of model uncertainty and correlated inputs. In: Proceedings of SAMO 2004, Santa-Fe, New Mexico, USA; March 2004.