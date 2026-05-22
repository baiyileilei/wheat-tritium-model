# A one-dimensional dynamical soil–atmosphere tritiated water transport model

**Hiromi Yamazawa**

*Department of Environmental Sciences, Japan Atomic Energy Research Institute, Tokai-mura, Ibaraki, 319-1195 Japan*

Received 23 November 2000; received in revised form 22 January 2001; accepted 14 March 2001

## Abstract

A one-dimensional numerical model for simulating transport of heat, water and tritiated water (hereafter referred to as HTO) in unsaturated surface soil and their soil-atmosphere exchange has been developed. This model consists of five prognostic equations for soil temperature, soil water content, soil air humidity and HTO concentrations in liquid and gas phases. The model is applied to a hypothetical and simplified scenario of HTO contamination of an unsaturated soil layer with actually observed meteorological conditions in Japan to analyze the dependencies of the HTO transport and evaporation on the meteorological conditions, hydrological conditions and soil properties. Results obtained indicate that the infiltration of water and the soil moisture conditions largely affect the transport and evaporation. Therefore, precipitation and soil moisture characteristics seem to be the most essential factors. Other meteorological factors are found to have substantial effects through two pathways, one being direct and fast by changing the atmospheric conditions and availability of vapor at the ground surface, and the other being indirect and slow by affecting the infiltration and water content. It can also be demonstrated that the usage of time-averaged meteorological and hydrological conditions reduce the estimated amounts of HTO transport and evaporation considerably, and that high-concentration episodes virtually determine the annual mean HTO concentration and evaporation. © 2001 Elsevier Science Ltd. All rights reserved.

**Keywords:** Tritiated water; Transport; Soil-atmosphere exchange; Surface evaporation; Numerical model; Simulation

## Software availability

| Field              | Value                                                                                           |
|:-------------------|:------------------------------------------------------------------------------------------------|
| Name of software   | SOLVEG                                                                                          |
| Developer          | Dr. H. Yamazawa and H. Nagai                                                                    |
| Contact address    | Department of Environmental Sciences, Japan Atomic Energy Research Institute, Tokai-mura, Ibaraki, 319-1195 Japan |
| First available    | 1997                                                                                            |
| Hardware           | Ultra-SPARC II EWS                                                                              |
| Software           | FORTRAN90                                                                                       |
| Program size       | Executable file 140 KB, Source code 6000 statements                                             |
| Availability and cost | Available only for non-profit purposes after JAERI's formalities, at no charge in principle    |

## 1. Introduction

Origins of environmental tritium, most of which is mainly in a molecular form (hereafter, HT, standing also for $T_{2}$), tritiated water (HTO, also for $T_{2}O$) or tritiated methane, are due to the atmospheric nuclear bomb tests in the 1950s and 1960s, releases from nuclear facilities and also due to cosmic ray reactions in the upper atmosphere (Okada and Momoshima, 1993). The use of tritium as fuel for fusion reactors in the future will be an additional and substantial source of environmental tritium. Once released into the atmosphere near the ground surface, HT is rapidly oxidized by biological activities in surface soils to form HTO. It is widely known that other oxidation processes are negligible compared with the biological oxidation in surface soil (Ogram, 1982). Since HTO is much more easily taken up by the human body than HT and thus causes a much higher radiological dose (Peterman et al., 1985), it is important to know the fate of HTO in the environment and to have the means to realistically simulate its behaviour.

Although the behaviour of HT and HTO in the atmosphere-bare soil system is rather simple as compared with that of a system including vegetation, it includes many elemental processes such as atmospheric dispersion, exchange between the atmosphere and the ground surface, and transport in the soil in gas and liquid phases (Bunnenberg et al., 1990). In addition, microbial oxidation in the surface soil is of high importance and complexity (Dunstall and Ogram, 1991; Murata and Noguchi, 1992). On the other hand, the atmosphere-surface exchange of momentum, heat, water vapor and other quantities have long been investigated from meteorological and hydrological points of view and much effort has been concentrated on this topic. The well-established part of this area has been summarized in many text books, for instance Brutsaert (1982), Pielke (1984), Stull (1988), Jones (1992) and Tindall et al. (1999). With help from these well-established theories, rules and parameter values, it would be possible to separate still unknown behaviours of tritium in the environment from known and/or predictable ones. To do this, however, we need a numerical model of the atmosphere-bare soil system since the physical quantities and parameters have complex interdependencies. A ground surface model has been developed for this objective which is applied together with a meteorological model (Yamazawa and Nagai, 1997; Nagai and Yamazawa, 1999). This paper will describe the original ground surface model and the tritium-related part, which is newly added in this study.

This model was applied to a hypothetical and idealized case, in which the evaporation of tritiated water from, and the transport in, an unsaturated surface soil layer were simulated by the model for various types of bare soil with the input of observed meteorological data. The aim of these simulations is to illustrate the interdependency of factors such as meteorological conditions, soil types, etc., affecting the tritiated water transport in the unsaturated soil layer under actual meteorological conditions in Japan. The relative importance of the elemental processes of tritiated water transport and evaporation such as advection, gas diffusion, liquid diffusion, etc., is also evaluated to explore the possibility of simplifying the model.

## 2. Model

### 2.1. Heat conduction and water transport in soil

Symbols are listed in the Nomenclature. The model prognostically evaluates the vertical profiles of the soil temperature $T_{\mathrm{s}}$, the volumetric soil water content $\eta_{\mathrm{w}}$, and the specific humidity of the soil air $q_{\mathrm{sa}}$.

$$
\frac{\partial T_{\mathrm{s}}}{\partial t} = \frac{\partial}{\partial z} k_{\mathrm{s}}\frac{\partial T_{\mathrm{s}}}{\partial z} +\frac{\dot{H}_{\mathrm{b}}}{C_{\mathrm{s}}\rho_{\mathrm{s}}} -\frac{C_{\mathrm{w}}E_{\mathrm{w}}}{C_{\mathrm{s}}\rho_{\mathrm{s}}}\frac{\partial T_{\mathrm{s}}}{\partial z} \tag{1}
$$

$$
\frac{\partial\eta_{\mathrm{w}}}{\partial t} = -\frac{1}{\rho_{\mathrm{w}}}\frac{\partial E_{\mathrm{w}}}{\partial z} -\frac{1}{\rho_{\mathrm{w}}}(\hat{E}_{\mathrm{t}} +\hat{E}_{\mathrm{b}}) \tag{2}
$$

$$
\frac{\partial[(\eta_{\mathrm{ws}} - \eta_{\mathrm{w}})q_{\mathrm{sa}}]}{\partial t} = \frac{\partial}{\partial z}\bigg[D_{\mathrm{qsf}}q_{\mathrm{sa}}(\eta_{\mathrm{w}})\frac{\partial q_{\mathrm{sa}}}{\partial z}\bigg] + \frac{\hat{E}_{\mathrm{b}}}{\rho} \tag{3}
$$

where the vertical flux of water is expressed as:

$$
E_{\mathrm{w}} = -\rho_{\mathrm{w}}\bigg(D\frac{\partial\eta_{\mathrm{w}}}{\partial z} +K\bigg) \tag{4}
$$

The heat conduction equation has a latent heat term for evaporation or condensation of water (hereafter, simply referred to as the evaporation term) and an advection (convection) term due to macroscopic vertical movement of water in addition to the conduction term. The equation for the liquid water movement is of classical Richard's type with the volumetric water content as the dependent variable instead of the hydraulic potential. The equation has additional terms concerning transpiration and evaporation/condensation. The equation for water vapor contains a diffusion term and an evaporation/condensation term. This model does not consider the mean air flow in soil, which might be caused by the trend of the air pressure at the ground surface or the infiltration of water.

The boundary condition for the heat conduction equation is a ground surface heat budget equation,

$$
R_{0} = H_{0} + G_{0} + H_{\mathrm{p0}} \tag{5}
$$

where

$$
\begin{aligned}
\text{net radiation } R_0 &= (1 - A_{\mathrm{b}})S_{\mathrm{l0}} + \epsilon_{\mathrm{b}}(L_{\mathrm{l0}} - \sigma T_{\mathrm{s0}}^4) \tag{6} \\
\text{sensible heat flux } H_0 &= C_{\mathrm{p}}\rho c_{\mathrm{H0}}|\mathbf{u}_{\mathrm{r}}|(T_{\mathrm{s0}} - T_{\mathrm{r}}) \tag{7} \\
\text{conductive heat flux } G_0 &= C_{\mathrm{p}}k_{\mathrm{s}}\frac{\partial T_{\mathrm{s}}}{\partial z}\bigg|_{z = 0} \tag{8}
\end{aligned}
$$

This heat budget equation does not have a latent heat flux term since the water vapor flux is explicitly evaluated by Eq. (3) and the latent heat is treated as a volume sink/source in Eq. (1). The boundary condition of Eq. (2) is determined by the continuity of liquid water flux at the ground surface, i.e.,

$$
E_{\mathrm{w0}} = \left\{ \begin{array}{ll}
E_{\mathrm{w0s}} & \eta_{\mathrm{w0}}\geq \eta_{\mathrm{w0s}} \\
-P_{\mathrm{r0}} + E_{\mathrm{r}} & \eta_{\mathrm{w0}}< \eta_{\mathrm{w0s}}
\end{array} \right. \tag{10}
$$

where $E_{\mathrm{r}}$ is the amount of runoff and $E_{\mathrm{w0s}}$ the maximum infiltration flux when the soil is saturated,

$$
E_{\mathrm{w0s}} = -\rho_{\mathrm{w}}K_{\mathrm{s}} \tag{11}
$$

If the level of soil water exceeds the saturated soil water content, the present version of the model assumes that the water in excess is stored at the ground surface unless the runoff $E_{\mathrm{r}}$ is externally specified.

$$
\frac{\mathrm{d}R}{\mathrm{d}t} = P_{\mathrm{r0}} - E_{\mathrm{r}} + E_{\mathrm{w0}} \tag{12}
$$

The water balance of a rice paddy field can be expressed by this formulation.

The boundary condition for the specific humidity can be determined by solving the following equation,

$$
-\rho D_{\mathrm{ufs}}(\eta_{\mathrm{w0}})\frac{\partial q_{\mathrm{s}}}{\partial z}\bigg|_{z = 0} + E_{\mathrm{b0}} = E_{\mathrm{0}} \tag{13}
$$

where

$$
E_{\mathrm{b0}} = \int \hat{E}_{\mathrm{b}}\mathrm{d}z \tag{14}
$$

and

$$
E_{\mathrm{0}} = \rho c_{\mathrm{E0}}|\mathbf{u}_{\mathrm{r}}|(q_{\mathrm{s0}} - q_{\mathrm{r}}) \tag{15}
$$

This boundary condition assumes that the water vapor flux from the ground surface to the atmosphere is the sum of water vapor flux diffused from the inside of the soil layer and the direct evaporation from the $\delta z_{0}$-thick layer that is in direct contact with the atmosphere.

### 2.2. Tritiated water

The present model has two equations for transport of tritiated water, in liquid and gas phases, respectively,

$$
\frac{\partial\eta_{\mathrm{w}}\chi_{\mathrm{w}}}{\partial t} = -\frac{1}{\rho_{\mathrm{w}}}\frac{\partial E_{\mathrm{w}}\chi_{\mathrm{w}}}{\partial z} +\frac{\partial}{\partial z}\bigg(D_{\mathrm{Tw}}\frac{\partial\chi_{\mathrm{w}}}{\partial z}\bigg) - \hat{e}_{\mathrm{b}} \tag{16}
$$

$$
\frac{\partial[(n_{\mathrm{ws}} - n_{\mathrm{w}})\chi_{\mathrm{ws}}]}{\partial t} = \frac{\partial}{\partial z}\bigg(D_{\mathrm{Ts}}f_{\mathrm{s}}(\eta_{\mathrm{w}})\frac{\partial\chi_{\mathrm{ws}}}{\partial z}\bigg) + \hat{e}_{\mathrm{b}} \tag{17}
$$

These two equations are linked to each other by the evaporation/condensation term $\hat{e}_{\mathrm{b}}$. The liquid phase equation has an advection term and a diffusion term, the latter including not only molecular diffusion but also dispersion,

$$
D_{\mathrm{Tw}} = f_{\mathrm{w}}(\eta_{\mathrm{w}})\hat{D}_{\mathrm{Tw}} + A_{\mathrm{w}}E_{\mathrm{w}} / \rho_{\mathrm{w}} \tag{18}
$$

The dispersion is expressed in terms of the speed of water flow in soil. The surface boundary condition for the liquid phase equation is specified by an additional term only for the top (surface) layer expressing a gain of tritiated water due to contaminated precipitation. Dilution due to precipitation is indirectly accounted for by the increase of water content on the left hand side of the equation. The evaporation of tritiated water into the atmosphere is expressed in a similar manner to that of water, but independently,

$$
-D_{\mathrm{Tw}}f_{\mathrm{sa}}(\eta_{\mathrm{w0}})\frac{\partial\chi_{\mathrm{sa}}}{\partial z}\bigg|_{z = 0} + e_{\mathrm{b0}} = e_{\mathrm{0}} \tag{19}
$$

where

$$
\begin{aligned}
e_{\mathrm{b0}} &= \int \hat{e}_{\mathrm{b}}\mathrm{d}z \tag{20} \\
e_{\mathrm{0}} &= c_{\mathrm{E0}}|\mathbf{u}_{\mathrm{r}}|(\chi_{\mathrm{sa0}} - \chi_{\mathrm{r}}) \tag{21}
\end{aligned}
$$

### 2.3. Evaporation of water in soil

Many models assume that evaporation occurs at the ground surface. This implies that water or tritiated water should undergo liquid phase transport process through unsaturated soil before evaporating at the surface. However, evaporation of water and tritiated water occurs not only at the ground surface but also beneath it (Kondo and Saigusa, 1994). If the surface soil is extremely dry as is found for bare soil surface in the afternoon of dry and hot days, gas diffusion and evaporation inside soil may become more dominant than liquid phase transport since the hydraulic conductivity is very small and liquid water hardly moves.

The present model explicitly deals with gas phase diffusion as shown by Eqs. (3) and (17). The evaporation of water and tritiated water in soil is respectively expressed as

$$
\begin{aligned}
\hat{E}_{\mathrm{b}} &= \frac{\rho}{r_{\mathrm{b}}} [q_{\mathrm{sa}}(T_{\mathrm{s}}) - q_{\mathrm{sa}}] \quad \text{when } q_{\mathrm{sa}}(T_{\mathrm{s}}) > q_{\mathrm{sa}} \tag{22} \\
\hat{e}_{\mathrm{b}} &= \frac{\rho}{r_{\mathrm{b}}} \left[\frac{q_{\mathrm{sa}}(T_{\mathrm{s}})\chi_{\mathrm{w}}}{\rho_{\mathrm{w}}} -\frac{\chi_{\mathrm{w}}}{\rho} \right] \tag{23}
\end{aligned}
$$

This formulation is based on the idea that the driving force of the evaporation in soil is the difference in specific humidity or tritiated water concentration between the evaporation site (surface of soil water) and the macro soil pore and that the evaporation is regulated by the resistance $r_{\mathrm{b}}$ which is an experimentally determined function of the volumetric water content (Kondo and Saigusa, 1994; Kondo and Xu, 1997). The resistance which is recalculated from their original formulae to fit the present definition is shown in Fig. 1. Since the resistance is not available for all soil types, one of the functions is selected for each soil type according to the similarity of the soil texture in the present simulations. It is assumed that the condensation of water occurs within a very short time to keep the specific humidity less than or equal to the saturation specific humidity at the soil temperature. The condensation of tritiated water, on the other hand, is evaluated by the above formula.

*[Figure 1]*  
*Dependency of the evaporation resistance on the water content, recalculated from the formulae published by Kondo and Saigusa (1994) (open marks) and Kondo and Xu (1997) (black marks).*

### 2.4. Moisture characteristics

The model uses a moisture characteristic curve of either Van Genuchten (1980) and Clapp-Hornberger (1978) type. In the present applications, the latter formulation is used since, although the former usually fits experimental data better, the latter is numerically easier to handle and the purpose of this study is to have an overall view of soil type dependency of the tritiated water transport in soil. The hydraulic potential $\Psi$, conductivity $K$, and diffusivity $D$ are respectively expressed by

$$
\begin{aligned}
\Psi &= \Psi_s\left(\frac{\eta_w}{\eta_{ws}}\right)^{-b} \tag{24} \\
K &= K_s\left(\frac{\eta_w}{\eta_{ws}}\right)^{2b + 3} \tag{25} \\
D &= K\frac{\partial\Psi}{\partial\eta_w} \tag{26}
\end{aligned}
$$

The parameters used in the present simulations are listed in Table 1. They are based on the classification by US Department of Agriculture and the values were compiled by Pielke (1984) and Cosby et al. (1984).

### 2.5. Thermal characteristics

The heat conductivity of soil is evaluated with the following formula derived by McCumber and Pielke (1981) from the data by Al Nakshabandi and Kohnke (1965),

$$
C_s\rho_sk_s[\mathrm{Wm}^{-1}\mathrm{K}^{-1}] = \left\{ \begin{array}{ll}
419\exp (-pF - 2.7), & pF\leq 5.1\\
0.172, & pF > 5.1
\end{array} \right. \tag{27}
$$

where $pF = \log_{10}(-\Psi) + 2$. The heat capacity of bulk soil is also a function of the water content,

$$
C_s\rho_s = (C_s\rho_{s})_{soil\max} + \eta_w(C_s\rho_{s})_{water} \tag{28}
$$

After Pielke (1984), the dependency of the soil surface albedo $A_{\mathrm{b}}$ on the wetness of the surface soil and the solar zenith angle $Z$ (deg.) is considered,

$$
A_{\mathrm{b}} = \max (A_0 - k_{\mathrm{A}}\frac{\eta_w}{\eta_{ws}} A_{\mathrm{m}}) + 0.01[\exp (0.003286Z^{1.5})] \tag{29}
$$

where the constants $(A_0, A_{\mathrm{m}}, k_{\mathrm{A}})$ depend on the soil type, and the values of $(0.28, 0.20, 0.18)$ for sandy soil and $(0.31, 0.34, 0.14)$ for other soil types are used.

### 2.6. Numerical aspects

The prognostic model Eqs. (1)-(3) for temperature, liquid water and water vapor, respectively, are solved with a finite difference scheme. The HTO transport Eqs. (16) and (17) are solved with the same finite difference scheme in parallel with the other prognostic equations by using the information on the temperature, water content and water movement at each time step. These equations can be written in a generalized form

$$
\frac{\partial\phi}{\partial t} = w\frac{\partial\phi}{\partial z} +\frac{\partial}{\partial z} K\frac{\partial\phi}{\partial z} +A\phi +F
$$

The model numerically solves the equation in two steps, one for the advection term with an explicit method and the other for the rest terms with a semi-implicit method except for the forcing term,

$$
\begin{aligned}
\frac{\phi^{*} - \phi^{t}}{\delta t} &= \mathrm{adv}(\phi^{t}) \\
\frac{\phi^{t + \delta t} - \phi^{*}}{\delta t} &= \alpha \left[\left(\frac{\partial}{\partial z}K\frac{\partial\phi}{\partial z}\right)^{t + \delta t} + A\phi^{t + \delta t}\right] + (1 - \alpha)\left[\left(\frac{\partial}{\partial z}K\frac{\partial\phi}{\partial z}\right)^{*} + A\phi^{*}\right] + F^{*}
\end{aligned} \tag{30}
$$

The advection term 'adv' on the right hand side, which corresponds to the term on the right hand side of Eq. (30), is spatially discretized with the low-numerical diffusion scheme HIFI by Yamazawa (1996). The lengthy description of this scheme will not be repeated here. A usual center-in-space differentiation is used for the diffusion terms. According to a value of the parameter $\alpha$, this method can become explicit, semi-implicit or fully implicit. For the present applications, $\alpha = 0.8$ is used. More detailed descriptions of the numerical solution method can be found in other reports (Yamazawa and Nagai, 1997; Nagai and Yamazawa, 1999).

**Table 1**  
Soil properties used in this study. Values in this table are based on Pielke (1984) which used Clapp-Hornberger (1978). Cosby et al. (1984) is also adopted.

| Soil Type        | Saturation Water Content (v/v) | Saturation Hydraulic Potential (m) | Saturation Hydraulic Conductivity (mm s⁻¹) | Exponent b in Eq. (24) | Wilting point (v/v) | Heat Capacity (MJ m⁻³ K⁻¹) |
|:-----------------|:-------------------------------|:----------------------------------|:-------------------------------------------|:-----------------------|:--------------------|:---------------------------|
| Sand             | 0.339                          | -0.069                            | 0.107                                      | 2.79                   | 0.0677              | -                          |
| Loamy sand       | 0.421                          | -0.036                            | 0.0141                                     | 4.26                   | 0.0750              | -                          |
| Sandy loam       | 0.434                          | -0.141                            | 0.00523                                    | 4.74                   | 0.1142              | -                          |
| Silt             | 0.476                          | -0.759                            | 0.0028                                     | 5.33                   | 0.1794              | -                          |
| Loam             | 0.439                          | -0.355                            | 0.00338                                    | 5.25                   | 0.1547              | -                          |
| Sandy clay loam  | 0.404                          | -0.135                            | 0.00445                                    | 6.66                   | 0.1749              | -                          |
| Silty clay loam  | 0.464                          | -0.617                            | 0.00204                                    | 8.72                   | 0.2181              | -                          |
| Clay loam        | 0.465                          | -0.263                            | 0.00245                                    | 8.17                   | 0.2498              | -                          |
| Sandy clay       | 0.406                          | -0.098                            | 0.00722                                    | 10.73                  | 0.2193              | -                          |
| Silty clay       | 0.468                          | -0.324                            | 0.00134                                    | 10.39                  | 0.2832              | -                          |
| Clay             | 0.468                          | -0.468                            | 0.000974                                   | 11.55                  | 0.2864              | -                          |

## 3. Simulations

### 3.1. Tests of the model code

The overall performance of the model including the vegetation part was preferably tested from a meteorological point of view with observational data of surface-atmosphere fluxes of heat and moisture (Nagai, 2001). The equations used in the present model are classical ones such as a Richard's equation for liquid water movement or a heat conduction equation for temperature, whose original form can be found in many textbooks, and their nature is a one-dimensional advection diffusion equation. The validation calculations were, therefore, conducted to test the numerical validity of the model and the adequacy of the parameter values used.

Since, as shown later, the model was applied to a very early stage of transition from the initial step-function shaped spatial distribution of concentration to rather smooth distribution, test calculations and comparison with analytical solutions were conducted to check the numerical validity of the newly added tritium-related part of the model and to determine the grid interval to minimize computational cost and numerical error. The test calculations assumed a constant volumetric water content of 0.2, no gas diffusion, no liquid water movement, and hence no advection and dispersion. The initial and boundary conditions were identical to those for the main simulations described in the next section. The test runs were carried out with different spatial resolutions, that is 10, 20, 40, 100 and 200 grids for a 1-m-thick surface soil layer.

*[Figure 2]*  
*Comparison of the numerical solution of Eq. (16) with the analytical solution during the first 350 days. The curves of the numerical solution for 200 model layers are overlapping the analytical solution.*

The numerical simulation results are compared with the analytical solutions in Fig. 2. In the first two or three months, the numerical error caused by insufficient spatial resolution is very large. Except for this point, the numerical model successfully simulated the vertical concentration distribution and its temporal change.

### 3.2. Conditions

One of the purposes of this numerical study is to illustrate first how each factor affects tritiated water transfer in unsaturated soil and its evaporation into the atmosphere, secondly which transport process is dominant, thirdly how the process depends on other processes and factors, and finally if there is possibility of simplifying the model by omitting less significant factors or processes. For this reason, the configuration of the simulations is simplified as follows, in order to make discussions on the results clearer.

The soil layer is assumed to be 1 m deep, unvegetated at the ground surface, horizontally uniform, and uncontaminated by tritium at the beginning. Simulations are carried out for each soil type listed in Table 1. This soil layer is divided uniformly into 200 layers for the first year and non-uniformly into 22 layers for the rest of the simulation period; layer interfaces being at depths of 0.0, 0.01, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95, 1.05 m. The bottom of the soil layer is open for water movement. This means that water can go through the bottom boundary upward or downward according to the hydraulic potential gradient. The bottom soil temperature is kept constant at $9^{\circ}C$ and the specific humidity is kept at the saturation value. The tritium concentration in soil water at the bottom is also assumed constant at $10\,\mathrm{MBq / m^3}$ and the tritium concentration in the gas phase equals the equilibrium value at the temperature and the liquid phase concentration.

Meteorological data observed at Tokai Establishment ($36^{\circ}27^{\prime}\mathrm{N}$, $140^{\circ}36^{\prime}\mathrm{E}$) of Japan Atomic Energy Research Institute at Ibaraki, Japan are used as input data to the model to specify the top boundary conditions. The wind speed observed at a height of $10\,\mathrm{m}$ was used for $|\mathbf{u}_r|$ and the temperature and the specific humidity observed at $1.5\,\mathrm{m}$ were respectively used and designated as $T_{r}$ and $q_{r}$ in Eqs. (7) and (15). Therefore, the bulk coefficients of the air-surface exchange are evaluated for these reference heights with the assumption that the roughness lengths are $z_{0} = 0.23\,\mathrm{mm}$ and $z_{t} = 0.0115\,\mathrm{mm}$. Simulations were carried out with meteorological data available at 1 h intervals from 1980 onward. Although the simulations were conducted for 16 years for each soil type, the following discussions will be mainly on the results obtained for the first 5 years since there is no systematic year-to-year trend in the concentration distribution after this period.

The effective liquid diffusion coefficient in Eq. (18) is calculated with the values of $\hat{D}_{\mathrm{Tw}} = 2.3\times 10^{-9}\,\mathrm{m}^2 /\mathrm{s}$ for the molecular diffusion of HTO in bulk water and $A_{\mathrm{w}} = 0.05\,\mathrm{m}$ for the dispersion coefficient. The molecular gas diffusion coefficient $D_{\mathrm{Ta}} = 2.2\times 10^{-5}\,\mathrm{m}^2 /\mathrm{s}$ is used. The HTO concentration is zero everywhere in the soil at the initial time except for the bottom, where the HTO concentration is assumed to be $10\,\mathrm{MBq / (m^3 water)}$ throughout the simulation period. The atmosphere and precipitation were also assumed to be HTO free.

## 4. Results and discussions

### 4.1. Hydrological conditions

*[Figure 3]*  
*Monthly evaporation and infiltration simulated by the present model for three types of soils during the first 5 years of the simulation period. The top figure depicts the monthly mean temperature and precipitation.*

Monthly mean precipitation and temperature are shown in Fig. 3 for the first 5 years of the simulation period. There are clear seasonal variations in the observed temperature and precipitation. Rainfall occurs mainly in the rainy season from June to July and in the autumn. The winters are characterized by cold and dry weather with clear sky. The annual precipitation and the annual mean temperature, averaged over this first 5 year period, are $1090\,\mathrm{mm / year}$ and $12.9^{\circ}C$. The fourth year is an exceptionally dry year with about two-thirds the precipitation of an ordinary year. The simulation results of the monthly evaporation and infiltration for sand, sandy loam and silt are also shown in Fig. 3. It is clear that the partitioning of the precipitation into evaporation and infiltration largely depends on the soil type or the soil texture. The evaporation from sand is much smaller than that from silt, resulting in a higher infiltration rate of $963\,\mathrm{mm / year}$ for sand as compared with $630\,\mathrm{mm / year}$ for sandy loam and $553\,\mathrm{mm / year}$ for silt. Although the month-to-month variation of the evaporation and infiltration almost follow that of the precipitation for all the soil types, there are some exceptions when the monthly precipitation includes intense rainfalls in relatively short periods as found in Months 10 and 21 of the simulation period. In these months, large portions of the precipitated water were not available for evaporation since the surface soil could not retain the water and this resulted in large infiltration.

### 4.2. Evaporation of HTO

*[Figure 4]*  
*Monthly HTO evaporation into the atmosphere. Simulation results for other soil types are between or just around the results for silt and sandy loam. The curve with open circles is the result for sand with precipitation reduced by a factor of 0.65.*

Monthly evaporation of HTO into the atmosphere from three types of soils is compared in Fig. 4. The difference between soil types is very large: for instance, about three orders of magnitude between sand and silt except for the very early period where evaporation from sand is much larger. Although results are not shown here, the temporal changes and the soil-to-soil difference of the HTO evaporation closely reflect those of concentration. A difference of the same order was found in the surface concentration. These large differences can be attributed to the difference in infiltration. At the beginning, the larger infiltration causes a more enhanced dispersion since there exists a steep vertical gradient of concentration. In the later period when the concentration gradient is no longer as steep, the transport of HTO is dominated by advection due to the macroscopic movement of water. Therefore, the larger the infiltration the lower the HTO evaporation. That the pattern of temporal changes in the HTO evaporation closely follows the precipitation or infiltration pattern shown in Fig. 3 is evidence of this. The decreases of HTO evaporation in the autumnal rainy season in the first 3 years and the increase in the fourth year are good examples.

Additional evidence for this is shown in Fig. 5, which summarizes the annual HTO evaporations and the annual infiltrations for several soil types. According to this result, although there are some small deviations, it is demonstrated that the annual infiltration is one of the key factors determining HTO evaporation. The difference in the infiltration rate from about 500 to $1000\,\mathrm{mm / year}$ causes a decrease in the annual HTO evaporation by more than a thousandfold. However, it would be interesting to see whether the annual HTO evaporation can be determined by annual infiltration only.

*[Figure 5]*  
*Annual evaporation of HTO and infiltration of water simulated for several types of soils.*

An additional simulation was carried out in which the external conditions are identical to those of the sand case, except that the precipitation rate is reduced by a factor of 0.65 to make the annual infiltration nearly equal to that of the sandy-loam case. The result of the HTO evaporation, depicted by open circles in Fig. 4, is somewhat larger than that of the basic sand case but much smaller than that of the sandy-loam case. Therefore, it can be concluded that, although the annual infiltration is one of the key factors, there exist one or more other factors determining HTO evaporation.

### 4.3. Transport processes

To illustrate the relative importance of each elemental process of HTO transport in unsaturated soil, a number of simulations were carried out for several soil types with different sets of elemental processes turned on. In the present study, elemental processes included in the model equations are molecular diffusion in liquid phase, advection in liquid phase, dispersion in liquid phase and molecular diffusion in gas phase.

*[Figure 6]*  
*Monthly HTO evaporation simulated by the model with different combinations of elemental processes of the HTO transport. The 'control' cases were carried out with the original model with all processes turned on. The 'reduced precipitation' case was a simulation with input data of the precipitation reduced by a factor of 0.65.*

Simulation results are shown in Fig. 6 for sand and sandy loam. Contribution of the advection and the dispersion processes can be evaluated by the difference between the open marks (both excluded) and the solid marks (both included). In the simulations without advection and dispersion, the HTO evaporation increased almost monotonously with time although the initial increases are smaller than the control cases, which include all the four processes of the HTO transport. It is thus inferred from the result that the increases of the HTO concentration at the surface and hence the evaporation from the surface in the very early stage are mainly caused by the dispersion. Advection is also dominant in determining the HTO evaporation in the later period as it is the only impeding process to dispersion and diffusion. The consequence of exclusion of the advection and the dispersion is larger in the sand case than in the sandy loam case since the infiltration of water is larger in the sand case.

It is a common question from a practical point of view whether one can ignore the diffusion of HTO in gas phase. If so, a model can be simplified by dropping the equation for HTO vapor or by merging it into the liquid diffusion equation. The consequence of switching off the gas diffusion can be judged by the difference between circles and squares in Fig. 6. The difference is very small in the sandy loam case, but larger in the sand case, especially in dry periods. It is thus concluded that, although the gas diffusion may not be ignored if the climate is dry and soil has sandy texture with a low field capacity, it can be ignored for other cases.

The importance of liquid diffusion is clearly illustrated by the large reduction of the HTO evaporation for both soil types when it is omitted. The reduction is larger in the sandy loam case where the volumetric water content is much higher on average.

### 4.4. Efficiency of diffusion

The above-mentioned conclusion that the gas diffusion cannot be ignored if soil is sandy and dry could be attributed to the availability of free air space for gas diffusion. The efficiency of the liquid phase diffusion can be expressed by $\eta_{\mathrm{w}}\cdot D_{\mathrm{Tw}}\approx 2.3\times 10^{-9}\eta_{\mathrm{w}}$ and that for gas phase diffusion by $\eta_{\mathrm{a}}\cdot \frac{\rho_{\mathrm{a}}}{\rho_{\mathrm{w}}} q_{\mathrm{sat}}(T)\cdot D_{\mathrm{Ta}}\approx 2.2\times 10^{-10}\eta_{\mathrm{a}}$.

Here we have made an assumption for simplicity that the tortuosities of air-filled space and water-filled space are the same although they may naturally differ. As a rule of thumb, the liquid phase diffusion is about ten times more efficient than the gas phase diffusion if the available spaces are similar. To investigate the dependency of the soil properties to the importance of diffusion, the following tables and figures are of importance. Table 2 summarizes the annual mean volumetric fractions of water and air of the 1-m-deep soil layer for the fifth year. Fig. 7 shows the annual mean HTO concentration profiles during the fifth year for the soils listed in Table 2. These results, and also referring to Fig. 5, show that soils with finer texture have higher water content with more space for liquid phase diffusion, and hence larger HTO evaporation from the ground surface (or higher concentration). In addition, this feature is negatively correlated to the annual amount of infiltration as shown in Table 2 because higher water content results in enhanced surface evaporation of water. It can therefore be concluded that the soil texture affects the HTO transport in an unsaturated soil by determining not only the infiltration (advection and dispersion processes) but also the volumetric fractions of water-filled and air-filled pores (diffusion in liquid and gas phases).

**Table 2**  
Annual mean volumetric fractions of water and air and annual infiltration of water simulated for the fifth year.

| Soil Type   | Volumetric fraction Water | Volumetric fraction Air | Infiltration (mm/year) |
|:------------|:--------------------------|:------------------------|:-----------------------|
| Silt        | 0.317                     | 0.159                   | 756                    |
| Loam        | 0.287                     | 0.152                   | 784                    |
| Sandy loam  | 0.266                     | 0.168                   | 846                    |
| Loamy sand  | 0.227                     | 0.194                   | 945                    |
| Sand        | 0.123                     | 0.216                   | 1164                   |

*[Figure 7]*  
*Vertical profile of the annual mean concentration of HTO for the fifth year.*

### 4.5. Effect of time averaging

In discussing the long term evolution of surface concentration or evaporation of HTO, it is important to notice the fact that the HTO concentration and the HTO evaporation vary very largely even in a year as shown in the previous figures. This implies that the evaporation of HTO in a year, for example, is not evenly contributed from each month or each week of the year. Relatively short but high-concentration periods could be main contributors to annual HTO evaporation or annual mean HTO concentration. For example, the maximum monthly evaporation of the second year from Month 13 to 24 is about two orders of magnitude greater than the minimum of this year (Fig. 4). Temporal variations in the concentration and the evaporation of HTO during the fifth year are shown in Fig. 8. The amplitudes of both the concentration and evaporation are very large. The annual mean HTO concentration would virtually be determined by the concentrations in the periods of roughly the first 60 days and from day 210 to 270. The same can be said for the annual HTO evaporation.

*[Figure 8]*  
*Daily mean HTO concentration in the surface soil water and daily HTO evaporation (a), and daily evaporation of water (b) calculated by the model for sand (year 5).*

To quantitatively test the effect of using time-averaged hydrological and meteorological data, additional simulations were carried out, in which daily, weekly and monthly averaged data were used for the volumetric water content, the soil water flux, the soil temperature, the precipitation, the wind speed, the air temperature and the humidity to solve the governing equations for the HTO concentrations in the soil water and the soil air. The other simulation conditions were identical to the original simulations, in which, in contrast to these additional simulations, hourly values of the above-mentioned data items were used. Simulation results of the annual evaporation of HTO are summarized in Table 3. Substantial reduction in the calculated HTO evaporation by using averaged hydrological and meteorological input data can be seen for all of the three types of soils in addition to the large variation due to the difference of soil type. This implies that fluctuations in the soil water flux and the soil water content on small time scales might have large influence on the HTO transport in soil. Therefore, to evaluate even an annual mean concentration or an annual evaporation rate, it is insufficient to take account of an annual or monthly mean structure of the meteorology and hydrology.

**Table 3**  
Annual evaporation of HTO ($\mathrm{Bq\,m^{-2}\,year^{-1}}$) calculated with different time-averaged, meteorological and hydrological data.

| Averaging period | Sand  | Sandy loam | Silt  |
|:-----------------|:------|:-----------|:------|
| Hour (original)  | 0.361 | 114        | 1880  |
| Day              | 0.240 | 83         | 910   |
| Week             | 0.140 | 58         | 600   |
| Month            | 0.071 | 33         | 290   |

### 4.6. Evaporation efficiency

The evaporation of HTO from the ground surface into the atmosphere depends not only on the HTO concentration at the ground surface but also on the meteorological conditions as modeled in Eq. (21). Variations in soil properties and soil moisture condition are also one of the key factors affecting the HTO evaporation. It would be of practical interest to see how the efficiency of the HTO evaporation depends on these factors. Here, we define the HTO evaporation coefficient $C_{\mathrm{HTO}}$ as the ratio of the amount of HTO evaporated to the mean HTO concentration in the soil water at the ground surface,

$$
C_{\mathrm{HTO}} = e_0 / \chi_{\mathrm{HTO},0}
$$

This definition is very similar to that of a deposition velocity. Since the present simulations were carried out with the assumption that $\chi_{\mathrm{r}} = 0$, $C_{\mathrm{HTO}}$ can be related directly to the bulk exchange coefficient $c_{\mathrm{E0}}|\mathbf{u}_{\mathrm{r}}|$ in Eq. (21). However, $C_{\mathrm{HTO}}$ accounts also for the availability of HTO vapor at the ground surface, while the bulk exchange coefficient accounts only for atmospheric conditions.

*[Figure 9]*  
*Annual variation in the daily mean, maximum and minimum of the HTO evaporation coefficient for sand during the fifth year.*

Annual variation in $C_{\mathrm{HTO}}$ calculated for sand is shown in Fig. 9, in which daily maxima and minima evaluated from hourly mean concentration and evaporation are depicted together with the daily averages calculated from the daily mean concentration and evaporation. The amplitude of the diurnal variation of the coefficient is very large. Although figures are not presented here, the maximum coefficients are found in the daytime when the atmospheric stratification is unstable while the minima occur in night time. The day-to-day variations as well as the seasonal trend are also very large. The pattern of the annual trend is very similar to that of water evaporation shown in Fig. 8(b). These are mainly caused by fluctuations in the atmospheric turbulence and the availability of HTO vapor at the ground surface, the latter being strongly affected by the ground surface temperature and wetness in addition to the HTO concentration in the soil water at the ground surface. According to these results, the HTO evaporation from the ground surface may vary by one order of magnitude or more depending on the time of the day and the day of the year even if the surface concentration is unchanged. The dependency of $C_{\mathrm{HTO}}$ on soil type is shown in Table 4. A large difference can be seen between sand and other soils while the difference is small between soils other than sand.

**Table 4**  
Evaporation coefficient $C_{\mathrm{HTO}}$ of HTO for a variety of soil types. The values of $C_{\mathrm{HTO}}$ in this table are averages of all hourly values of the coefficient during the first 5 years of the simulation period. The daily range is a range between the daily maximum and minimum averaged over a 5 year period, while the annual range is the amplitude of the annual variation in daily mean $C_{\mathrm{HTO}}$.

| Soil Type        | C<sub>HTO</sub> ($10^{-7}$ m/s) | Daily range ($10^{-7}$ m/s) | Annual range ($10^{-7}$ m/s) |
|:-----------------|:--------------------------------|:----------------------------|:-----------------------------|
| Sand             | 0.072                           | 0.023–0.17                  | 0.010–0.40                   |
| Loamy sand       | 0.22                            | 0.046–0.57                  | 0.025–1.10                   |
| Sandy loam       | 0.30                            | 0.054–2.11                  | 0.048–1.29                   |
| Silt             | 0.36                            | 0.061–1.49                  | 0.052–1.38                   |
| Loam             | 0.34                            | 0.059–1.98                  | 0.051–1.34                   |
| Clay loam        | 0.34                            | 0.063–2.97                  | 0.052–1.38                   |
| Sandy clay       | 0.32                            | 0.060–1.64                  | 0.051–1.33                   |
| Silty clay       | 0.34                            | 0.064–2.51                  | 0.052–1.38                   |
| Clay             | 0.35                            | 0.063–2.22                  | 0.053–1.38                   |

## 5. Conclusions

A numerical model for simulating the soil-atmosphere exchange of heat, water and HTO was developed. The meteorological and hydrological parts of this model had been tested in another study. In the present study, the numerical validity of the HTO part was successfully tested by comparing the simulation results with analytical solutions. This model was applied to an idealized HTO contamination scenario, in which the transport of HTO through an unsaturated surface soil layer above a constantly contaminated layer and the evaporation of HTO from the ground surface were the objectives of the simulations.

A summary of the discussions in the previous section on process interdependencies is schematically shown in Fig. 10. In the present model, the HTO transport processes are expressed in the form of dispersion, advection, liquid diffusion and gas diffusion. A long-term trend of the concentration distribution is primarily maintained by the balance between the advection and the liquid diffusion while a short-term variation by the balance between the advection and the dispersion. The contribution of gas diffusion is relatively small and can be ignored to simplify models except when the soil is dry. There are many meteorological and hydrological factors affecting these transport processes and eventually the HTO evaporation and concentration. The present study quantitatively pictured the interdependencies between them as discussed in the previous section. Infiltration and water content directly and largely affect the advection process and the liquid diffusion process, respectively. The consequences of increased precipitation are very large and simple while those for other meteorological factors are rather indirect but substantial. For example, increases in wind speed and temperature and reduction in atmospheric stability (higher turbulence) cause an increase in water evaporation. This effect directly and quickly enhances the HTO evaporation. This also enhances the HTO evaporation slowly and largely by reducing the infiltration and hence the advection. Although the negative effect through liquid diffusion is also slow and substantial, it is smaller than the positive effect through advection.

*[Figure 10]*  
*Schematic diagram of the interdependency of the HTO transport processes in unsaturated surface soil. The thickness of the arrows indicates their relative importance. This diagram is valid for a contamination at the bottom of the objective soil layer. A different diagram can be drawn for contamination at the surface.*

The validity of using time-averaged meteorological and hydrological data for the evaluation of the HTO transport in an unsaturated soil layer was evaluated. It was found that the use of data averaged over longer periods reduced the simulated surface concentration of HTO and its evaporation into the atmosphere. It was also pointed out that the annual evaporation and the annual mean surface concentration were mainly contributed by rather short periods of high concentration caused by meteorological and hydrological conditions. Although these aspects are important for the precise understanding and evaluation of the HTO transport, they are still less important than the proper consideration of the transport processes (Fig. 6) or the determination of soil properties (Fig. 5).

## References

1. Al Nakshabandi, G., Kohnke, H., 1965. Thermal conductivity and diffusivity of soils as related to moisture tension and other physical properties. Agricultural Meteorology 2, 271-279.
2. Brutsaert, W.H., 1982. Evaporation into the Atmosphere. D. Reidel Publishing Co, Dordrecht.
3. Bunnenberg, C., Täschner, M., Ogram, G.L., 1990. Determination of key processes and quantification of key parameters for tritium environmental transport models. Study-Contract No. 327/88-10/FU-D/NET, 190 pp.
4. Clapp, R., Hornberger, G., 1978. Empirical equations for some soil hydraulic properties. Water Resource Research 14, 601-604.
5. Cosby, B.J., Hornberger, G.M., Clapp, R.B., Ginn, T.R., 1984. A statistical exploration of the relationship of soil moisture characteristics to the physical properties of soils. Water Resource Research 20, 628-690.
6. Dunstall, T.G., Ogram, G.L., 1991. Diffusion and biological oxidation as component processes regulating the deposition of tritiated hydrogen to soils. Ontario Hydro Research Division Report 90-235-K.
7. Jones, H.G., 1992. Plants and Microclimate, second ed. Cambridge University Press, Cambridge.
8. Kondo, J., Saigusa, N., 1994. Modeling the evaporation from bare soil with a formula for vaporization in the soil pores. Journal of Meteorological Society of Japan 72 (3), 413-421.
9. Kondo, J., Xu, J., 1997. Seasonal variations in the heat and water balance for nonvegetated surfaces. Journal of Applied Meteorology 36 (12), 1676-1695.
10. McCumber, M.C., Pielke, R.A., 1981. Simulation of the effects of surface fluxes of heat and moisture in a mesoscale numerical model 1 soil layer. Journal of Geophysical Research 86 (C10), 9929-9938.
11. Murata, M., Noguchi, H., 1992. Estimation of HT gas diffusion coefficient and conversion rate constant of HT gas to HTO in intact soil. Journal of Atomic Energy Society of Japan 34 (12), 149-152, in Japanese.
12. Nagai, H., Yamazawa, H., 1999. Development of one-dimensional atmosphere-soil-vegetation model. JAERI-Data/Code 99-024, in Japanese.
13. Nagai, H., 2001. Atmosphere-soil-vegetation model: model description, validation with observation data, and sensitivity analysis. Journal of Applied Meteorology, submitted for publication.
14. Ogram, G.L., 1982. The oxidation of molecular tritium released to the atmosphere. Ontario Hydro Research Division Report 82-449-K.
15. Okada, S., Momoshima, N., 1993. Overview of tritium: characteristics, sources and problems. Health Physics 65 (6), 595-609.
16. Peterman, B.F., Jhonson, J.R., McElroy, R.G.C., 1985. HT/HTO conversion in mammals. Fusion Technology 8 (8), 2557-2563.
17. Pielke, R.A., 1984. Mesoscale Meteorological Modeling. Academic Press, London.
18. Stull, R.B., 1988. An Introduction to Boundary Layer Meteorology. Kluwer Academic Publishers, Dordrecht.
19. Tindall, J.A., Kunkel, J.R., Anderson, D.E., 1999. Unsaturated Zone Hydrology for Scientists and Engineers. Prentice-Hall.
20. Van Genuchten, M.Th., 1980. A closed-form equation for predicting the hydraulic conductivity of unsaturated soils. Soil Science Society of America Journal 44, 892-898.
21. Yamazawa, H., Nagai, H., 1997. Development of one-dimensional atmosphere-bare soil model. JAERI-Data/Code 97-041, in Japanese.
22. Yamazawa, H., 1996. Development of a numerical solution method for advection terms and its application to the atmospheric dynamic model, PHYSIC. Journal of Nuclear Sciences and Technologies 33 (1), 69-77.