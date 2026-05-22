# Simulating energy and carbon fluxes over winter wheat using coupled land surface and terrestrial ecosystem models

**Vivek K. Arora\***

*Canadian Centre for Climate Modelling and Analysis, Meteorological Service of Canada, University of Victoria, Victoria, Canada BC V8W 2Y2*

Received 24 June 2002; received in revised form 20 March 2003; accepted 20 March 2003

## Abstract

Coupled land surface and terrestrial ecosystem models are used to simulate energy and carbon fluxes over winter wheat at the Ponca City, Oklahoma, Ameriflux site. The terrestrial ecosystem model consists of photosynthesis and respiration (autotrophic and heterotrophic) sub-modules, which uses canopy temperature, soil moisture, and soil temperature simulated by the land surface scheme. The photosynthesis sub-module, which provides an estimate of canopy conductance to the land surface scheme, is designed to use both the big- and the two-leaf (sunlit/shaded) approaches, and canopy conductance formulations based on both relative humidity and vapor pressure deficit. This provides a tool to test the sensitivity of model results to these two different approaches of modeling photosynthesis and stomatal conductance. Model results for carbon and energy fluxes compare well with observations over the growing season of 1997, especially with the use of the two-leaf model and stomatal conductance formulation based on vapor pressure deficit. Averaged over the growing season, the model results suggest that for this particular site, the difference in simulated latent heat fluxes caused by the choice of the photosynthesis approach (big- or two-leaf) is smaller $(\sim 1\%)$ than the difference caused by the choice of the stomatal conductance formulation $(\sim 10\%)$. In regard to the carbon fluxes, averaged over the growing season and compared with the two-leaf model, the simulated net photosynthesis rate and net ecosystem exchange flux are about 5 and $18\%$ higher, respectively, for the big-leaf model. It is shown that comparisons with both observed energy and carbon fluxes are necessary to constrain model behavior and test its performance adequately.

Crown Copyright © 2003 Published by Elsevier B.V. All rights reserved.

**Keywords:** Photosynthesis; Stomatal conductance; Ecosystem model; Land-atmosphere CO₂ exchange

## 1. Introduction

Vegetation and ecosystem dynamics exert control over climate at a range of temporal and spatial scales via many different physical processes. At the time scale of a few hours to a few months, vegetation influences the atmospheric processes through its effect on the partitioning of net radiation into latent and sensible heat fluxes. Such biophysical effects of vegetation on climate have been addressed in a number of studies which have investigated the effects of deforestation (Charney, 1975; Dickinson and Henderson-Sellers, 1988; Lean and Rowntree, 1993; Dirmeyer and Shukla, 1994; Lean and Rowntree, 1997; Xue, 1997), the effects of anthropogenic land-cover change (Brovkin et al., 1999; Chase et al., 2000; Heck et al., 2001; Zhao et al., 2001), and the effects of changes in structural and physiological vegetation characteristics (Pollard and Thompson, 1995; Betts et al., 1997; Douville et al., 2000). At longer time scales of decades to centuries the vegetation and ecosystem dynamics affect climate through the biogeochemical cycles that control the land surface-atmosphere exchange of $\mathrm{CO}_2$ and other radiatively important trace gases (Shaver et al., 1992). At these longer time scales, however, the climate also influences the vegetation and the climate-vegetation feedbacks determine the geographical distribution of various plant functional types (PFTs) (Holdridge, 1947; Claussen, 1998). These changes in geographical distribution of PFTs affect the climate via biophysical processes.

The interactions between the terrestrial biosphere and climate in atmospheric models are represented by soil-vegetation-atmosphere-transfer (SVAT) schemes. Although SVAT schemes that include partially dynamic vegetation modules (e.g. Dickinson et al., 1998; Sellers et al., 1996) are emerging, most SVAT schemes that are currently operated within general circulation models (GCMs) do not take into account the dynamic aspects of vegetation that are necessary for modeling climate at time scales of decades to a century. In a broad sense, the consideration of vegetation as a dynamic component in GCMs implies that the primary biophysical, biogeochemical, and biogeographical processes, via which the terrestrial biosphere affects the atmosphere, should be modeled explicitly. Most current SVAT schemes used in GCMs already model the complex biophysical interactions between the land surface and the atmosphere by treating the energy and water balances of the vegetation canopy and soil layers in a detailed manner. However, the effect of atmospheric $\mathrm{CO}_2$ concentration on stomatal conductance, the biogeochemical processes that determine the land-atmosphere exchange of $\mathrm{CO}_2$, and dynamic changes in geographical distribution of PFTs, are currently not modeled in most GCMs. Simulation of land-atmosphere exchange of $\mathrm{CO}_2$ fluxes require that processes of photosynthesis, respiration from vegetation and soil carbon components, and allocation of net carbon uptake to various vegetation components (foliage, stem, branches, and roots) be explicitly modeled. Work is at present underway to include these and other terrestrial ecosystem processes, which would make vegetation a dynamic component, in the next generation of the Canadian Centre for Climate Modelling and Analysis (CCCma) coupled general circulation model (CGCM). Simulation of land-atmosphere $\mathrm{CO}_2$ fluxes within the coupled climate model (together with an oceanic carbon cycle model) will allow atmospheric $\mathrm{CO}_2$ concentration to be modeled as a prognostic variable, rather than an externally prescribe quantity, in near future coupled climate-carbon simulations.

This paper describes the coupling and initial validation of photosynthesis and respiration sub-modules with the Canadian land surface scheme (CLASS) for intended use in the next generation of CCCma's coupled carbon general circulation model. The coupled land surface scheme and terrestrial ecosystem module (with its photosynthesis and respiration sub-modules) is tested by comparing simulated energy and carbon fluxes with observations at Ponca City, Oklahoma, AmeriFlux site. Section 2 describes the CLASS land surface scheme, the terrestrial ecosystem module and the manner in which they are coupled. The Ponca City, Oklahoma site from which data are used in this study is briefly described in Section 3. The comparisons between simulated energy and $\mathrm{CO}_2$ fluxes are performed in Section 4, and the results are summarized in Section 5.

## 2. The land surface and the terrestrial ecosystem module

The structure of the terrestrial ecosystem module is shown in Fig. 1. The model contains three live vegetation components (leaves, stem, and roots) and two dead carbon components (litter and soil carbon). Fig. 1 also shows the rate change equations for the carbon in the five model pools. The manner in which the land surface scheme and the terrestrial ecosystem module are coupled is shown in Fig. 2. Gross photosynthetic uptake (GPP) and canopy conductance are estimated by the photosynthesis sub-module (Section 2.2) which uses canopy temperature, aerodynamic conductance, soil moisture, and other variables simulated by the land surface scheme (Section 2.1). The photosynthesis sub-module operates at the same time step as the land surface scheme (30 min). Fast biophysical land surface processes, including photosynthesis and evapotranspiration, which affect the energy and water balance are thus modeled at a small time step. Canopy conductance estimated by the photosynthesis sub-module is passed back to the land surface scheme where it is used in its energy and water balance calculations. Canopy and soil temperatures, and soil moisture, simulated by the land surface scheme, are used to estimate maintenance respiration from the three vegetation components, and heterotrophic respiration from litter and soil carbon pools (Section 2.3). The net photosynthetic uptake, after the respiratory losses have been taken into account, is allocated between leaves, stem, and roots. The model also estimates litter and stem fall, and root mortality. Respiration from the vegetation components and litter and soil carbon pools, allocation, and mortality losses, i.e. the intermediate time-scale biogeochemical processes, are modeled at a daily time step (see Fig. 2). Allocation to, and mortality losses from, the three vegetation components make their biomasses dynamic in time. The allocation and litter fall sub-modules of the terrestrial ecosystem module were, however, not activated in this study since estimates of leaf, stem, and root biomasses and soil organic matter (SOM) derived from observations at the Ponca City, Oklahoma site, were used and these are also not explained in the text. This allowed assessment of the performance of the photosynthesis, and autotrophic and heterotrophic respiration sub-modules of the model, without incurring errors associated with incorrectly simulated biomass, leaf area index (LAI), and SOM.

*[Figure 1]* The structure of the terrestrial ecosystem module and the rate change equations for the carbon in five model pools: leaves (L), stem (S), root (R), litter or debris (D), and soil organic matter or humus (H). A = photosynthesis, GPP; A_S = carbon allocated to stem from leaves; A_R = carbon allocated to roots from leaves; R_g = Growth respiration for leaves, and similarly for stem (S) and roots (R); R_m = Maintenance respiration for leaves and similarly for stem (S) and roots (R); R_hD = Heterotrophic respiration from the litter or debris pool; R_hH = Heterotrophic respiration from the soil carbon (humus) pool; C_DH = carbon transferred from the litter to the soil carbon pool.

*[Figure 2]* The manner in which the land surface scheme and the terrestrial ecosystem module are coupled to each other. The sub-modules of the terrestrial ecosystem model are shown with a thick and dark outline.

### 2.1. The land surface scheme

The version 2.7 of CLASS used here, and expected to be used in the first generation coupled climate-carbon model, is described in detail by Verseghy (1991) and Verseghy et al. (1993). The scheme comprises three soil layers (with depths of 0.1, 0.25, and $3.75\,\mathrm{m}$), a snow layer where applicable, a single vegetative canopy layer (which intercepts both rain and snow), prognostic soil temperatures, prognostic liquid and frozen soil moisture contents, and soil surface properties (e.g. surface roughness heights and surface albedo) which are functions of soil moisture conditions and the soil and vegetation types. The radiation sub-model calculates the visible, near infrared (NIR), and longwave radiation absorbed by the canopy. The absorption of visible and NIR radiation is based on vegetation-dependent visible and NIR albedos and transmissivities, while net longwave radiation absorbed by the canopy is based on sky-view factor, which describes the degree of the canopy closure. The canopy conductance $(g_c = 1/r_c)$ parameterization used in CLASS is similar to that of Jarvis (1976). The canopy resistance $(r_c)$ is expressed as a function of minimum stomatal resistance $(r_{\min})$ and a series of environmental dependences whose effects are assumed to be multiplicative.

$$
r_c = r_{\min} f_1(S) f_2(\Delta e) f_3(w) f_4(T_a) \tag{1}
$$

where $f_1, f_2, f_3$, and $f_4$ are dependences on incoming solar radiation $S$ ($\mathrm{W}\,\mathrm{m}^{-2}$), vapour pressure deficit $\Delta e$ (mbar), soil matric potential $w$ (m), and air temperature $T_a$ ($^{\circ}\mathrm{C}$), respectively, and are given by

$$
\begin{aligned}
f_1(S) &= \max(1.0, (500.0 / S) - 1.5) \\
f_2(\Delta e) &= \max(1.0, \Delta e / 5.0) \\
f_3(w) &= \max(1, w / 40.0) \\
f_4(T_a) &= \begin{cases}
1.0, & 40^{\circ}\mathrm{C} > T_a > 0^{\circ}\mathrm{C} \\
5000.0 / r_{\min}, & T_a \ge 40^{\circ}\mathrm{C} \text{ or } T_a \le 0^{\circ}\mathrm{C}
\end{cases}
\end{aligned} \tag{2}
$$

The parameters in Eq. (2) are assumed to be generic and used in the application of the CLASS land surface scheme in the GCM. In its present form, Eqs. (1) and (2) do not explicitly model the effect of atmospheric $\mathrm{CO}_2$ concentration on stomatal resistance. The canopy and ground temperatures are calculated by iterative solution of their respective energy balance equations. Surface runoff in the scheme is generated when the amount of ponded water exceeds a specified limit and ponds form when precipitation intensity exceeds infiltration capacity of soil. Drainage from the bottom-most soil layer is assumed equal to the hydraulic conductivity of soil, which itself is a function of soil moisture.

### 2.2. The photosynthesis sub-module

There are two primary reasons for modeling photosynthesis within the framework of climate models. First, in addition to environmental variables mentioned in Eq. (1), photosynthesis allows to model the effect of atmospheric $\mathrm{CO}_2$ concentration on stomatal conductance. This is essential to simulate the physiological effects of increasing $\mathrm{CO}_2$ amounts on stomatal conductance in a transient climate simulation. Second, in order to simulate land-atmosphere $\mathrm{CO}_2$ exchange rates and to model vegetation as a dynamic component, it is necessary to estimate the amount of $\mathrm{CO}_2$ uptake by vegetation.

The photosynthesis sub-module used here is based on the biochemical approach (Farquhar et al., 1980; Collatz et al., 1991, 1992) as implemented in the SiB2 (Sellers et al., 1996) and MOSES (Cox et al., 1999) land surface schemes with some minor differences. The photosynthesis rate, $A$, is co-limited by assimilation rates based on Rubisco $(J_c)$, light $(J_e)$, and transport capacity $(J_s)$. The model equations are summarized in Appendix A and show the functional dependence of the Rubisco $(J_c)$, light $(J_e)$, and transport capacity $(J_s)$ limited leaf assimilation rates on various biophysical parameters and environmental conditions, including the partial pressure of $\mathrm{CO}_2$ in the leaf interior $(c_i)$.

$$
A = f(\text{environmental conditions}, c_i) \tag{3}
$$

The code is designed in such a way that the CLASS land surface scheme may use its original Jarvis type formulation to find canopy conductance, or it may use conductance estimated by the photosynthesis sub-module. In addition, the photosynthesis sub-module is designed to use both the big-leaf and the two-leaf (sunlit and shaded) approaches, either of which may be chosen for a given simulation. In the big-leaf model the scaling up from leaf to canopy is based on the assumption that the profile of leaf nitrogen content through the depth of the canopy follows the time-mean profile of radiation (Sellers et al., 1992). Since maximum photosynthetic rate, Rubisco and electron transport rates, and respiration rate have been shown to co-vary and increase more or less linearly with leaf nitrogen content (Ingestad and Lund, 1986; Field and Mooney, 1986), knowledge of leaf nitrogen content profile can be used to scale leaf photosynthesis to the canopy level. The central assumption of this hypothesis is that the photosynthetic properties of leaves, including leaf nitrogen content, acclimate fully to the prevailing light conditions within a canopy so that the photosynthetic capacity is proportional to the time-integrated absorbed radiation, normalized with respect to photosynthetic capacity and absorbed radiation, respectively, at some reference point, typically at the top of the canopy (Kull and Jarvis, 1995). The vertical profile of radiation itself along the depth of the canopy is described by the Beer's law,

$$
I_L = I_0 \mathrm{e}^{-k_n L} \tag{4}
$$

where $I_0$ and $I_L$ are the values of photosynthetically active radiation (PAR) at the top of the canopy and under a leaf area index $L$, respectively, and $k_n$ is a vegetation-dependent nitrogen extinction coefficient. Total photosynthetically active radiation $I_T$, reaching the entire canopy can be obtained by integrating Eq. (4) over the depth of the canopy,

$$
I_T = I_0 \int_0^{L_T} \mathrm{e}^{-k_n L} \mathrm{d}L = I_0 \frac{1 - \mathrm{e}^{-k_n L_T}}{k_n} = I_0 f_{\mathrm{scale}} \tag{5}
$$

where $L_T$ is the total leaf area index (LAI). Eq. (5) implies that PAR at the top of the canopy can be scaled by $f_{\mathrm{scale}}$ to obtain the canopy-averaged value. Photosynthesis estimated at the top of the canopy, $A_0$, is similarly scaled to obtain the total canopy value, $A_{\mathrm{canopy}}$.

$$
A_{\mathrm{canopy}} = A_0 \frac{1 - \mathrm{e}^{-k_n L_T}}{k_n} = A_0 f_{\mathrm{scale}} \tag{6}
$$

In the two-leaf model the canopy is divided into the sunlit and shaded fractions for which the photosynthesis rates are estimated separately. The two-leaf model questions the assumption that leaf nitrogen is approximately distributed in the canopy in proportion to the time-averaged profile of absorbed radiation. de Pury and Farquhar (1997) argue that the big-leaf model ignores the instantaneous distribution of radiation due to penetration of sunflecks and the effect of leaf angles on radiation absorbed by the canopy. Wang and Leuning (1998) argue that modeling the canopy as a single big leaf ignores the non-linear response of leaf photosynthesis to light and so the use of mean absorbed radiation will significantly over-estimate canopy photosynthesis.

The penetration of sunflecks in the two-leaf model is assumed to decay exponentially and described by the light extinction parameter $k_b$, which is a function of sun's zenith angle, and leaf angle distribution. Following de Pury and Farquhar (1997), the sunlit and shaded fractions of the canopy are given by $\mathrm{e}^{-k_b L_T}$ and $(1 - \mathrm{e}^{-k_b L_T})$, respectively. The photosynthesis rate for the sunlit fraction of the canopy, $A_{\mathrm{sun}}$, is obtained by integrating the photosynthesis rate at the top of the canopy, $A_{0,\mathrm{sun}}$, over the depth of the canopy but only for sunlit fraction.

$$
A_{\mathrm{sun}} = A_{0,\mathrm{sun}} \int_0^{L_T} \mathrm{e}^{-k_n L} \mathrm{e}^{-k_b L} \mathrm{d}L = A_{0,\mathrm{sun}} \frac{1 - \mathrm{e}^{-(k_n + k_b)L_T}}{k_n + k_b} = A_{0,\mathrm{sun}} f_{\mathrm{sun}} \tag{7}
$$

Similarly, the photosynthesis rate for the shaded fraction of the canopy, $A_{\mathrm{sha}}$, is obtained as,

$$
A_{\mathrm{sha}} = A_{0,\mathrm{sha}} \int_0^{L_T} \mathrm{e}^{-k_n L} (1 - \mathrm{e}^{-k_b L}) \mathrm{d}L = A_{0,\mathrm{sha}} \left( \frac{1 - \mathrm{e}^{-k_n L_T}}{k_n} - \frac{1 - \mathrm{e}^{-(k_n + k_b)L_T}}{k_n + k_b} \right) = A_{0,\mathrm{sha}} f_{\mathrm{sha}} \tag{8}
$$

Note that $f_{\mathrm{scale}}$ (as used in the big-leaf model in Eq. (6)), is equal to the sum of $f_{\mathrm{sun}}$ and $f_{\mathrm{sha}}$. Since the Rubisco- and light-limited assimilation rates are different for the sunlit and shaded fractions of the canopy they co-limit the photosynthesis rates $A_{0,\mathrm{sun}}$ and $A_{0,\mathrm{sha}}$ differently. The canopy photosynthesis rate, $A_{\mathrm{canopy}}$, is obtained by adding $A_{\mathrm{sun}}$ and $A_{\mathrm{sha}}$. Following Sellers (1985), the light extinction parameter, $k_b$, is obtained as,

$$
\begin{aligned}
k_b &= \frac{G(\mu)}{\mu} (1 - \sigma^2) \\
G(\mu) &= \phi_1 + \phi_2 \mu \\
\phi_1 &= 0.5 - 0.633\chi - 0.33\chi^2 \\
\phi_2 &= 0.877(1 - 2\phi_1)
\end{aligned} \tag{9}
$$

where $\mu$ is the cosine of solar zenith angle, $\sigma$ the leaf scattering coefficient, and $\chi$ an empirical vegetation-dependent parameter describing leaf angle distribution which varies between $-0.4$ and 0.6. Since $k_b$ is a function of sun's zenith angle it changes during the day with solar elevation and so do the fractions of the sunlit and shaded portions within the canopy. The scaling from leaf to the canopy level photosynthesis is thus performed using Eq. (6) for the big-leaf model, and using Eqs. (7) and (8) for the two-leaf model in a manner similar to Ronda et al. (2001).

#### 2.2.1. Effect of soil moisture stress on photosynthesis

Most vegetative canopies suffer from soil moisture stress during periods of low soil moisture. Different approaches have been used to account for soil moisture stress on stomatal closure. Some models decrease the photosynthetic rate (Cox, 2001) which then decreases the stomatal conductance (via equations similar to (13) or (14)), while others decrease estimated stomatal conductance directly (Knorr, 2000; Warnant et al., 1994; Foley et al., 1996). In the model presented here, the potential (unstressed) photosynthetic rate is reduced via a non-linear soil moisture function.

$$
A_{\mathrm{canopy,stressed}} = A_{\mathrm{canopy}} G(\theta) \tag{10}
$$

There is some evidence that reduction in photosynthetic rate does not scale linearly with soil moisture stress (Feddes et al., 1978). Following Ronda et al. (2001), the soil moisture stress term $G(\theta)$ is given by,

$$
\begin{aligned}
G(\theta) &= 2\beta(\theta) - \beta^2(\theta) \\
\beta(\theta) &= \max\left[0, \min\left(1, \frac{\theta - \theta_{\mathrm{wilt}}}{\theta_{\mathrm{field}} - \theta_{\mathrm{wilt}}}\right)\right]
\end{aligned} \tag{11}
$$

where $\theta$, $\theta_{\mathrm{wilt}}$, and $\theta_{\mathrm{field}}$ are the soil moisture content, wilting point soil moisture, and field capacity, respectively, and $\beta$ the degree of soil saturation. Since $\theta_{\mathrm{wilt}}$ and $\theta_{\mathrm{field}}$ values may be different for each soil layer, $G(\theta)$ is calculated separately for each soil layer and then weighted according to the fraction of roots present in each layer. The physiological basis for Eqs. (10) and (11) is to model drought stress effect by reducing the photosynthetic rate.

#### 2.2.2. Photosynthesis-stomatal conductance coupling

Net canopy photosynthesis rate, $A_n$ ($\mu\mathrm{mol}\,\mathrm{CO}_2\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}$), is used to estimate canopy conductance. $A_n$ is obtained by subtracting canopy leaf maintenance respiration from the canopy photosynthesis rate.

$$
A_n = A_{\mathrm{canopy,stressed}} - R_{\mathrm{mL}} \tag{12}
$$

Estimation of leaf maintenance respiration is discussed in Section 2.3. The photosynthesis sub-module is designed to use both Ball et al. (1987) (BWB) and Leuning (1995) formulations, and either formulation may be used. The primary difference between Ball et al. (1987) and Leuning (1995) formulations is the manner in which they use humidity information. Ball et al. (1987) use relative humidity in their formulation, while Leuning (1995) uses vapor pressure deficit. The Ball et al. (1987) stomatal conductance model is given by,

$$
g_c = m \frac{A_n h_s p}{c_s} + b L_T \tag{13}
$$

where $g_c$ is the canopy conductance ($\mu\mathrm{mol}\,\mathrm{CO}_2\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}$), $h_s$ the relative humidity, $p$ the pressure (Pa), $c_s$ the partial pressure of $\mathrm{CO}_2$ at the leaf surface (Pa), and $m$ and $b$ are vegetation dependent parameters. The Leuning (1995) formulation is given by,

$$
g_c = m \frac{A_n p}{(c_s - \Gamma)} \frac{1}{(1 + D/D_0)} + b L_T \tag{14}
$$

where $\Gamma$ is the $\mathrm{CO}_2$ compensation point in pascals (the $\mathrm{CO}_2$ partial pressure at which photosynthetic uptake is equal to the leaf respiratory losses), $D$ the vapor pressure deficit (Pa), and $D_0$ is a vegetation dependent parameter (Pa). The comparison of Eqs. (13) and (14) shows that in the Leuning (1995) formulation the term $c_s$ is replaced by $(c_s - \Gamma)$, and relative humidity, $h_s$, is replaced by a vapor pressure deficit term $(1 / (1 + D/D_0))$. Leuning (1990) shows that using $(c_s - \Gamma)$ instead of $c_s$ improves the behavior of the model at low values of $c_s$. Ball et al.'s (1987) formulation based on relative humidity has been used by Collatz et al. (1991, 1992) and by Sellers et al. (1996) in SiB2 land surface scheme. Cox et al. (1999) relate stomatal conductance to vapor pressure deficit in the MOSES land surface scheme. Aphalo and Jarvis (1993) argue that Ball et al.'s model provides no evidence for a hypothetical response of stomata to relative humidity. They cite experiments which indicate that stomata respond to vapor pressure deficit and not relative humidity. Betts et al. (1999) found that vegetative resistance, inferred from Northern Study Area old black spruce BOREAS site, was more tightly correlated with relative humidity than vapor pressure deficit. Whether stomatal conductance correlates well with relative humidity or vapor pressure deficit is still debatable and there is no compelling evidence for either approach, although Leuning (1995) argued that use of vapor pressure deficit is preferable.

The $\mathrm{CO}_2$ partial pressure at the leaf surface (Pa), $c_s$, used in Eqs. (13) and (14) is estimated using,

$$
\frac{c_a - c_s}{p} \frac{g_b}{1.4} = A_n \tag{15}
$$

where $c_a$ is the atmospheric $\mathrm{CO}_2$ partial pressure (Pa), and $g_b$ is the aerodynamic conductance obtained from the land surface scheme. The intercellular $\mathrm{CO}_2$ concentration, $c_i$, is estimated using,

$$
\frac{c_s - c_i}{p} \frac{g_c}{1.6} = A_n \tag{16}
$$

and $g_c$ is obtained from Eqs. (13) or (14). The factors 1.4 and 1.6, in Eqs. (15) and (16), account for different diffusivities of water and $\mathrm{CO}_2$ in the leaf boundary layer and stomatal pores, respectively. The temperature dependence of photosynthesis (see Appendix A) implies that photosynthesis, stomatal conductance, and energy balance are all linked and both canopy temperature and $c_i$ be determined iteratively. The intercellular $\mathrm{CO}_2$ concentration, $c_i$ estimated from Eq. (16) is used to find the value of canopy photosynthesis rate, $A_{\mathrm{canopy}}$ (Eq. (3)) and the cycle is repeated to estimate $c_i$. Four iterations are performed every time step in the model presented here and this was found sufficient for $c_i$ to converge.

### 2.3. The respiration sub-module

The respiration sub-module calculates autotrophic respiration, $R_a$, from live vegetation components, and heterotrophic respiration, $R_h$, from dead carbon pools.

#### 2.3.1. Autotrophic respiration

Autotrophic respiration, $R_a$, is estimated as the sum of maintenance respiration, $R_m$, from the three live vegetation components (leaves, stem, and root) and growth respiration, $R_g$.

$$
\begin{aligned}
R_a &= R_m + R_g \\
R_m &= R_{\mathrm{mL}} + R_{\mathrm{mS}} + R_{\mathrm{mR}}
\end{aligned} \tag{17}
$$

where $R_{\mathrm{mL}}$, $R_{\mathrm{mS}}$, and $R_{\mathrm{mR}}$ are maintenance respiration from the leaves, stem, and root, respectively. Growth respiration, which is used to synthesize new plant material, is highly correlated with the total growth of plants. In a manner similar to most ecosystem models (e.g. Knorr, 2000; Foley et al., 1996; Ludeke et al., 1994; Woodward et al., 1995), growth respiration is estimated as a constant fraction of gross canopy photosynthetic rate minus maintenance respiration.

$$
R_g = \begin{cases}
\alpha_g (A_{\mathrm{canopy,stressed}} - R_m), & \text{when } (A_{\mathrm{canopy,stressed}} - R_m) \text{ is positive} \\
0, & \text{otherwise}
\end{cases} \tag{18}
$$

Net primary productivity (NPP) is estimated as,

$$
\mathrm{NPP} = A_{\mathrm{canopy}} - R_m - R_g \tag{19}
$$

Maintenance respiration is used to keep existing tissue alive and functioning, and is a function of environmental stress on vegetation. If the stress levels are high, e.g. due to high temperature, maintenance respiration levels will increase. Maintenance respiration rates from leaves, stem, and roots have been observed to correlate better with nitrogen than with their carbon content (Ryan, 1991; Reich et al., 1998). Simulating plant nitrogen explicitly, however, requires modelling of the nitrogen-cycle which also involves the soils. Instead, the fact that maximum catalytic capacity of Rubisco $V_{\max}$ is closely related to leaf nitrogen content is used to estimate leaf respiration. Following Collatz et al. (1991, 1992), leaf maintenance respiration, $R_{\mathrm{mL}}$, is estimated as

$$
R_{\mathrm{mL}} = \begin{cases}
0.015 V_{\max}, & \text{for } C_3 \text{ plants} \\
0.025 V_{\max}, & \text{for } C_4 \text{ plants}
\end{cases} \tag{20}
$$

Following Ryan (1991), and in a manner similar to the BIOME-BGC model (Keyser et al., 2000), maintenance respiration for stem $(R_{\mathrm{mS}})$ and root $(R_{\mathrm{mR}})$ are estimated on the basis of their nitrogen content. The C:N ratio of stem and root (prescribed as a function of vegetation type) and amount of carbon ($\mathrm{kgC}\,\mathrm{m}^{-2}$) present in these components are used to estimate amount of nitrogen ($\mathrm{kgN}\,\mathrm{m}^{-2}$). Respiration is estimated on the basis of a specified respiration rate $\beta_N$ ($0.218\,\mathrm{kgC}\,\mathrm{kgN}^{-1}\,\mathrm{day}^{-1}$) at $20^{\circ}\mathrm{C}$ and a $Q_{10}$ temperature function.

$$
R_{\mathrm{mS}} = \beta_N \frac{C_S}{S_S} f_{20}(Q_{10}) \tag{21}
$$

$$
R_{\mathrm{mR}} = \beta_N \frac{C_R}{S_R} f_{20}(Q_{10}) \tag{22}
$$

where $C_S$ and $C_R$ are the amounts of carbon in stem and root components, and $S_S$ and $S_R$ their respective C:N ratios. $f_{20}(Q_{10})$ is a temperature dependent function given by $Q_{10}^{(T - 20)/10}$, where $T$ ($^{\circ}\mathrm{C}$) is the stem $(T_S)$ or root $(T_R)$ temperature. The stem temperature is assumed to be the same as the canopy temperature simulated by the land surface scheme. The root temperature $T_R$ is estimated on the basis of temperature of the three soil layers and the fraction of roots present in each soil layer. Maximum rooting depth is prescribed as an input parameter for the land surface scheme. The fraction of roots in each layer varies in time and is modeled as a function of vegetation type (Verseghy et al., 1993). The $Q_{10}$ value for maintenance respiration is not assumed to be a constant but modeled as a function of temperature following Tjoelker et al. (2001) as,

$$
Q_{10} = 3.22 - 0.046 T \tag{23}
$$

where $T$ ($^{\circ}\mathrm{C}$) is the stem $(T_S)$ or the root $(T_R)$ temperature.

Since $R_{\mathrm{mL}}$ is used to estimate net leaf photosynthetic rate (Eq. (12)) it is estimated within the photosynthesis sub-module at the time step of $30\,\mathrm{min}$. Maintenance respiration from stem and root are, however, modeled at a daily time step using daily-averaged canopy and soil temperatures which are passed to the autotrophic respiration sub-module from the land surface scheme (see Fig. 2).

#### 2.3.2. Heterotrophic respiration

Respiration from litter and soil carbon pools plays an important role in the terrestrial ecosystem carbon budget and represents a major carbon efflux from the ecosystems (Schlesinger and Andrews, 2000; Schlesinger et al., 2000). Heterotrophic respiration from both pools is primarily regulated by soil temperature and soil moisture. For given soil moisture conditions, and provided there is enough decomposable material, an increase in soil temperature almost invariably leads to an increase in microbial respiration rates due to increased activity of soil micro-organisms, although optimal temperatures for microbial activity are believed to reached between 35 and $45^{\circ}\mathrm{C}$ (Paul, 2001). Temperature dependency of microbial soil respiration rates has been expressed by a number of formulations ranging from the simple exponential $(Q_{10})$ formulations to Arrhenius type formulations (e.g. see review by Lloyd and Taylor, 1994). A $Q_{10}$ formulation, with a temperature-dependent $Q_{10}$ value, is used in the model presented here.

The dependency of microbial soil respiration rates on soil moisture is, however, not straightforward. Low soil moisture values (and the resulting high absolute values of soil matric potential) are known to constrain microbial activity and resulting microbial soil respiration (Davidson et al., 2000; Orchard et al., 1992). On the other hand, when the soils are saturated, then the lack of availability of oxygen to microbes restricts microbial activity and respiration rates. Griffin (1981) suggests that the microbial activity is optimal at soil matric potential of $-0.05\,\mathrm{MPa}$ and decreases as the soil becomes water-logged near $0.00\,\mathrm{MPa}$ or too dry near $-1.5\,\mathrm{MPa}$. Soil respiration has been found to decrease at very high and very low soil moisture content at boreal sites (Schlentner and van Cleve, 1985; Savage et al., 1997), in temperate deciduous forests (Davidson et al., 1998), and in arctic tundra (Luken and Billings, 1985; Oberbauer et al., 1991). Davidson et al. (2000) and Orchard and Cook (1983) show that soil respiration rates are linearly correlated with the logarithm of soil matric potential. The effects of temperature and moisture are opposite to each other, (e.g. high temperatures are associated with low soil moisture values, and vice versa) and it can be problematic to separate their effects on microbial decomposition rates in the field (Kirschbaum, 1995). Davidson et al. (2000) review the formulae that have been used by various researchers to model the effect of soil moisture on microbial soil respiration rates. These formulae range from linear, logarithmic, quadratic, parabolic, and hyperbolic functions of soil moisture expressed as soil matric potential, gravimetric and volumetric soil moisture content, water holding capacity, water-filled pore space, precipitation indices, and depth to water table. Following Griffin (1981), Davidson et al. (2000) and Orchard and Cook (1983) the dependency of soil moisture on microbial respiration rates is modeled here via soil matric potential. Since surface litter is always exposed to air, litter respiration rates are not constrained by lack of oxygen when the soils are saturated. Warm and wet conditions lead to greater litter decomposition rates (Howard and Howard, 1979; Law et al., 2001). The effect of moisture on litter decomposition rate is modeled in a manner similar to that for soil carbon, with the difference that litter decomposition rates are not constrained by high moisture content.

After climate, the primary control on litter and soil organic matter decomposition rates is exerted by litter quality (Lavelle et al., 1993; Aerts, 1997) which is usually expressed in terms of C:N or lignin:N ratios. Decomposition rates tend to decrease with higher values of C:N (Aerts, 1997; Gholz et al., 2000). Higher lignin concentrations compared to nitrogen also lead to slower decomposition rates (Melillo et al., 1982). Since the nitrogen cycle is not simulated explicitly in the model, the effect of substrate quality on litter and soil organic matter respiration rates is modeled in terms of prescribed base respiration rates (see Eqs. (25) and (26)) which are function of vegetation types.

Heterotrophic respiration, $R_h$, is estimated as the sum of respiration from the litter $(C_D)$ and soil carbon $(C_H)$ pools (see Fig. 1),

$$
R_h = R_{\mathrm{hD}} + R_{\mathrm{hH}} \tag{24}
$$

Respiration from the litter $(R_{\mathrm{hD}})$ and soil carbon $(R_{\mathrm{hH}})$ pools is estimated using specified respiration rates at $15^{\circ}\mathrm{C}$, the amount of carbon in these pools, a temperature dependent $Q_{10}$ function (Eq. (28)), and a soil moisture dependent factor.

$$
R_{\mathrm{hD}} = \beta_D C_D f_{15}(Q_{10}) f_D(\psi) \tag{25}
$$

$$
R_{\mathrm{hH}} = \beta_H C_H f_{15}(Q_{10}) f_H(\psi) \tag{26}
$$

where $C_D$ and $C_H$ are the amounts of carbon in litter (debris) and soil carbon (humus) pools ($\mathrm{kgC}\,\mathrm{m}^{-2}$) and $\beta_D$ and $\beta_H$ are the specified vegetation-dependent respiration rates ($\mathrm{kgC}\,\mathrm{kgC}^{-1}\,\mathrm{day}^{-1}$) for the litter and soil carbon pools. $f_{15}(Q_{10})$ is a temperature dependent function given by $Q_{10}^{(T - 15)/10}$, where $T$ ($^{\circ}\mathrm{C}$) is the litter $(T_D)$ or soil carbon $(T_H)$ temperature. In the model, the litter pool represents combined litter from the mortality of leaf, stem, and root components. Litter temperature is therefore assumed to be a weighted average of soil temperature of the top layer and root temperature $(T_R)$:

$$
T_D = x T_{\mathrm{soil}} + (1 - x) T_R \tag{27}
$$

Since the globally-averaged profiles for soil organic carbon and root distribution are fairly similar (Fig. 4 of Jobbagy and Jackson, 2000), the temperature of the soil carbon pool, $T_H$, is assumed to be the same as that of root temperature. The $Q_{10}$ value used in Eqs. (25) and (26) is estimated as a function of temperature using the following expression obtained by Kirschbaum (1995),

$$
Q_{10} = \exp\left[2.04\left(1 - \frac{T}{T_{\mathrm{opt}}}\right)\right] \tag{28}
$$

where $T$ ($^{\circ}\mathrm{C}$) is the litter or soil carbon temperature and $T_{\mathrm{opt}}$ is equal to $36.9^{\circ}\mathrm{C}$. $f_H(\psi)$ represents the effect of soil moisture on microbial respiration rates from the soil carbon pool $(C_H)$ via soil matric potential $(\psi)$. Being a suction pressure soil matric potential is usually expressed as a negative value, but its absolute values are considered in the following text. Following Griffin (1981) optimum soil moisture conditions are assumed to occur when soil matric potential lies between 0.04 and $0.06\,\mathrm{MPa}$. Between 0.06 and $100\,\mathrm{MPa}$ the value of $f_H(\psi)$ is assumed to decrease linearly with the logarithm of matric potential, and when the soil matric potential is greater than $100\,\mathrm{MPa}$ then microbial respiration is assumed to cease (Davidson et al., 2000). Between $0.04\,\mathrm{MPa}$ and saturation matric potential $(\psi_{\mathrm{sat}})$ the value of $f_H(\psi)$ is also assumed to decrease linearly with the logarithm of matric potential, and at saturation matric potential microbial respiration rate is assumed to be half of that when the soil moisture is optimum. Fig. 3 shows $f_H(\psi)$ as a function of soil matric potential $(\psi)$.

$$
f_H(\psi) = \begin{cases}
1 - 0.5 \frac{\log(0.04) - \log\psi}{\log(0.04) - \log\psi_{\mathrm{sat}}}, & 0.04 > \psi \ge \psi_{\mathrm{sat}} \\
1, & 0.06 \ge \psi \ge 0.04 \\
1 - \frac{\log\psi - \log(0.06)}{\log(100) - \log(0.06)}, & 100.0 \ge \psi > 0.06 \\
0, & \psi > 100.0
\end{cases} \tag{29}
$$

Soil matric potential itself is expressed as a function of soil moisture following Clapp and Hornberger (1978),

$$
\psi(\theta) = \psi_{\mathrm{sat}} \left( \frac{\theta}{\theta_{\mathrm{sat}}} \right)^{-c} \tag{30}
$$

where $\psi_{\mathrm{sat}}$, $\theta_{\mathrm{sat}}$ (saturated soil moisture content), and $c$ are parameters related to the soil type. The soil moisture factor for litter decomposition $(f_D(\psi))$ is similar to that for soil carbon $(f_H(\psi))$ with the difference that soil moisture content of only top soil layer is used and litter decomposition rates are assumed not be constrained by high moisture content (and low absolute values of soil matric potential). The daily values of respiratory fluxes from the litter and soil organic matter pools are estimated on the basis of soil temperature and moisture for the three soil layers simulated by the land surface scheme and passed to the heterotrophic respiration sub-module (see Fig. 2).

Finally, net ecosystem exchange (NEE) is estimated as the difference between photosynthetic uptake and all the respiratory fluxes,

$$
\mathrm{NEE} = \mathrm{NPP} - R_h = A_{\mathrm{canopy,stressed}} - R_a - R_h \tag{31}
$$

## 3. The study site, the meteorological forcing and flux data

### 3.1. The Ponca City, Oklahoma, AmeriFlux site

Year-round measurements and analysis of land surface-atmosphere carbon exchange have been initiated recently for a variety of key terrestrial ecosystems around the world. The FLUXNET project (Baldocchi et al., 2001) serves as a mechanism for uniting several of these regional and continental networks (e.g. AmeriFlux, EuroFlux, AsiaFlux) into an integrated global network. These data are being used to understand the dynamics of ecosystem carbon, energy, and water balances, to quantify the stand-scale response of carbon, energy, and water fluxes to various environmental factors, and to validate a hierarchy of SVAT scheme and trace gas exchange models (Baldocchi et al., 2001). Ponca City, in north central Oklahoma ($36^{\circ}45^{\prime}\mathrm{N}$; $97^{\circ}05^{\prime}\mathrm{W}$) is one of the AmeriFlux sites at which fluxes of $\mathrm{CO}_2$, water vapor, sensible heat, and momentum are being measured using the eddy covariance technique, along with supporting meteorological variables, soil moisture, leaf area index, and biomass (Verma, 1996; Suyker and Verma, 2002). The measurements at this site started in the fall of 1996. In this agricultural ecosystem, the primary vegetation is winter wheat whose maximum green leaf area index (LAI) at peak growth exceeds $5\,\mathrm{m}^2\,\mathrm{m}^{-2}$, and the soil is silty clay loam. The mean annual temperature (for years 1961–1990) at this site is $15.03^{\circ}\mathrm{C}$ with a range of $-3.7$ to $33.9^{\circ}\mathrm{C}$ and the annual average precipitation (1961–1990) is $834.7\,\mathrm{mm}$.

### 3.2. Meteorological forcing data

Half-hourly meteorological data from the Ponca City AmeriFlux site were collected in a study by S. Verma, PI and his colleagues (A. Suyker and G. Burba) of the University of Nebraska, Lincoln, Nebraska. Continuous filled half-hourly meteorological data for this site prepared by B.W. Shea, S. Verma, J. Berry, J. Privette, and N. Hanan are used. These researchers used linear interpolation technique together with average of meteorological variables from the previous/following day for the same/same and other years to fill missing values.

### 3.3. Energy and $\mathrm{CO}_2$ flux data

In Section 4, the simulated latent and sensible heat fluxes, net radiation, and NEE fluxes are compared with observations. The gap-filled observations of these quantities are available from the AmeriFlux web site for the year 1997. The gap-filling strategies for these energy and NEE fluxes are described in detail by Falge et al. (2001a,b), respectively. Following Falge et al.'s (2001a,b) recommendations, observational estimates that are gap-filled using the method based on look-up tables are used in this study for both energy and NEE fluxes.

### 3.4. Observed estimates of vegetation biomass and soil organic matter

The observed green LAI, together with an estimate of specific leaf area of wheat (SLA, the ratio of leaf area to leaf dry mass) of $30\,\mathrm{m}^2\,\mathrm{kg}^{-1}$ (Hocking and Meyer, 1991) was used to estimate the leaf carbon biomass ($\mathrm{kgC}\,\mathrm{m}^{-2}$) (assuming that dry mass is $50\%$ of the total leaf mass). This estimate of leaf biomass was subtracted from observed total aboveground green biomass to obtain an estimate of live stem biomass. Root biomass was estimated from observations at the Ponca City site. Rice (1999) reported root carbon biomass of $\sim 370\,\mathrm{g}\,\mathrm{kg}^{-1}$ of soil in the top $20\,\mathrm{cm}$ of soil during May of 1997. Assuming a soil density of $1.50\,\mathrm{g}\,\mathrm{cm}^{-3}$ for silt clay loam soil this yields a value of $\sim 110\,\mathrm{gC}\,\mathrm{m}^{-2}$ in the top $20\,\mathrm{cm}$ of soil. Maximum rooting depth was prescribed as $1.20\,\mathrm{m}$ (Kirkegaard et al., 2001). Using an estimate of fraction of roots in each soil layer simulated by the land surface scheme, the root carbon biomass value of $110\,\mathrm{gC}\,\mathrm{m}^{-2}$ in the top $20\,\mathrm{cm}$ was extrapolated to the entire rooting depth and an estimate of $300\,\mathrm{gC}\,\mathrm{m}^{-2}$ was obtained. In addition, in a manner similar to Wechsung et al. (1995), it was assumed that the live root biomass increased linearly (growth) from the date of sowing to its maximum value in 30 days, remained constant thereafter, and then decreased linearly (senescence) towards the end of the growing season. The daily values of the biomasses of three vegetation components (leaves, stem, and roots) are shown in Fig. 4.

The amount of soil organic matter was estimated by using percentages of soil carbon content of 1.2, 0.7, 0.6, and $0.4\%$ for soil layers 1–47, 47–78, 78–115, and 115–150 cm, respectively, reported at the AmeriFlux web site. In addition, for soil layers 150–200 and 200–300 cm soil carbon contents of 0.2 and $0.1\%$ respectively, were assumed. Using this soil carbon content information, the total soil carbon amount was estimated to be approximately $20\,\mathrm{kgC}\,\mathrm{m}^{-2}$. During the growing season, agricultural ecosystems are typically characterized by very low litter amounts and a constant value of litter pool of $0.1\,\mathrm{kgC}\,\mathrm{m}^{-2}$ was therefore assumed.

## 4. Model simulations of energy and $\mathrm{CO}_2$ fluxes

### 4.1. Initial conditions and model parameters

The coupled land surface-terrestrial ecosystem model was run for the year 1997 but only results from the growing season are reported here. Initial conditions were prescribed on the basis of data available from the AmeriFlux web site. Observed LAI data from the Ponca City site were used to drive the land surface scheme and the photosynthesis sub-module, and observed biomass and soil organic matter data were used to estimate autotrophic and heterotrophic respiration. The values of model parameters for the land surface scheme, and the photosynthesis and respiration sub-modules are summarized in Table 1 together with published references or web sites from which the parameter values were obtained.

**Table 1** Values of model parameters used in the land surface scheme and sub-modules of the terrestrial ecosystem model

| Symbol | Parameter description | Value used in the current study | Reference |
|:-------|:----------------------|:--------------------------------|:----------|
| **Land surface scheme** ||||
| $\alpha_{\mathrm{VIS}}$ | Canopy albedo, visible | 0.06 | Verseghy et al. (1993) |
| $\alpha_{\mathrm{NIR}}$ | Canopy albedo, near-infra red | 0.25 | Verseghy et al. (1993) |
| $d$ | Maximum rooting depth | 1.2 m | Kirkegaard et al. (2001) |
| $z_0$ | Roughness length | 0.08 m | |
| $C_{\max}$ | Maximum total canopy mass | $2.5\,\mathrm{kg}\,\mathrm{m}^{-2}$ | AmeriFlux web site |
| | Percent sand | 4.5, 2.5, and 5% in three model layers, respectively | AmeriFlux web site |
| | Percent clay | 28, 35, and 40% in three model layers, respectively | AmeriFlux web site |
| | Percent organic matter | 1.2, 1.2, and 0.5% in three model layers, respectively | AmeriFlux web site |
| **Photosynthesis sub-module** ||||
| $V_{\max}$ | Maximum catalytic capacity of Rubisco | $93\,\mu\mathrm{mol}\,\mathrm{CO}_2\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}$ | S. Verma and J. Berry |
| $k_n$ | Nitrogen extinction coefficient | 0.43 | Dreccer et al. (2000) |
| $\chi$ | Leaf angle parameter | $-0.30$ | |
| $\sigma$ | Leaf scattering coefficient | 0.15 | Cox (2001) |
| $\alpha$ | Quantum efficiency | 0.08 | Cox (2001) |
| $m$ | Stomatal conductance formulation parameter | 11.0 | Mo and Liu (2001) |
| $b$ | Stomatal conductance formulation parameter | 0.01 | Mo and Liu (2001) |
| $D_0$ | Stomatal conductance parameter in Leuning formulation | 1500 Pa | Mo and Liu (2001) |
| $T_{\mathrm{low}}$ | Upper temperature for limiting photosynthesis | $-3^{\circ}\mathrm{C}$ | Ito and Oikawa (2000) |
| $T_{\mathrm{up}}$ | Lower temperature for limiting photosynthesis | $42^{\circ}\mathrm{C}$ | Ito and Oikawa (2000) |
| **Autotrophic respiration sub-module** ||||
| $\alpha_g$ | Growth respiration parameter | 0.35 | Knorr (2000) |
| $\beta_N$ | Base respiration rate based on N content | $0.218\,\mathrm{kgC}\,\mathrm{kgN}^{-1}\,\mathrm{day}^{-1}$ | Keyser et al. (2000) |
| $S_S$ | C:N ratio of stem | 50 | |
| $S_R$ | C:N ratio of root | 50 | |
| $x$ | Parameter used to find weighted average litter pool temperature | 0.5 | |
| **Heterotrophic respiration sub-module** ||||
| $\beta_D$ | Base respiration rate for litter pool | $0.050\,\mathrm{kgC}\,\mathrm{kgC}^{-1}\,\mathrm{yr}^{-1}$ | Ito and Oikawa (2000) |
| $\beta_H$ | Base respiration rate for SOM pool | $0.037\,\mathrm{kgC}\,\mathrm{kgC}^{-1}\,\mathrm{yr}^{-1}$ | Ito and Oikawa (2000) |

*[Figure 4]* Daily values of observed above-ground total green biomass ($\mathrm{gC}\,\mathrm{m}^{-2}$) and LAI ($\mathrm{m}^2\,\mathrm{m}^{-2}$) and estimated observational-based values of foliage, stem, and root biomasses, over the growing season, at the Ponca City, AmeriFlux site.

### 4.2. Comparison of simulated energy fluxes

The observational estimates of latent and sensible heat fluxes, and net radiation, were compared with estimates obtained from the CLASS land surface scheme with its original Jarvis type canopy conductance formulation, and when conductance is estimated by the photosynthesis sub-module using both the big- and the two-leaf approaches. In the photosynthesis sub-module, canopy conductance is estimated using the Leuning (1995) type formulation since the observed half-hourly growing season estimates of latent heat fluxes, for the Ponca City site, correlated slightly better with the VPD term $(1 / (1 + D/D_0))$, used in Eq. (13) $(R^2 = 0.28)$ than with relative humidity used in Eq. (14) $(R^2 = 0.24)$. Comparison of the performances of the Ball et al. (1987) and Leuning (1995) stomatal conductance formulations is made in Section 4.2.1.

Daily observations of net radiation over the growing season are compared with simulated values in Fig. 5. The two model-simulated curves in Fig. 5 correspond to results from simulations using Jarvis type canopy conductance formulation and the Leuning (1995) formulation used with the big-leaf photosynthesis model. For reference, the seasonal evolution of observed LAI is also shown. The land surface scheme net radiation estimates from the two simulations are fairly similar, since net radiation is primarily determined by vegetation albedo. Averaged over the growing season the model-simulated net radiation estimates compare well with observations $(R^2 \ge 0.94)$, although the model estimates (coefficient of variation, $\mathrm{CV} = 0.63$) show slightly higher variability than the observations $(\mathrm{CV} = 0.45)$.

*[Figure 5]* Comparison of model and observed net radiation estimates ($\mathrm{W}\,\mathrm{m}^{-2}$) over the growing season. The land surface scheme (CLASS) estimates are from two simulations, one using the Jarvis type conductance formulation, and the other using Leuning (1995) formulation with the big-leaf photosynthesis model. Root mean square error (RMSE) and $R^2$ values are also shown.

Observed growing season estimates of daily latent heat (LE) fluxes are compared with those simulated using the Jarvis type canopy conductance formulation used in CLASS in Fig. 6a, and when conductance estimate is used from the photosynthesis sub-module (using both the big- and the two-leaf models) in Fig. 6b. Fig. 6a shows that the latent heat fluxes, at the Ponca City site, are significantly underestimated by the current Jarvis type formulation used in CLASS land surface scheme. Latent heat fluxes based on canopy conductance estimated by the photosynthesis sub-module compare fairly well the observational estimates. Both the big- and the two-leaf model capture the daily variation in latent heat fluxes reasonably well, and the two photosynthesis approaches yield similar average latent heat flux over the growing season and $R^2$ values of around 0.82. Averaged over the growing season, however, the two-leaf model yields slightly higher estimate of latent heat flux (see Fig. 6). Compared to the big- and the two-leaf photosynthesis models used with Leuning (1995) formulation, the Jarvis type formulation (Eq. (1)) yields higher values of canopy resistance $(r_c = 1/g_c)$ leading to lower latent heat fluxes. Averaged over the growing season the day-time (between 9 a.m. and 4 p.m.) canopy resistance obtained from the Jarvis type formulation $(362\,\mathrm{s}\,\mathrm{m}^{-1})$ is more than twice the canopy resistance obtained from the big- $(148\,\mathrm{s}\,\mathrm{m}^{-1})$ and the two-leaf $(146\,\mathrm{s}\,\mathrm{m}^{-1})$ models.

*[Figure 6]* Comparison of observations of growing season latent heat fluxes ($\mathrm{W}\,\mathrm{m}^{-2}$) with simulated values (a) obtained from the use of original Jarvis type stomatal conductance formulation in the CLASS land surface scheme, and (b) obtained from the use of stomatal conductance estimated by the big- and two-leaf approaches in the photosynthesis sub-module, which uses Leuning (1995) stomatal conductance-photosynthesis coupling. Root mean square error (RMSE) and $R^2$ values are also shown.

Lower latent heat fluxes simulated by the Jarvis type canopy conductance formulation imply that simulated sensible heat $(H)$ fluxes are higher compared to observations and this is shown in Fig. 7a. Sensible heat fluxes simulated by the land surface scheme when canopy conductance is estimated using the big- and the two-leaf photosynthesis models, however, compare reasonably well with observations in terms of average value over the growing season, lower RMSE, and higher correlation (Fig. 7b). Higher variability in simulated sensible heat fluxes in Fig. 7b, compared to observations, is caused by model's net radiation estimates. A comparison of Figs. 5 and 7b shows that simulated sensible heat fluxes are higher than observations on days when the land surface scheme overestimates net radiation, and simulated sensible heat fluxes are lower than observations on days when the land surface scheme underestimates net radiation. Since latent heat fluxes simulated by the big- and the two-leaf models compare well with observations $(R^2 \ge 0.82)$ (Fig. 6b) any differences in model and observed net radiation estimates are mainly reflected in sensible heat fluxes. Averaged over the growing season the sensible heat fluxes compare relatively well with observations when canopy conductance estimate is used from the big- and the two-leaf models, while the use of Jarvis canopy conductance formulation yields poor sensible heat flux estimates which are about twice the observed estimate (Fig. 7). Table 2 shows, that the incorrect partitioning of net radiation into latent and sensible heat fluxes, when the Jarvis type conductance formulation is used, results in a Bowen ratio $(\gamma = H/LE)$ estimate (calculated using average fluxes over the growing season) which is too high compared to observations. Bowen ratios when canopy conductance is estimated via the photosynthesis sub-module, however, compare well with observations, with the two-leaf model's estimate being slightly better than the big-leaf model.

*[Figure 7]* Comparison of observational estimates of growing season sensible heat fluxes ($\mathrm{W}\,\mathrm{m}^{-2}$) with simulated values (a) obtained from the use of original Jarvis type stomatal conductance formulation in the CLASS land surface scheme, and (b) obtained from the use of stomatal conductance estimated by the big- and two-leaf approaches in the photosynthesis sub-module, which uses Leuning (1995) stomatal conductance-photosynthesis coupling. Root mean square error (RMSE) and $R^2$ values are also shown.

**Table 2** Comparison of observed Bowen ratio estimate, averaged over the growing season, with simulated values

| | Bowen ratio |
|:--|:------------|
| Observed | 0.22 |
| CLASS-Jarvis | 0.59 |
| CLASS-single leaf | 0.24 |
| CLASS-two leaf | 0.22 |

#### 4.2.1. Comparison between stomatal conductance-photosynthesis formulations

The performance of the Ball et al. (1987) and Leuning (1995) stomatal conductance-photosynthesis formulations is assessed in Fig. 8, which compares the daily growing season estimates of latent heat flux simulated using both formulations, together with observations, for both the big- and the two-leaf photosynthesis approaches. The same values of parameters $m$ (11.0) and $b$ (0.01) are used in both models (in Eqs. (13) and (14)) and a value of parameter $D_0$ equal to $1500\,\mathrm{Pa}$ is used in the Leuning (1995) model for winter wheat, following Mo and Liu (2001). Fig. 8 shows that, averaged over the growing season, the latent heat fluxes estimated using the Ball et al. (1987) formulation are about $10\%$ lower than those estimated using Leuning (1995) formulation, for both the big- and the two-leaf photosynthesis approaches. In addition, averaged over the growing season, the difference between the simulated latent heat fluxes caused by the choice of the big- or the two-leaf photosynthesis approach (1.3 and $0.2\,\mathrm{W}\,\mathrm{m}^{-2}$ for Leuning and Ball et al.'s stomatal conductance formulations, respectively) is smaller than the difference caused by the choice of the stomatal conductance formulation $(\sim 8\,\mathrm{W}\,\mathrm{m}^{-2})$. The difference between the Ball et al. (1987) and the Leuning (1995) formulations is primarily caused by the use of relative humidity and vapor pressure deficit (VPD) term $(1 / (1 + D/D_0))$ in these formulations, respectively, both of which are related linearly to stomatal conductance.

*[Figure 8]* Comparison of daily estimates of latent heat fluxes ($\mathrm{W}\,\mathrm{m}^{-2}$) simulated using the Ball et al. (1987) and Leuning (1995) stomatal conductance formulations (for both the big- and two-leaf photosynthesis approaches) with observations.

Fig. 9 shows the daily averages (calculated from half-hourly data) of day-time (between 9 a.m. and 4 p.m.) relative humidity $(h_s)$ and the VPD term $(1 / (1 + D/D_0))$, over the growing season, for the Ponca City site. For the value of $D_0$ (1500 Pa) used in this study, the higher value of the VPD term (used in Leuning formulation) than relative humidity, leads to higher stomatal conductance and subsequently higher latent heat fluxes compared to the Ball et al. (1987) formulation. Fig. 9 also shows the range of values of the VPD term that may be obtained by varying the parameter $D_0$ within its approximate feasible parameter range between 500 and $2500\,\mathrm{Pa}$. Fig. 9 implies that, for a given net photosynthetic uptake $A_n$, a wide range of stomatal conductance values may be obtained by varying the parameter $D_0$. Both $D_0$ and $m$ are empirical parameters whose values are generally obtained by regression. In addition, $D_0$ and $m$ are negatively correlated, and the choice of one parameter affects the other (Leuning, 1995). Regardless of whether stomatal conductance correlates better with relative humidity or VPD, the presence of an additional parameter in the Leuning (1995) formulation helps to obtain a better fit to observed data.

*[Figure 9]* Comparison of daily averages (calculated from half-hourly data) of day-time (between 9 a.m. and 4 p.m.) relative humidity (shown as RH) and the VPD term $(1 / (1 + D/D_0))$, used in the Ball et al. (1987) and Leuning (1995) formulations, respectively, over the growing season, for the Ponca City site. The range of values of the VPD term that may be obtained by varying the parameter $D_0$ within its approximate feasible parameter range between 500 and 2500 Pa are also shown.

### 4.3. Comparison of simulated $\mathrm{CO}_2$ fluxes

In Section 4.2, reasonably good comparison between simulated latent heat fluxes and their observations, and an improvement in simulated sensible heat fluxes, is obtained when canopy conductance is estimated via the photosynthesis sub-module. Since latent heat fluxes and photosynthetic $\mathrm{CO}_2$ uptake are coupled to, and constrained by, each other, a complete test of coupled land surface and photosynthesis models also involves comparison of simulated gross photosynthetic $\mathrm{CO}_2$ uptake (GPP or $A_{\mathrm{canopy}}$) with observations. However, only estimates of net ecosystem exchange (NEE) fluxes are available for the Ponca City site. Modeled respiratory fluxes from the vegetation, litter, and soil organic matter pools were therefore subtracted from simulated GPP to estimate NEE fluxes. Growth and maintenance respiration from the three live vegetation components of the model were estimated as explained in Section 2.3.1 using observed estimates of vegetation biomass. Heterotrophic respiration from the litter and soil organic matter pools was estimated using the methodology explained in Section 2.3.2 using observed estimates of soil organic matter.

Simulated net photosynthesis $(A_n = A_{\mathrm{canopy,stressed}} - R_{\mathrm{mL}})$ rates from the big- and the two-leaf photosynthesis approaches are compared in Fig. 10a. Fig. 10a shows that, compared to the two-leaf model, the big-leaf model overestimates net photosynthetic $\mathrm{CO}_2$ uptake. On selected days, the net photosynthesis rates estimated by the big-leaf model are up to $30\%$ higher than those predicted by the two-leaf model. However, averaged over the growing season the big-leaf photosynthesis approach yields $A_n$ estimates that are about $5\%$ higher than the two-leaf approach. Using simulations for a single day, and compared to a multi-layer model, de Pury and Farquhar (1997) reported overestimation of canopy photosynthesis by 20 and $45\%$ for LAI of 4 and 6, respectively, by the big-leaf model.

*[Figure 10]* (a) Comparison of simulated net photosynthesis $(A_n)$ rates by the big- and the two-leaf photosynthesis models, and (b) Comparison of observations of NEE fluxes with simulated values using GPP estimates from both the big- and the two-leaf photosynthesis models. Root mean square error (RMSE) and $R^2$ values are also shown for simulated NEE fluxes.

In their simulation of net photosynthesis rates over winter wheat, Mo and Liu (2001) reported that averaged over the growing season, compared to the two-leaf, their big-leaf model overestimated net photosynthesis by $33\%$, while the difference in evapotranspiration estimates was of the order of $5\%$. Qualitatively, similar results have been obtained in this study in that the difference in net photosynthesis rates $(\sim 5\%)$ is bigger than the difference in latent heat fluxes $(\sim 1.5$ and $0.2\%$ for Leuning and Ball et al.'s stomatal conductance formulations, respectively). The overestimation of net photosynthesis rates of $5\%$ by the big-leaf model in this study is smaller than Mo and Liu's (2001) estimate of $33\%$. Amongst other possible reasons, this difference is likely due to Mo and Liu's (2001) use of a $V_{\max}$ value of $200\,\mu\mathrm{mol}\,\mathrm{CO}_2\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}$, while a $V_{\max}$ value of $93\,\mu\mathrm{mol}\,\mathrm{CO}_2\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}$ is used here for winter wheat. Although not shown here, a difference of $20\%$ was obtained in simulated net photosynthesis rates from the big- and the two-leaf photosynthesis approaches when a $V_{\max}$ value of $200\,\mu\mathrm{mol}\,\mathrm{CO}_2\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}$ was used in an experimental simulation based on Ponca City data. The $V_{\max}$ values for wheat at Ponca City site have been reported to range between 53 and $160\,\mu\mathrm{mol}\,\mathrm{CO}_2\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}$ with a mean $V_{\max}$ value of $93\,\mu\mathrm{mol}\,\mathrm{CO}_2\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}$.

Simulated NEE fluxes are shown in Fig. 10b for both the big- and the two-leaf photosynthesis approaches, and compare well with observations. Averaged over the growing season, the simulated NEE flux is about $18\%$ (big-leaf) and $4\%$ (two-leaf) higher than its observed estimate. The simulated NEE fluxes explain about $70\%$ (big-leaf) and $76\%$ (two-leaf) of the observed variability. Results from the two-leaf model are thus slightly better than from the big-leaf model. Reasonably good comparisons between simulated and observed NEE fluxes imply that confidence can be placed in simulated GPP estimates. Although desirable, in absence of observations of GPP and respiration fluxes it is not possible to validate the photosynthesis and respiration sub-modules separately, and only the combined performance of these sub-modules (in terms of simulated NEE fluxes) may be assessed.

### 4.4. Constraining model performance via comparisons with both energy and carbon fluxes

If the objective of this study were only to simulate energy fluxes with the use of canopy conductance estimated by the photosynthesis sub-module, and had comparisons for carbon fluxes not been performed, it is possible that the use of the big-leaf model with Ball et al. stomatal conductance formulation would had been considered adequate. Indeed with the use of $V_{\max}$ value of $130\,\mu\mathrm{mol}\,\mathrm{CO}_2\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}$, which is well within the range of values reported at the Ponca City site, and still smaller than the value of $200\,\mu\mathrm{mol}\,\mathrm{CO}_2\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}$ used by Mo and Liu (2001) for winter wheat, simulated latent heat fluxes with Ball's formulation may be made to match their observations (not shown). The use of a higher $V_{\max}$ value implies higher $\mathrm{CO}_2$ assimilation and, in absence of comparisons with observed carbon fluxes, this discrepancy would certainly go undetected.

In contrast, if model behavior were assessed only against observations of carbon fluxes with the big-leaf model, then a $V_{\max}$ value smaller than $93\,\mu\mathrm{mol}\,\mathrm{CO}_2\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}$ could have been used to obtain reasonable comparison with observed NEE fluxes, although this would imply a decrease in latent heat flux. Comparisons with both energy and carbon fluxes thus help to constrain model performance and obtain realistic model behavior. For the simulation results presented here, and for the parameter values reported for winter wheat at the Ponca City site and in published literature, it appears that the use of the two-leaf model with Leuning's stomatal conductance formulation gives results that compare well with observations for both the energy and carbon fluxes. Averaged over the growing season, the use of Ball's conductance formulation underestimates latent heat fluxes by about $10\%$ and the use of the GPP estimates from the big-leaf model results in an overestimation of NEE fluxes of around $18\%$.

## 5. Summary and conclusions

Work is at present underway to include terrestrial ecosystem processes, to model land-atmosphere exchange of $\mathrm{CO}_2$ fluxes, in the next generation of CCCma coupled climate model. This paper describes the coupling and validation of photosynthesis and respiration sub-modules with the CLASS land surface scheme for intended operational use in the climate model. CLASS has also been coupled to other ecosystem models of varying complexity (Wang et al., 2001; Arain et al., 2002). Validation exercises such as the one presented in this paper are planned to assess the performance of the coupled land surface scheme and terrestrial ecosystem module using data from various fluxnet sites. In this paper, I provide some initial evaluation of the performance of the coupled land surface scheme and terrestrial ecosystem models via comparisons with observed energy and carbon fluxes from the Ponca City, Ameriflux site.

The photosynthesis sub-module operates at the short time step of $30\,\mathrm{min}$ and provides estimates of canopy conductance to the land surface scheme. The photosynthesis sub-module is designed to use both the big-leaf and the two-leaf (sunlit/shaded) approaches, and stomatal conductance formulations based on relative humidity and vapor pressure deficit. Although when operated within the climate model only one of the photosynthesis approaches and stomatal conductance formulations is to be used, the flexibility to use both approaches provides a tool to test the sensitivity of the model results to these two different approaches of modeling photosynthesis and stomatal conductance. Other than photosynthesis, all terrestrial ecosystem sub-modules, which model the intermediate time-scale biogeochemical processes are operated at a daily time step. Daily-averaged values of canopy and soil temperature, soil moisture and other variables, which are required to model these biogeochemical processes, are passed from the land surface scheme to the respective sub-modules of the terrestrial ecosystem model.

The allocation and mortality sub-modules were not activated in this study since observed biomass, LAI, and soil organic matter (SOM) data were used from the Ponca City site. This allowed assessment of the performance of the autotrophic and heterotrophic respiration sub-modules of the model, without incurring errors associated with incorrectly simulated biomass, LAI, and SOM. In addition, the use of model-simulated SOM values to estimate heterotrophic respiration, required that the model be run with observed climate data for a long-time to allow the model soil carbon pools to come into equilibrium. Model validation exercises that would allow assessment of model simulated equilibrium values of the biomasses of the three vegetation components, and the values of litter and SOM pools, are the subject of near-future studies.

Comparisons with observed energy fluxes show that the use of canopy conductance estimated by the photosynthesis sub-module significantly improves simulated latent heat fluxes, compared to the use of the original Jarvis type conductance formulation in the land surface scheme. An improvement in simulated latent heat fluxes, also leads to an improvement in simulated sensible heat fluxes, although some differences remain which are primarily attributed to differences in simulated net radiation estimates. Incorrect partitioning of net radiation into latent and sensible heat fluxes, when the Jarvis type conductance formulation is used, leads to a Bowen ratio that is much higher than its observed value. The use of canopy conductance estimated by the big- and the two-leaf photosynthesis approaches yields Bowen ratio estimates that compare fairly well with observations. In regard to the effect of photosynthesis approach and stomatal conductance formulation, the model results suggest that, averaged over the growing season and for the winter wheat parameter values reported at the Ponca City site and in literature, the difference in simulated latent heat fluxes caused by the choice of the big- or two-leaf photosynthesis approach is much smaller than the difference caused by the choice of the stomatal conductance formulation.

A complete test of the coupled land surface and photosynthesis models involves validation with both observed energy and carbon fluxes. Reasonably good comparisons with either energy or carbon fluxes may be obtained by adjusting parameter values still within the range of uncertainty. Comparisons with both energy and carbon fluxes in this study helped to constrain model behavior and allowed to assess the performance of two of the both photosynthesis and stomatal conductance formulations. Model results also show that, averaged over the growing season, the percentage difference in simulated net photosynthesis rates is bigger than percentage difference in simulated latent heat fluxes when the big- and the two-leaf photosynthesis approaches are compared. Qualitatively similar results for winter wheat have been reported by Mo and Liu (2001).

Eddy-flux measurements of carbon and energy fluxes may contain both systematic and unsystematic errors (Wofsy et al., 1993; Goulden et al., 1996; Aubinet et al., 2000). Gap-filling for missing data leads to additional uncertainty (Falge et al., 2001a). Uncertainty in eddy-flux measurements is also introduced due to lack of energy balance closure and underestimation of night-time respiratory fluxes when the air becomes stably stratified (Massman and Lee, 2002). Anthoni et al. (1999) provide an estimate of systematic errors in daytime $\mathrm{CO}_2$ eddy-flux measurements of around $\pm 12\%$. While the results shown here suggest that the two-leaf model performs slightly better than the big-leaf model, given the uncertainty associated with the model parameters (in particular $V_{\max}$), and observations of carbon and energy fluxes, it is difficult to say so conclusively. In a review of various photosynthesis approaches Medlyn (2001) draws a similar conclusion.

## Acknowledgements

The efforts of the AmeriFlux network researchers in providing public access to flux and other data was a great help in this study. Half-hourly meteorological data from the Ponca City AmeriFlux site were collected by S. Verma and his colleagues (A. Suyker and G. Burba) of the University of Nebraska, Lincoln, NE. I gratefully acknowledge George Boer for his help in interpreting model results and for numerous useful discussions, and Greg Flato and Ken Denman for providing useful comments on earlier version of this manuscript. I would also like to thank Diana Verseghy for providing the code for the CLASS land surface scheme, and other members of the Global Coupled Carbon Climate Model $(\mathrm{GC}^3\mathrm{M})$ project for suggestions and helpful advice. I also thank the two anonymous reviewers for their comments and suggestions that greatly improved the paper.

## Appendix A

### A.1. The biochemical model of leaf photosynthesis

The $C_3$ and $C_4$ photosynthesis model structure adopted in the model is based on the work of Collatz et al. (1991, 1992) and as applied by Sellers et al. (1996) and Cox (2001). The gross leaf photosynthetic rate is calculated in terms of three potentially limiting assimilation rates:

(i) $J_c$ represents the gross photosynthetic rate limited by the photosynthetic enzyme Rubisco.

$$
J_c = \begin{cases}
V_m \left[ \frac{c_i - \Gamma}{c_i + K_c(1 + O_a/K_o)} \right], & \text{for } C_3 \text{ plants} \\
V_m, & \text{for } C_4 \text{ plants}
\end{cases} \tag{A.1}
$$

where $V_m$ ($\mu\mathrm{mol}\,\mathrm{CO}_2\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}$) is the temperature adjusted maximum catalytic capacity of Rubisco, $c_i$ the intercellular $\mathrm{CO}_2$ concentration, $O_a$ (Pa) is the partial pressure of atmospheric oxygen, $\Gamma$ is the $\mathrm{CO}_2$ compensation point, and $K_c$ and $K_o$ (Pa) are the Michaelis-Menten constants for $\mathrm{CO}_2$ and $\mathrm{O}_2$ respectively. $V_m$, $\Gamma$, $K_c$ and $K_o$ are all temperature dependent functions (see Eqs. (A.4–A.6)).

(ii) $J_e$ represents the gross photosynthetic rate limited by the amount of available light.

$$
J_e = \begin{cases}
\alpha(1 - \pi)I \left[ \frac{c_i - \Gamma}{c_i + 2\Gamma} \right], & \text{for } C_3 \text{ plants} \\
\alpha(1 - \pi)I, & \text{for } C_4 \text{ plants}
\end{cases} \tag{A.2}
$$

where $\alpha$ is the quantum efficiency and values of 0.08 and 0.04 are used for $C_3$ and $C_4$ plants, respectively, $\pi$ the leaf scattering coefficient and values of 0.15 and 0.17 are used for $C_3$ and $C_4$ plants, respectively, and $I$ is the incident PAR.

(iii) $J_s$ represents the gross photosynthetic rate limited by the capacity to transport photosynthetic products for $C_3$ plants, but is the $\mathrm{CO}_2$-limited capacity for $C_4$ plants.

$$
J_s = \begin{cases}
0.5 V_m, & \text{for } C_3 \text{ plants} \\
2 \times 10^4 V_m \frac{c_i}{p}, & \text{for } C_4 \text{ plants}
\end{cases} \tag{A.3}
$$

where $p$ (Pa) is surface air pressure.

Gross photosynthetic rate, $A_0$, at the top of the canopy is estimated as the minimum of the above three limiting rates. For the two-leaf model, in Eq. (A.2), $I$ is the diffused fraction of PAR for the shaded part of the canopy and it is the direct beam fraction for the sunlit part. In addition, for the two-leaf model the term $(1 - \pi)$ is omitted since scattering is taken into account via Eq. (9). The maximum temperature adjusted catalytic capacity of Rubisco $V_m$ is estimated as,

$$
V_m = \frac{V_{\max} f_{25}(2.0)}{[1 + \exp(0.3(T_c - T_{\mathrm{up}}))][1 + \exp(0.3(T_{\mathrm{low}} - T_c))]} \tag{A.4}
$$

where $V_{\max}$ is the maximum Rubisco capacity which is used as an input parameter to the model, $f_{25}$ is the standard $Q_{10}$ temperature function $f_{25}(Q_{10}) = Q_{10}^{0.1(T_c - 25)}$, $T_c$ is the canopy temperature, and $T_{\mathrm{up}}$ and $T_{\mathrm{low}}$ are vegetation dependent temperatures. The $\mathrm{CO}_2$ compensation point $\Gamma$ is estimated as,

$$
\Gamma = \begin{cases}
\frac{O_a}{2\sigma}, & \text{for } C_3 \text{ plants} \\
0, & \text{for } C_4 \text{ plants}
\end{cases} \tag{A.5}
$$

where $\sigma$ is the Rubisco specificity for $\mathrm{CO}_2$ relative to $\mathrm{O}_2$ and estimated as $\sigma = 2600 f_{25}(0.57)$. The Michaelis-Menten constants for $\mathrm{CO}_2$ and $\mathrm{O}_2$, $K_c$ and $K_o$ (Pa), respectively, are estimated as,

$$
\begin{aligned}
K_c &= 30 f_{25}(2.1) \\
K_o &= 3 \times 10^4 f_{25}(1.2)
\end{aligned} \tag{A.6}
$$

## References

Aerts, R., 1997. Climate, leaf litter chemistry and leaf litter decomposition in terrestrial ecosystems: a triangular relationship. Oikos 79, 439–449.

Anthoni, P.M., Law, B.E., Unsworth, M.H., 1999. Carbon and water vapour exchange of an open-canopied ponderosa pine ecosystem. Agric. For. Meteorol. 95 (3), 151–168.

Aphalo, P.J., Jarvis, P.G., 1993. An analysis of Ball's empirical model of stomatal conductance. Ann. Botany 72 (4), 321–327.

Arain, M.A., Black, T.A., Barr, A.G., Jarvis, P.G., Massheder, J.M., Verseghy, D.L., Nesic, Z., 2002. Effects of seasonal and interannual climate variability on net ecosystem productivity of boreal deciduous and conifer forests. Can. J. For. Res. 32 (5), 878–891.

Aubinet, M., Grelle, A., Ibrom, A., Moncrieff, J., Foken, T., Kowalski, A.S., Martin, P.H., Berbigier, P., Bernhofer, C., Clement, R., Elbers, J., Granier, A., Grünwald, T., Morgenstern, K., Pilegaard, K., Rebmann, C., Snijders, W., Valentini, R., Vesala, T., 2000. Estimates of the annual net carbon and water exchange of European forests: the EUROFLUX methodology. Adv. Ecol. Res. 30, 113–175.

Baldocchi, D., Falge, E., Gu, L., Olson, R., Hollinger, D., Running, S., Anthoni, P., Bernhofer, C., Davis, K., Evans, R., Fuentes, J., Goldstein, A., Katul, G., Law, B., Lee, X., Malhi, Y., Meyers, T., Munger, W., Oechel, W., Paw U, K.T., Pilegaard, K., Schmid, H.P., Valentini, R., Verma, S., Vesala, T., Wilson, K., Wofsy, S., 2001. FLUXNET: a new tool to study the temporal and spatial variability of ecosystem-scale carbon-dioxide, water vapor, and energy flux densities. Bull. Am. Meteorol. Soc. 82 (11), 2415–2434.

Ball, J.T., Woodrow, I.E., Berry, J.A., 1987. A model predicting stomatal conductance and its contribution to the control of photosynthesis under different environmental conditions. In: Biggens, J. (Ed.), Progress in Photosynthesis Research, vol. V. Dordrecht, Martinus Nijhoff, pp. 221–224.

Betts, R.A., Cox, P.M., Lee, S.L., Woodward, F.I., 1997. Contrasting physiological and structural vegetation feedbacks in climate change simulations. Nature 387, 796–799.

Betts, A.K., Goulden, M., Wofsy, S., 1999. Controls on evaporation in a boreal spruce forest. J. Climate 12, 1601–1618.

Brovkin, V., Ganopolski, A., Svirezhev, Y., 1999. Modelling climate response to historical land cover change. Global Ecol. Biogeogr. 8, 509–517.

Charney, J.G., 1975. Dynamics of deserts and drought in the Sahel. Q. J. R. Meteorol. Soc. 101, 193–202.

Chase, T.N., Pielke Sr., R.A., Kittel, T.G.F., Nemani, R.R., Running, S.W., 2000. Simulated impacts of historical land cover changes on global climate in northern winter. Clim. Dyn. 16, 93–105.

Clapp, R.B., Hornberger, G.M., 1978. Empirical equations for some soil hydraulic properties. Water Resour. Res. 14, 601–604.

Claussen, M., 1998. On multiple solutions of the atmosphere-vegetation system in present-day climate. Global Change Biol. 4, 549–559.

Collatz, G.J., Ball, J.T., Grivet, C., Berry, J.A., 1991. Physiological and environmental regulation of stomatal conductance, photosynthesis and transpiration: a model that includes a laminar boundary layer. Agric. For. Meteorol. 54, 107–136.

Collatz, G.J., Ribas-Carbo, M., Berry, J.A., 1992. Coupled photosynthesis-stomatal conductance model for leaves of C4 plants. Aust. J. Plant Physiol. 19, 519–538.

Cox, P.M., Huntingford, C., Harding, R.J., 1999. A canopy conductance and photosynthesis model for use in a GCM land surface scheme. J. Hydrol. 212–213, 79–94.

Cox, P.M., 2001. Description of the TRIFFID Dynamic Global Vegetation Model. Hadley Centre Technical Note 24, Met Office, Bracknell, UK, 16 pp.

Davidson, E.A., Belk, E., Boone, R.D., 1998. Soil water content and temperature as independent or confounded factors controlling soil respiration in a temperate mixed hardwood forest. Global Change Biol. 4, 217–227.

Davidson, E.A., Verchot, L.V., Cattânio, J.H., Ackerman, I.L., Carvalho, J.E.M., 2000. Effects of soil water content on soil respiration in forests and cattle pastures of eastern Amazonia. Biogeochemistry 48, 53–69.

de Pury, D.G.G., Farquhar, G.D., 1997. Simple scaling of photosynthesis from leaves to canopies without the errors of big-leaf models. Plant Cell Environ. 20, 537–557.

Dickinson, R.E., Henderson-Sellers, A., 1988. Modelling tropical deforestation: a study of GCM land-surface parameterizations. Q. J. R. Meteorol. Soc. 114, 439–462.

Dickinson, R.E., Shaikh, M., Bryant, R., Graumlich, L., 1998. Interactive canopies for a climate model. J. Climate 11, 2823–2836.

Dirmeyer, P.A., Shukla, J., 1994. Albedo as a modulator of climate response to tropical deforestation. J. Geophys. Res. 99 (D10), 20863–20877.

Douville, H., Planton, S., Royer, J.-F., Stephenson, D.B., Tyteca, S., Kergoat, L., Lafont, S., Betts, R.A., 2000. Importance of vegetation feedbacks in doubled-$\mathrm{CO}_2$ climate experiments. Part I: Impact of stomatal and leaf area index changes. J. Geophys. Res. 105 (D11), 14841–14861.

Dreccer, M.F., van Oijen, M., Schapendonk, A.H.C.M., Pot, C.S., Rabbinge, R., 2000. Dynamics of vertical leaf nitrogen distribution in a vegetative wheat canopy: impact on canopy photosynthesis. Ann. Bot. 86, 821–831.

Falge, E., Baldocchi, D., Olson, R., Anthoni, P., Aubinet, M., Bernhofer, C., Burba, G., Ceulemans, R., Clement, R., Dolman, H., Granier, A., Gross, P., Grünwald, T., Hollinger, D., Jensen, N.-O., Katul, G., Keronen, P., Kowalski, A., Lai, C.T., Law, B.E., Meyers, T., Moncrieff, J., Moors, E., Munger, J.W., Pilegaard, K., Rannik, Ü., Rebmann, C., Suyker, A., Tenhunen, J., Tu, K., Verma, S., Vesala, T., Wilson, K., Wofsy, S., 2001a. Gap filling strategies for defensible annual sums of net ecosystem exchange. Agric. For. Meteorol. 107, 43–69.

Falge, E., Baldocchi, D., Olson, R., Anthoni, P., Aubinet, M., Bernhofer, C., Burba, G., Ceulemans, R., Clement, R., Dolman, H., Granier, A., Gross, P., Grünwald, T., Hollinger, D., Jensen, N.-O., Katul, G., Keronen, P., Kowalski, A., Lai, C.T., Law, B.E., Meyers, T., Moncrieff, J., Moors, E., Munger, J.W., Pilegaard, K., Rannik, Ü., Rebmann, C., Suyker, A., Tenhunen, J., Tu, K., Verma, S., Vesala, T., Wilson, K., Wofsy, S., 2001b. Gap filling strategies for long term energy flux data sets. Agric. For. Meteorol. 107, 71–77.

Farquhar, G.D., von Caemmerer, S., Berry, J.A., 1980. A biochemical model of photosynthetic $\mathrm{CO}_2$ assimilation in leaves of C3 species. Planta 149, 78–90.

Feddes, R.A., Kowalik, P.J., Zaradny, H., 1978. Simulation of field water use and crop yield. Simulation Monographs, Pudoc, Wageningen, Netherlands, 189 pp.

Field, C., Mooney, H.A., 1986. The photosynthesis-nitrogen relationship in wild plants. In: Givnish, T.J. (Ed.), On the Economy of Plant Form and Function. Cambridge University Press, Cambridge, pp. 25–55.

Foley, J.A., Prentice, I.C., Ramankutty, N., Levis, S., Pollard, D., Sitch, S., Haxeltine, A., 1996. An integrated biosphere model of land surface processes, terrestrial carbon balance, and vegetation dynamics. Global Biogeochem. Cycles 10, 603–628.

Gholz, H.L., Wedin, D.A., Smitherman, S.M., Harmon, M.E., Parton, W.J., 2000. Long-term dynamics of pine and hardwood litter in contrasting environments: toward a global model of decomposition. Global Change Biol. 6, 751–765.

Goulden, M.L., Munger, J.W., Fan, S.-M., Daube, B.C., Wofsy, S.C., 1996. Measurements of carbon sequestration by long-term eddy covariance: methods and a critical evaluation of accuracy. Global Change Biol. 2, 169–182.

Griffin, D.M., 1981. Water and microbial stress. In: Alexander, M. (Ed.), Advances in Microbial Ecology. Plenum Press, New York, pp. 91–136.

Heck, P., Luthi, D., Wernli, H., Schar, C., 2001. Climate impacts of European-scale anthropogenic vegetation changes: a sensitivity study using a regional climate model. J. Geophys. Res. 106 (D8), 7817–7835.

Hocking, P.J., Meyer, C.P., 1991. Effects of $\mathrm{CO}_2$ enrichment and nitrogen stress on growth, and partitioning of dry matter and nitrogen in wheat and maize. Aust. J. Plant Physiol. 18, 339–356.

Holdridge, L.R., 1947. Determination of world plant formations from simple climatic data. Science 105, 367–368.

Howard, P.J.A., Howard, D.M., 1979. Respiration of decomposing litter in relation to temperature and moisture. Oikos 33, 457–465.

Ingestad, T., Lund, A.-B., 1986. Theory and techniques for steady state mineral nutrition and growth of plants. Scandinavian J. For. Res. 1, 439–453.

Ito, A., Oikawa, T., 2000. A model analysis of the relationship between climate perturbations and carbon budget anomalies in global terrestrial ecosystems: 1970–1997. Clim. Res. 15 (3), 161–183.

Jarvis, P.G., 1976. The interpretation of leaf water potential and stomatal conductance found in canopies in the field. Philos. Trans. R. Soc. London, Ser. B 273, 593–610.

Jobbagy, E.G., Jackson, R.B., 2000. The vertical distribution of soil organic carbon and its relation to climate and vegetation. Ecol. Appl. 10 (2), 423–436.

Keyser, A.R., Kimball, J.S., Nemani, R.R., Running, S.W., 2000. Simulating the effects of climate change on the carbon balance of North American high-latitude forests. Global Change Biol. 6 (s1), 185–195.

Kirschbaum, M.U.F., 1995. The temperature dependence of soil organic matter decomposition, and the effect of global warming on soil organic C storage. Soil Biol. Biochem. 27 (6), 753–760.

Kirkegaard, J.A., Howe, G.N., Simpfendorfer, S., Angus, J.A., Gardner, P.A., Hutchinson, P., 2001. Poor wheat yield response to conservation cropping—causes and consequences during 10 years of the Harden Tillage Trial. In: Proceedings of the 10th Australian Agronomy Conference, Hobart, 28 January to 1 February.

Knorr, W., 2000. Annual and interannual $\mathrm{CO}_2$ exchanges of the terrestrial biosphere: process based simulations and uncertainties. Global Ecol. Biogeography 9, 225–252.

Kull, O., Jarvis, P.G., 1995. The role of nitrogen in a simple scheme to scale up photosynthesis from leaf to canopy. Plant Cell Environ. 18, 1174–1182.

Lavelle, P., Blanchart, E., Martin, S., Martin, A., Barois, S., Toutain, F., Spain, A., Schaefer, R., 1993. A hierarchical model for decomposition in terrestrial ecosystems: application to soils of the humid tropics. Biotropica 25 (2), 130–150.

Law, B.E., Thornton, P.E., Irvine, J., Anthoni, P.M., van Tuyl, S., 2001. Carbon storage and fluxes in ponderosa pine forests at different developmental stages. Global Change Biol. 7 (7), 755–777.

Lean, J., Rowntree, P.R., 1993. A GCM simulation of the impact of Amazonian deforestation on climate using an improved canopy representation. Q. J. R. Meteorol. Soc. 119, 509–530.

Lean, J., Rowntree, P.R., 1997. Understanding the sensitivity of a GCM simulation of Amazonian deforestation to the specification of vegetation and soil characteristics. J. Clim. 10, 1216–1235.

Leuning, R., 1990. Modeling stomatal behaviour and photosynthesis of Eucalyptus grandis. Aust. J. Plant Physiol. 17, 159–175.

Leuning, R., 1995. A critical appraisal of a combined stomatal-photosynthesis model for $C_3$ plants. Plant Cell Environ. 18, 339–355.

Lloyd, J., Taylor, J.A., 1994. On the temperature dependence of soil respiration. Funct. Ecol. 8, 315–323.

Ludeke, M.K.B., Badeck, F.W., Otto, R.D., Hager, C., Donges, S., Kindermann, J., Wirth, G., Lang, T., Jakel, U., Klaudius, A., Ramge, P., Habermehl, S., Kohlmaier, G.H., 1994. The Frankfurt Biosphere Model: a global process oriented model of seasonal and long-term $\mathrm{CO}_2$ exchange between terrestrial ecosystems and the atmosphere. I. Model description and illustrative results for cold deciduous and boreal forests. Clim. Res. 4, 143–166.

Luken, J.O., Billings, W.D., 1985. The influence of microtopographic heterogeneity on carbon dioxide efflux from a subarctic bog. Holarct. Ecol. 8, 306–312.

Massman, W.J., Lee, X., 2002. Eddy covariance flux corrections and uncertainties in long-term studies of carbon and energy exchanges. Agric. For. Meteorol. 113, 121–144.

Medlyn, B., 2001. Radiation conversion. In: Kirschbaum, M.U.F., Mueller, R. (Eds.), Net Ecosystem Exchange. Cooperative Research Centre for Greenhouse Accounting, Canberra, Australia, pp. 33–37.

Melillo, J.M., Aber, J.D., Muratore, J.F., 1982. Nitrogen and lignin control of hardwood leaf litter decomposition dynamics. Ecology 63 (3), 621–626.

Mo, X., Liu, S., 2001. Simulating evapotranspiration and photosynthesis of winter wheat over the growing season. Agric. For. Meteorol. 109 (3), 203–222.

Oberbauer, S.F., Tenhunen, J.D., Reynolds, J.F., 1991. Environmental effects on $\mathrm{CO}_2$ efflux from water track and tussock tundra in arctic Alaska, USA. Arctic Alpine. Res. 23, 162–169.

Orchard, V.A., Cook, F., 1983. Relationship between soil respiration and soil moisture. Soil Biol. Biogeochem. 15, 447–453.

Orchard, V.A., Cook, F.J., Corderoy, D.M., 1992. Field and laboratory studies on the relationships between respiration and moisture for two soils of contrasting fertility status. Pedobiologia 36, 21–33.

Paul, K., 2001. Temperature and moisture effects on decomposition. In: Kirschbaum, M.U.F., Mueller, R. (Eds.), Net Ecosystem Exchange. Cooperative Research Centre for Greenhouse Accounting, Canberra, Australia, pp. 95–102.

Pollard, D., Thompson, S.L., 1995. Use of a land surface transfer scheme (LSX) in a global climate model: the response to doubling stomatal resistance. Global Planetary Change 10, 129–161.

Reich, P.B., Walters, M.B., Tjoelker, M.G., Vanderklein, D., Buschena, C., 1998. Photosynthesis and respiration rates depend on leaf and root morphology and nitrogen concentration in nine boreal tree species differing in relative growth rate. Funct. Ecol. 12, 395–405.

Rice, C.W., 1999. Belowground carbon allocation and cycling in tallgrass prairie and wheat ecosystems. In: Proceedings of the Paper Presentation at the Annual Great Plains Climate Change Meeting of NIGEC, Lincoln, Nebraska, March 1999.

Ronda, R.J., de Bruin, H.A.R., Holtslag, A.A.M., 2001. Representation of the canopy conductance in modeling the surface energy budget for low vegetation. J. Appl. Meteorol. 40 (8), 1431–1444.

Ryan, M.G., 1991. Effects of climate change on plant respiration. Ecol. Appl. 1 (2), 157–167.

Savage, K., Moore, T.R., Crill, P.M., 1997. Methane and carbon dioxide exchanges between the atmosphere and northern boreal forests soils. J. Geophys. Res. 102, 29279–29288.

Schlentner, R.E., van Cleve, K., 1985. Relationships between CO₂ evolution from soil, substrate temperature, and substrate moisture in four mature forests types in interior Alaska. Can. J. For. Res. 15, 97–106.

Schlesinger, W.H., Andrews, J.A., 2000. Soil respiration and the global carbon cycle. Biogeochemistry 4, 7–20.

Schlesinger, W.H., Winkler, J.P., Megonigal, J.P., 2000. Soils and the global carbon cycle. In: Wigley, T.M.L., Schimel, D.S. (Eds.), The Carbon Cycle. Cambridge University Press, Cambridge, pp. 93–101.

Sellers, P.J., 1985. Canopy reflectance, photosynthesis, and transpiration. Int. J. Remote Sens. 6 (8), 1335–1372.

Sellers, P.J., Berry, J.A., Collatz, G.J., Field, C.B., Hall, F.G., 1992. Canopy reflectance, photosynthesis. Remote Sens. Environ. 42, 187–216.

Sellers, P.J., Los, S.O., Tucker, C.J., Justice, C.O., Dazlich, D.A., Collatz, G.J., Randall, D.A., 1996. A revised land surface parameterization (SiB2) for atmospheric general circulation models. Part 2. The generation of global fields of terrestrial biophysical parameters from satellite data. J. Clim. 9, 706–737.

Shaver, G.R., Billings, W.D., Chapin III, F.S., Giblin, A.E., Nadelhoffer, K.J., Oechel, W.C., Rastetter, E.B., 1992. Global change and the carbon balance of arctic ecosystems. BioScience 61, 415–435.

Suyker, A.E., Verma, S., 2002. Carbon dioxide exchange in a winter wheat and a tall grass prairie. In: Proceedings of the 25th Conference on Agricultural and Forest Meteorology, Paper 10.5, 20–24 May, Norfolk, Virginia.

Tjoelker, M.G., Oleksyn, J., Reich, P.B., 2001. Modelling respiration of vegetation: evidence for a general temperature-dependent Q₁₀. Global Change Biol. 7 (2), 223–230.

Verma, S.B., 1996. Measurement of Mass and Energy Fluxes in Grassland and Agricultural Ecosystems. Principal Investigators Workshop, Great Plains Regional Center of the National Institute for Global Environmental Change, Nebraska City, Nebraska, 9–10 October.

Verseghy, D., 1991. CLASS—a Canadian land surface scheme for GCMs. Part I. Soil Model. Int. J. Climatol. 11, 111–133.

Verseghy, D., McFarlane, N.A., Lazare, M., 1993. CLASS—A Canadian land surface scheme for GCMs. Part II. Vegetation model and coupled runs. Int. J. Climatol. 13, 347–370.

Wang, Y.-P., Leuning, R., 1998. A two-leaf model for canopy conductance, photosynthesis and partitioning of available energy. Part I. Model description and comparison with a multi-layered model. Agric. For. Meteorol. 91, 89–111.

Wang, S., Grant, R.F., Verseghy, D.L., Black, T.A., 2001. Modelling plant carbon and nitrogen dynamics of a boreal aspen forest in CLASS—the Canadian Land Surface Scheme. Ecol. Modell. 142, 135–154.

Warnant, P., Francois, L., Gerard, J.-C., 1994. A global model of terrestrial biological productivity. Global Biogeochem. Cycles 8 (3), 255–270.

Wechsung, G., Wechsung, F., Wall, G.W., Adamsen, F.J., Kimball, B.A., Garcia, R.L., Pinter Jr., P.J., Kartschall, T., 1995. Biomass and growth rate of a spring wheat root system grown in free-air $\mathrm{CO}_2$ enrichment (FACE) and ample soil moisture. J. Biogeography 22, 623–634.

Wofsy, S.C., Goulden, M.L., Munger, J.W., Fan, S.-M., Bakwin, P.S., Daube, B.C., Bassow, S.L., Bazzaz, F.A., 1993. Net $\mathrm{CO}_2$ exchange in a mid-latitude forest. Science 260, 1314–1317.

Woodward, F.I., Smith, T.M., Emanuel, W.R., 1995. A global land primary productivity and phytogeography model. Global Biogeochem. Cycles 9 (4), 471–490.

Xue, Y., 1997. Biosphere feedback on regional climate in tropical north Africa. Q. J. R. Meteorol. Soc. 123, 1483–1515.

Zhao, M., Pitman, A.J., Chase, T., 2001. The impact of land cover change on the atmospheric circulation. Clim. Dyn. 17 (5–6), 467–477.