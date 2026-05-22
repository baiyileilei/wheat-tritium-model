# A Terrestrial Ecosystem Model (SOLVEG) Coupled with Atmospheric Gas and Aerosol Exchange Processes

**Genki KATATA and Masakazu OTA**

*Environment and Radiation Sciences Division*
*Nuclear Science and Engineering Center*
*Sector of Nuclear Science Research*
*Japan Atomic Energy Agency*
*Tokai-mura, Naka-gun, Ibaraki-ken*

(Received November 10, 2016)

## Abstract

In order to predict the impact of atmospheric pollutants (gases and aerosols) to the terrestrial ecosystem, new schemes for calculating the processes of dry deposition of gases and aerosols, and water and carbon cycles in terrestrial ecosystems were implemented in the one-dimensional atmosphere-SOiL-VEGetation model, SOLVEG. We made performance tests at various vegetation areas to validate the newly developed schemes. In this report, the detail in each modeled process is described with an instruction how to use the modified SOLVEG. The framework of "terrestrial ecosystem model" was developed for investigation of a change in water, energy, and carbon cycles associated with global warming and air pollution and its impact on terrestrial ecosystems.

**Keywords:** Land Surface Model, Atmospheric Deposition, Gas, Aerosol, Ecosystem Modeling

---

## 1. Introduction

Over recent decades, it is of great concern over negative impacts of climate changes and human activities on earth's terrestrial ecosystems. Atmospheric deposition and emission (i.e., atmospheric exchange) of anthropogenic materials are known as the disturbance that causes various environmental issues such as air pollution, eutrophication, acidification, and even biological diversity. However, atmospheric exchange rate is hard to estimate properly because it strongly depends on complex processes related to complicated biogeochemical interactions between atmosphere and terrestrial ecosystems, i.e., energy, water, and carbon cycles. In this context, a detailed terrestrial ecosystem model is useful for understanding above interactions for various types of the land surface.

Since last decade, we have developed the one-dimensional model for atmosphere-SOIL-VEGtation interaction SOLVEG (Nagai 2004$^{1)}$; Katata 2009$^{2)}$). The model was validated with field datasets over various land types: semi-arid deserts (Katata et al 2007$^{3)}$), croplands (Nagai 2002$^{4)}$, 2003$^{5)}$; Katata et al 2007$^{3)}$), rice paddy field (Katata et al 2013$^{6)}$), temperate grasslands (Nagai 2005$^{7)}$; Ota et al 2013$^{8)}$), and forests (Nagai 2003$^{5)}$; Katata et al 2008$^{9)}$, 2011$^{10)}$, 2014$^{11)}$). In the above studies, the authors primarily focused on modeling of atmospheric deposition of gases and aerosols (Katata et al. 2011$^{10)}$, 2013$^{6)}$, and 2014$^{11)}$). Further modifications in biogeochemical interactions were also made in the model (Ota et al 2013$^{8)}$; Desai et al., 2016$^{12)}$). However, a full description of model improvement in independent studies is still not available elsewhere.

Thus, the objective of the present report is to summarize new schemes incorporated in SOLVEG extended to the so-called terrestrial ecosystem model.

## 2. Model overview

The SOLVEG model consists of one-dimensional multi-layer sub-models for atmosphere, soil, and vegetation with a radiation transfer scheme for calculating the transmission of solar and long-wave radiation fluxes in the canopy layer. The variables from the bottom of soil layer to the top of atmospheric layer were integrated numerically using an implicit finite difference method and Gaussian elimination method. A detailed description of basic equations and model framework is found in Nagai (2004)$^{1)}$ and Katata (2009)$^{2)}$.

*[Figure 1-1]* Schematic illustration of newly modelled processes in the atmosphere-soil-vegetation system represented in SOLVEG after Katata (2009)$^{2)}$.

## 3. Atmospheric gas and aerosol exchange processes

### 3.1. Basic equation of atmospheric sub-model

The atmosphere sub-model calculates variables at each atmospheric layer by numerically solving one-dimensional diffusion equations for the horizontal wind speed components, potential temperature, specific humidity, liquid water content of fog, turbulent kinetic energy and length scale, and gas and particle concentrations. By using $\phi$ for these variables, one-dimensional diffusion equations are described in the same form as:

$$
\frac{\partial\phi}{\partial t} = \frac{\partial}{\partial z}\left(K_z\frac{\partial\phi}{\partial z}\right) + F_{\phi} \tag{3-1}
$$

where $t$ is the time [s], $z$ the height in the atmosphere [m], $K_z$ the vertical turbulence diffusivity $[\mathrm{m}^2 \mathrm{s}^{-1}]$ calculated by the second-order turbulence closure model. The last term $F_{\phi}$ is a forcing term which includes the exchange between the vegetation and canopy air as the volume source/sink for each atmospheric variable. The top boundary conditions are provided from input data. The soil surface boundary conditions are the momentum, heat, and water vapor fluxes calculated using bulk transfer equations of wind speed, potential temperature, and specific humidity at the lowest air layer and the soil surface temperature and specific humidity, which are determined with the soil sub-model. Temporal changes in vertical profiles of typical inorganic gas (ozone, NO, $\mathrm{NO}_2$, $\mathrm{HNO}_3$, $\mathrm{HCl}$, $\mathrm{SO}_2$, and $\mathrm{NH}_3$) and aerosol mass concentrations are also predicted by solving Eq. (3-1).

### 3.2. Dry deposition of insoluble gases

Atmospheric gases are vertically transported by turbulent eddy diffusion and mainly absorbed by plants due to stomata uptake at plants' leaves. When the plant's leaves are not wet, the source/sink term for water vapor, $F_q$, is represented as the aggregation of the evaporation rate of leaf surface water, $E_d$, and the transpiration rate, $E_s$, at each canopy layer as (Nagai 2004$^{1)}$):

$$
\begin{aligned}
F_q &= a(E_d + E_s) / \rho \\
E_s &= \rho \frac{r_d}{R}[q_{sa}(T_c) - q_a] \\
E_d &= \rho \frac{r_s}{R}[q_{sa}(T_c) - q_a]
\end{aligned} \tag{3-2}
$$

where $r_d$, $r_s$ are the resistances $[\mathrm{m}\,\mathrm{s}^{-1}]$ of leaf boundary layer and stomata, respectively, $R = r_d r_s + r_d r_d + r_s r_d$, $q_{sa}(T_c)$ the saturated specific humidity $[\mathrm{kg}\,\mathrm{kg}^{-1}]$ for $T_c$ [K], and $q_a$ the specific humidity of air $[\mathrm{kg}\,\mathrm{kg}^{-1}]$. Note that the resistance $(r_b)$ and the sum of $r_d$ and $r_s$ are in series, but $r_d$ and $r_s$ are in parallel, because evaporation of the leaf surface water and transpiration occur independently from the leaf surface water and the stomata, respectively.

A diagram of trace gas exchanges between the atmosphere and the land surface is represented based on the analogy of evaporation rate as Eqs. (3-2) and (3-4). The gas deposition rate at each canopy layer, $F_g$ $[\mu\mathrm{g}\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}]$, is modeled using the stomatal resistance $(r_s)$ calculated and quasi-laminar resistance over the leaves $(r_a)$ as (Katata et al. 2011$^{10)}$):

$$
F_g = a\left(\frac{D_g}{D_w}\right)\frac{1}{r_s + r_a}(c_{ga} - c_{gs}) \tag{3-5}
$$

where $D_g$ and $D_w$ are the diffusivity $[\mathrm{m}^2\,\mathrm{s}^{-1}]$ of trace gas and water vapor, and $c_{ga}$ and $c_{gs}$ the gas concentration $[\mu\mathrm{g}\,\mathrm{m}^{-3}]$ around the leaf surface and within the stomata, respectively.

For relatively insoluble gas species such as ozone, and nitrogen monoxide (NO) and dioxide ($\mathrm{NO}_2$), the gas concentration in sub-stomatal cavity is simply assumed to be zero, i.e., $c_{gs} = 0$ (Fig. 3-1a). This assumption has been validated by comparing calculations with observations from datasets for ozone deposition onto maize crops and broad-leaved forest canopies$^{10)}$.

In addition to the above assumption of $c_{gs} = 0$, the stomatal resistance of $r_s$ is set to be zero for highly reactive and water-soluble gas species of nitric acid vapor ($\mathrm{HNO}_3$) and HCl (Fig. 3-1b), i.e., perfect absorption by plant canopies. This assumption has been reported by a number of measurements (e.g., Huebert and Robert 1985$^{13)}$).

### 3.3. Water-soluble gas exchanges over wet canopy

Some water-soluble gas species such as sulfur dioxide ($\mathrm{SO}_2$) and ammonia ($\mathrm{NH}_3$) have also other transfer pathways to the vegetative surfaces: for example, the cuticle and wetted surfaces of leaves (especially for water-soluble compounds), the branches, the trunks, and the soil exposed to atmosphere. All of these pathways, which are often summarized as the so-called non-stomatal deposition, have become recognized as a sink of gases at the terrestrial surface.

When the plant nitrogen status is high at the fertilized surface, $\mathrm{NH}_3$ deposition often occurs onto the wet canopy at night, but there are emissions during the daytime due to evaporation from the stomata under warm conditions. In such situations, the original model underestimated $\mathrm{NH}_3$ flux over a wet canopy. Moreover, the assumption of $c_{gs} = 0$ in Eq. (3-5) is not valid for $\mathrm{NH}_3$ in many cases because $\mathrm{NH}_3$ has emission potentials at the foliage.

Thus, the water vapor flux over a leaf surface in SOLVEG was used to calculate $\mathrm{NH}_3$ and $\mathrm{SO}_2$ fluxes for each canopy layer as shown in Fig. 3-1c (Katata et al. 2013$^{6)}$). Eqs. (3-2) and (3-3) are based on the assumption that water vapor both in the stomata and just above the leaf surface water (i.e., compensation points) are equal to the saturated value $(q_{sat})$ for a given leaf temperature $(T_c)$. Using the compensation points for other trace gases in the sub-stomatal cavity $(\chi_s [\mu\mathrm{g}\,\mathrm{m}^{-3}])$ and above the leaf water surface $(\chi_d [\mu\mathrm{g}\,\mathrm{m}^{-3}])$ in place of $q_{sat}$, Eqs. (3-2) and (3-3) can be generalized for bi-directional gas exchange fluxes over stomata $(F_{gs} [\mu\mathrm{g}\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}])$ and leaf water surfaces $(F_{gd} [\mu\mathrm{g}\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}])$ as:

$$
F_{gs} = a\left(\frac{D_g}{D_w}\right)R^{-1}\left[(r_b + r_d)\chi_s - r_b\chi_d - r_d\chi_a\right] \tag{3-6}
$$

$$
F_{gd} = a\left(\frac{D_g}{D_w}\right)R^{-1}\left[(r_b + r_s)\chi_d - r_b\chi_s - r_s\chi_a\right] \tag{3-7}
$$

where $\chi_a$ is the ambient gas concentration $[\mu\mathrm{g}\,\mathrm{m}^{-3}]$ in the canopy layer. The above equations are similar in concept to existing bi-directional $\mathrm{NH}_3$ exchange models (e.g., Zhang et al. 2010$^{14)}$). The total gas exchange flux over the leaves can be calculated as the sum of $F_{gs}$ and $F_{gd}$ for all canopy layers.

The bi-directional flux of $\mathrm{NH}_3$ is calculated using Eqs. (15) and (16) and the calculated value of $\chi_s$ based on thermodynamic equilibrium between $\mathrm{NH}_3$ in the liquid and gas phases:

$$
\chi_s = \left(\frac{161500}{T_c}\right)\exp\left(-\frac{10378}{T_c}\right)\Gamma_s \tag{3-8}
$$

where $\chi_s$ is the stomatal emission potential (also known as the apoplastic ratio) at 1013 hPa, as:

$$
\Gamma_s = \frac{[\mathrm{NH}_4^{+}]_s}{[\mathrm{H}^{+}]_s} \tag{3-9}
$$

where $[\mathrm{NH}_4^{+}]_s$ and $[\mathrm{H}^{+}]_s$ are the $\mathrm{NH}_4^{+}$ and $\mathrm{H}^{+}$ concentrations $[\mathrm{mol}\,\mathrm{L}^{-1}]$ in the apoplastic fluid, respectively. $[\mathrm{H}^{+}]_s$ is defined as $10^{-\mathrm{pH}}$, where the pH of the apoplastic fluid is given at 1013 hPa.

In these calculations, when the canopy is wet with microscopic water layers that appear under high relative humidity condition $(\mathrm{RH} > 60\%)$, water-soluble gases can also be emitted from wet canopies through evaporation. For simplification, some models have assumed that the $\mathrm{NH}_3$ concentration at the leaf surface is zero for transfer between the canopy air space and the leaf surface. In the modified SOLVEG model, the $\mathrm{NH}_3$ concentration at the leaf surface water $(\chi_d)$ was calculated by assuming Henry's Law and dissociation equilibrium with the atmospheric concentration of $\mathrm{NH}_3$ at each canopy layer. To calculate the exchange flux of $\mathrm{NH}_3$ and $\mathrm{SO}_2$ over the wet canopy, the following formula for the evaporation (cuticular) resistance $(r_d)$ was applied:

$$
r_d = 31.5\,AR^{-1}\exp[a(100 - RH)] \tag{3-10}
$$

where $AR$ is the ratio of total acid/$\mathrm{NH}_3$, represented as $(2[\mathrm{SO}_2] + [\mathrm{HNO}_3] + [\mathrm{HCl}]) / [\mathrm{NH}_3]$ and $RH$ the relative humidity $[\%]$ at each atmospheric layer calculated using the diffusion equation for specific humidity (Nagai 2004$^{1)}$). The value of $AR$ is calculated from calculations of gaseous inorganic concentration at each atmospheric layer. Since the affinity of $\mathrm{SO}_2$ for the leaf surface was approximately twice that of $\mathrm{NH}_3$ (van Hove et al. 1989$^{15)}$), a half value of $r_d$ calculated by (3-10) is applied to $\mathrm{SO}_2$ deposition.

### 3.4. Dry deposition of aerosols

The atmosphere and vegetation sub-models include the module for the calculation of fog deposition onto the leaves based on the processes of inertial impaction and gravitational settling of particles at each vegetation layer (Katata 2009$^{2)}$). In the present study, a novel scheme of the collection rates due to Brownian diffusion and interception, which can affect fine particles typically smaller than $0.1\,\mu\mathrm{m}$ in diameter, is developed (Katata et al. 2011$^{10)}$). Both processes are formulated based on semi-empirical equations obtained by wind-tunnel studies for packed fibres of a filter.

The particle deposition rate, $F_p [\mu\mathrm{g}\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}]$, in each canopy layer is represented as:

$$
F_p = aE_p \tag{3-11}
$$

$$
E_p = \epsilon F_p|\mathbf{u}|c_p \tag{3-12}
$$

where $E_p$ is the capture of particles by leaves $[\mu\mathrm{g}\,\mathrm{m}^{-3}\,\mathrm{s}^{-1}]$, $\epsilon$ the total capture efficiency of the plants' leaves for particles, $F_p$ the shielding coefficient for particles in horizontal direction, $|\mathbf{u}|$ the horizontal wind speed $[\mathrm{m}\,\mathrm{s}^{-1}]$ at each canopy layer, and $c_p$ the mass concentration of aerosol particles $[\mu\mathrm{g}\,\mathrm{m}^{-3}]$.

Assuming that each collection mechanism acts in series, the total capture efficiency $\epsilon$ can be expressed as:

$$
\epsilon = 1 - \prod_{x}(1 - \epsilon_x) \tag{3-13}
$$

where $x$ is the collection mechanism of inertial impaction, gravitational settling, Brownian diffusion, and interception. Since the formulations of $\epsilon$ for inertial impaction $\epsilon_{imp}$ and gravitational settling $\epsilon_{gr}$ have been described in Katata (2009)$^{2)}$, only collection efficiencies due to Brownian diffusion and interception are described below.

Fine particles smaller than approximately $0.1\,\mu\mathrm{m}$ diffuse toward the foliar surface (Brownian diffusion), when moving along the streamline around the leaves under forced convection. The collection efficiency due to Brownian diffusion, $\epsilon_{df}$, is described by the following formula:

$$
\epsilon_{df} = 2.7 Pe^{-2/3} \tag{3-14}
$$

$$
Pe = \frac{|\mathbf{u}|d_{leaf}}{D_B(d_p)} \tag{3-15}
$$

where $Pe$ is the Peclet number, which is the product of Schmidt $(Sc)$ and Reynolds number $(Re)$, $d_{leaf}$ the characteristic length of vegetation element $[\mathrm{m}]$ (e.g., needle diameter for coniferous forest), and $D_B(d_p)$ the Brownian diffusion coefficient $[\mathrm{m}^2\,\mathrm{s}^{-1}]$ as a function of particle diameter $d_p$ [μm]. The value of 2.7 in Eq. (3-14) is a number determined by experimental measurements of filter efficiencies. Equation (3-14) includes both effects of convection $(Re)$ and particle diffusion $(Sc)$ and is physically more reasonable than the prior parameterizations using only $Sc$ in the commonly used model such as Zhang et al. (2001)$^{16)}$.

When small particles perfectly follow a streamline that reaches within one particle radius of the foliar surface, the particle hits the leaf and is captured because of its finite size (interception). The collection efficiency due to interception, $\epsilon_{in}$, is expressed as:

$$
\epsilon_{in} = (1 + R_i) - (1 + R_i)^{-1} \tag{3-16}
$$

$$
R_i = \frac{d_p}{d_{leaf}} \tag{3-17}
$$

where $R_i$ and $d_p$ are the dimensionless parameter of interception and the (wet) particle diameter $[\mathrm{m}]$ of the bin, respectively. For broad-leaved trees (planar obstacles), the parameter $R$ is modified based on an analytical formulation of the collection velocity for a Dirac distribution of the leaf width as:

$$
R_i = \frac{d_p}{d_{leaf}}\left(2 + \ln\frac{4d_{leaf}}{d_p}\right) \tag{3-18}
$$

### 3.5. Aerosol hygroscopic growth

Hygroscopic growth is significant in aerosols containing water-soluble compounds such as ammonium sulfate under humid conditions. The degree of water uptake by aerosols is typically represented by the hygroscopic growth factor, $G_f$, defined as the ratio between the humidified and dry particle diameters. In SOLVEG, the widely used $\kappa$-Köhler theory (Petters and Kreidenweis 2007$^{17)}$) was employed to calculate the water uptake of aerosols in the atmosphere, i.e., the wet diameter of particles in each bin, $d_p$. The theory is convenient as it requires only one parameter $\kappa$ to represent the hygroscopicity of a single particle as internal mixtures of inorganics and organics. According to Petters and Kreidenweis (2007)$^{17)}$, the typical experimental values of $\kappa$ for both ammonium sulfate and ammonium nitrate are 0.6, the sodium chloride and sodium bisulfate values are 1.0 and the values for hygroscopic organic compounds such as organic acids are in the range of 0.1-0.2. Using the above $\kappa$ values and available data for inorganic compounds, the hygroscopicity of a multi-component particle was calculated by a volume-weight average of $\kappa$ for each compound.

For larger particles $(d_p > 1\,\mu\mathrm{m})$, the mass transfer of water vapor during particle growth restricts hygroscopic growth because the particles require several minutes to several ten minutes to reach equilibrium, especially under near-saturated conditions. Mass transfer of water vapor to the aerosol surface is dynamically calculated for each time step in SOLVEG as follows (Katata et al. 2014$^{11)}$):

$$
\frac{dL_{a,l}}{dt} = \frac{\pi}{4}\alpha\bar{c}d_p^2 f(d_p,\alpha) n \rho (q - q_{eq}) \tag{3-19}
$$

where $L_{a}$ and $n$ are the total aerosol water content $[\mathrm{kg}\,\mathrm{m}^{-3}]$ and the number concentration $[\mathrm{m}^{-3}]$ of each bin, $q$ $[\mathrm{kg}\,\mathrm{kg}^{-1}]$ is the water vapor mixing ratio in the canopy layer, $\bar{c}$ $[\mathrm{m}\,\mathrm{s}^{-1}]$ is the molecular speed of the water vapor, $\alpha$ is the mass accommodation coefficient, which is set to unity, and $q_{eq}$ $[\mathrm{kg}\,\mathrm{kg}^{-1}]$ and $\kappa$ are the equilibrium water vapor mixing ratio for the aerosol surface of the bin and the hygroscopicity of particles, as determined by the $\kappa$-Köhler theory. The correction factor, $f$, for the transition regime is taken from Fuchs and Sutugin (1971)$^{18)}$. For simplicity, we assumed a single log-normal function for aerosol size distributions without size dependencies of the aerosol properties, i.e., $\kappa$ and the volume fraction of inorganic compounds $(f_{io})$, is unchanged with particle size. The procedure used to determine the number concentration of each bin, $n$, and to integrate the mass transfer equation, Eq. (3-19), was calculated as follows. First, the total aerosol mass was calculated from inorganic components measured by filter pack, the above volume fractions of the total inorganics, and an assumed particle density, $1.8\,\mathrm{kg}\,\mathrm{m}^{-3}$. Then, $n$ in Eq. (3-19) was calculated for each bin and was integrated for a given log-normal size distribution with given parameters of the number-equivalent geometric mean dry diameter $(d_{gn} [\mu\mathrm{m}])$ and the geometric standard deviation $(\sigma_g)$.

In Eq. (3-19), the mass transfer of heat is not calculated. The water vapor mixing ratio, $q$, is assumed to be constant during particle growth and shrinkage due to water uptake. This assumption is reasonable because the maximum calculated total aerosol water mixing ratio is less than $1\%$ of $q$.

It should be noted that the $\kappa$-Köhler theory does not take into account the water hysteresis effect, i.e., the efflorescence and deliquescence of aerosols. The authors investigate the impact of this effect via test calculations of the aerosol thermodynamic equilibrium model ISORROPIA2 (Fountoukis and Nenes 2007$^{19)}$) at Japanese broad-leaved forest in summertime$^{11)}$. The results showed that the aerosol water content is greater than zero throughout the simulation period; i.e., the RH was always larger than the mutual deliquescence relative humidity (MDRH) of the aerosols. Thus, the scheme based on the $\kappa$-Köhler theory is applicable to typical humid temperate climate.

Using the total liquid water content, $L_a$ $[\mathrm{kg}\,\mathrm{m}^{-3}]$, the growth factor for bin, $G_f$, can be calculated as:

$$
G_f = \frac{d_p}{d_{p,dry}} = \frac{\left[\frac{6L_a}{\pi\rho_w} + (d_{p,dry})^3\right]^{1/3}}{d_{p,dry}} \tag{3-20}
$$

where $d_{p,dry}$ is the dry diameter of the particles $[\mathrm{m}]$ and $\rho_w$ is the density of water $[\mathrm{kg}\,\mathrm{m}^{-3}]$. Finally, the mean growth factor, $G_{f,ave}$, is calculated by volume-averaging $G_f$ in Eq. (3-20) for all bins.

*[Figure 3-2]* Size-resolved dry deposition velocity calculated by the model $(d_{gn}=0.2\,\mu\mathrm{m}, \sigma_g=1.6)$ with $(\kappa=0.6$, red solid lines) and without particle growth (black solid lines) over the Japanese broad-leaved forest (after Katata et al. 2014$^{11)}$). Observational data from the literature for coniferous (open plots) and broad-leaved forests (closed plots) are plotted.

## 4. Other processes for terrestrial ecosystem modeling

### 4.1. Snow accumulation and melting

The ice phase processes in snow and soil layers have an important role in water cycle in the terrestrial ecosystem under cold environment. To simulate these processes, the multi-layer snow module is incorporated into the model. Most of variables in the following equations are based on either the Community Land Model, CLM (Oleson et al. 2010$^{20)}$) or SNTHERM (Jordan 1991$^{21)}$), while the model is unique in including the gravitational and capillary liquid water flows in unsaturated snow based on van Genuchten's concept (c.f., Hirashima et al 2010$^{22)}$).

The temporal change in snow temperature $T_{sn}$ [K] is expressed by the heat conduction equation based on Yamazaki (2001)$^{23)}$ as:

$$
C_{sn}\rho_{sn}\frac{\partial T_{sn}}{\partial t} = \frac{\partial}{\partial z}\left(\lambda_{sn}\frac{\partial T_{sn}}{\partial z}\right) - \frac{\partial I_n}{\partial z} - l_f E_{smelt} - l E_{sb} \tag{4-1}
$$

where $C_{sn}$ and $\rho_{sn}$ are the specific heat of snow $[\mathrm{J}\,\mathrm{kg}^{-1}\,\mathrm{K}^{-1}]$ and the density of the bulk snow $[\mathrm{kg}\,\mathrm{m}^{-3}]$, respectively, $\lambda_{sn}$ the thermal conductivity of snow $[\mathrm{W}\,\mathrm{m}^{-1}\,\mathrm{K}^{-1}]$, $I_n$ the net solar flux in snow $[\mathrm{W}\,\mathrm{m}^{-2}]$, $l_f$ and $l$ the latent heats of fusion and sublimation $[\mathrm{J}\,\mathrm{kg}^{-1}]$, respectively, $E_{smelt}$ the melting or freezing rate in snow $[\mathrm{kg}\,\mathrm{m}^{-3}\,\mathrm{s}^{-1}]$, and $E_{sb}$ the sublimation rate of water vapor in snow $[\mathrm{kg}\,\mathrm{m}^{-3}\,\mathrm{s}^{-1}]$. $I_n$ is calculated as $(1 - r)(1 - A_b)S_{down}\exp(-\mu z)$, where $r$ the absorptivity of solar radiation at the snow surface, $A_b$ the snow albedo as a sum of that for direct and diffuse visible and near-infrared solar and long-wave radiations (Wiscombe and Warren 1980$^{24)}$), and $\mu$ the extinction coefficient of solar radiation (Jordan 1991$^{21)}$).

$E_{sb}$ is calculated only at the snow surface by assuming that water vapor is saturated over the snow:

$$
E_{sb0} = \sigma_{sn}\rho c_{E0}|\mathbf{u}|[q_{sat}(T_{sn0}) - q_r] \tag{4-2}
$$

where $\sigma_{sn}$ is the fractional area of snowcover parameterized using physical snow height (Essery et al. 2013$^{25)}$), $\rho$ the density of air $[\mathrm{kg}\,\mathrm{m}^{-3}]$, $c_{E0}$ the bulk coefficient, $q_{sat}(T_{sn0})$ the saturated specific humidity at the snow surface temperature $[\mathrm{kg}\,\mathrm{kg}^{-1}]$, $T_{sn0}$ the snow surface temperature [K], and $|\mathbf{u}|$ and $q_r$ the horizontal wind speed $[\mathrm{m}\,\mathrm{s}^{-1}]$ and specific humidity $[\mathrm{kg}\,\mathrm{kg}^{-1}]$ at the lowest atmospheric layer, respectively.

Melting or freezing rate in snow is calculated by snow temperature as:

$$
E_{smelt} = \frac{C_{sn}\rho_{sn}}{l_f}\frac{T_{sn} - T_m}{\Delta t} \tag{4-3}
$$

where $T_m$ is the melting point of 273.15 K. Using $E_{smelt}$, ice content in snow $w_i$ at each snow layer $[\mathrm{kg}\,\mathrm{m}^{-2}]$ is determined as:

$$
\frac{\partial w_i}{\partial t} = -E_{smelt}\Delta z \tag{4-4}
$$

Liquid water content in snow is expressed by the Richards' equation:

$$
\rho_w\frac{\partial\eta_{sw}}{\partial t} = \frac{\partial}{\partial z}\left(D_{sw}\frac{\partial\eta_{sw}}{\partial z} + K_{sw}\right) - E_{smelt} \tag{4-5}
$$

where $\eta_{sw}$ is the snow volumetric liquid water content $[\mathrm{m}^3\,\mathrm{m}^{-3}]$, $D_{sw}$ is the snow liquid water diffusivity $[\mathrm{m}^2\,\mathrm{s}^{-1}]$, $K_{sw}$ the snow unsaturated hydraulic conductivity $[\mathrm{m}\,\mathrm{s}^{-1}]$, and $\rho_w$ the density of liquid water $[\mathrm{kg}\,\mathrm{m}^{-3}]$. The equations for $D_{sw}$ and $K_{sw}$ are similar to those for soil water content in capillary region (Katata 2009$^{2)}$) using the empirical parameters given by Hirashima et al. (2010)$^{22)}$.

Snow accumulation and compaction at each snow layer are modelled as:

$$
\begin{aligned}
\frac{1}{\Delta z}\frac{\partial\Delta z}{\partial t} &= C_{snf} - C_{met} - C_{over} - C_{mel} \tag{4-6} \\
C_{met} &= c_1\exp[-c_2(T_m - T_s) - c_3\max(0, \rho_s - \rho_0)] \tag{4-7} \\
C_{over} &= \frac{-P_s}{\eta_{sn}} \tag{4-8} \\
C_{mel} &= \frac{1}{\Delta t}\max\left(0, \frac{f_{ice} - f_{ice}^{+}}{f_{ice}}\right) \tag{4-9}
\end{aligned}
$$

where $\Delta z$ is the snow layer thickness $[\mathrm{m}]$, $C_{snf}$, $C_{met}$, $C_{over}$, and $C_{mel}$ the change rate in $\Delta z$ $[\mathrm{s}^{-1}]$ due to snowfall, metamorphism, overburden, and melting, respectively, and $f_{ice}$ and $f_{ice}^{+}$ the fraction of ice before and after the melting, respectively. $C_{snf}$ is calculated as $S_f \rho_{fs} / \rho_w$, where $S_f$ is the snowfall rate $[\mathrm{mm}\,\mathrm{s}^{-1}]$ given by either the input data or the empirical equation using total rainfall rate and wet bulb temperature (Yamazaki 2001$^{23)}$), and $\rho_{fs}$ the fresh snow density $[\mathrm{kg}\,\mathrm{m}^{-3}]$ obtained by Boone (2002)$^{26)}$. Values for the parameters in the above equations are given by Oleson et al. (2010)$^{20)}$.

Snow grain growth is calculated based on Jordan (1991)$^{21)}$ as:

$$
\frac{\partial d_{sn}}{\partial t} = \begin{cases}
\frac{g_1|U_v|}{d_{sn}} & \eta_{sw} = \eta_{sw,irr} \\
\frac{g_2}{d_{sn}}(\eta_{sw} + 0.05) & \eta_{sw,irr} < \eta_{sw} < 0.09 \\
0.14\frac{g_2}{d_{sn}} & 0.09 \le \eta_{sw}
\end{cases} \tag{4-10}
$$

where $d_{sn}$ is the snow grain diameter $[\mathrm{m}]$, $U_v$ the mass vapor flux in snow layer $[\mathrm{kg}\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}]$, and $g_1$ and $g_2$ the parameters. The formulation of $U_v$ and values of $g_1$ and $g_2$ are given by Jordan (1991)$^{21)}$.

After the above calculations for temperature, and liquid and ice water contents, and accumulation and compaction in snow, the number of snow layers is adjusted by either combining or subdividing layers (Jordan 1991$^{21)}$) to obtain the physical snow height.

### 4.2. Soil freeze-thaw

In the soil module, freeze-thaw processes in soil are considered to heat conduction and liquid water flow equations as follows:

$$
C_s\rho_s\frac{\partial T_s}{\partial t} = \frac{\partial}{\partial z}\left(\lambda_s\frac{\partial T_s}{\partial z}\right) - l E_b - l_f E_{mel} \tag{4-11}
$$

$$
\rho_w\frac{\partial\eta_w}{\partial t} = \frac{\partial}{\partial z}\left(D_w\frac{\partial\eta_w}{\partial z} + K\right) - E_b - E_{mel} \tag{4-12}
$$

where $C_s$ and $\rho_s$ are the specific heat of soil $[\mathrm{J}\,\mathrm{kg}^{-1}\,\mathrm{K}^{-1}]$ and the density of the bulk soil $[\mathrm{kg}\,\mathrm{m}^{-3}]$, respectively, $\lambda_s$ the thermal conductivity of soil $[\mathrm{W}\,\mathrm{m}^{-1}\,\mathrm{K}^{-1}]$, $l_f$ and $l$ the latent heats of fusion and sublimation $[\mathrm{J}\,\mathrm{kg}^{-1}]$, respectively, $\eta_w$ is the volumetric soil water content $[\mathrm{m}^3\,\mathrm{m}^{-3}]$, $D_w$ is the soil water diffusivity $[\mathrm{m}^2\,\mathrm{s}^{-1}]$, $K$ the unsaturated hydraulic conductivity $[\mathrm{m}\,\mathrm{s}^{-1}]$, $E_b$ the evaporation or condensation or sublimation of soil water $[\mathrm{kg}\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}]$, and $E_{mel}$ the melting or freezing rate in soil $[\mathrm{kg}\,\mathrm{m}^{-3}\,\mathrm{s}^{-1}]$, respectively. The soil water diffusivity $D_w$ is expressed by:

$$
D_w = K\frac{\partial\psi}{\partial\eta_w} \tag{4-13}
$$

where $\psi$ is the water potential $[\mathrm{m}]$.

Ice content at each soil layer $\eta_i$ $[\mathrm{m}^3\,\mathrm{m}^{-3}]$ is determined in a similar way of snow ice content [Eqs. (4-2) and (4-3)] as:

$$
\frac{\partial\eta_i}{\partial t} = -\frac{E_{mel}}{\rho_i} \tag{4-14}
$$

$$
E_{mel} = \frac{C_s\rho_s}{l_f}\frac{T_s - T_m}{\Delta t} \tag{4-15}
$$

where $\rho_i$ is the density of ice $[\mathrm{kg}\,\mathrm{m}^{-3}]$.

The water potential $\psi$ $[\mathrm{m}]$ and unsaturated hydraulic conductivity $K$ $[\mathrm{m}\,\mathrm{s}^{-1}]$ in frozen soil [Eq. (4-12)] are modeled based on the concept of freezing point depression:

$$
\psi = \psi_{unfrozen}\left(1 + C_k\eta_i\right)^2 \tag{4-16}
$$

$$
K = K_{unfrozen}10^{-E_i\eta_i} \tag{4-17}
$$

where $C_k$ and $E_i$ are the empirical parameters given by Zhang et al (2007)$^{27)}$, and $\psi_{unfrozen}$ and $K_{unfrozen}$ the $\psi$ and $K$ in unfrozen soil described in Katata (2009)$^{2)}$, respectively.

After the above modification, SOLVEG can predict temporal changes in ice and liquid water content, temperature, and grain size at each snow layer, and ice water content in each soil layer.

### 4.3. Vegetation growth

Towards ecosystem modeling, the processes for plant phenology (e.g., leaf development and senescence) and soil and dissolved organic carbon cycle are implemented into the SOLVEG. First, the relevant schemes in grass growth model LINtul GRAssland, LINGRA (Schapendonk et al 1998$^{28)}$; Höglind et al 2001$^{29)}$) is coupled with the vegetation sub-model to simulate the vegetation growth. LINGRA is based on plant morphological key processes and light interception and has separated algorithms for source- and sink-related processes and a mechanistic, though simple, approach of grass morphological development, simulating the natural sequence of events in grasslands as regular defoliation due to grazing or cutting. The scheme is evaluated by using experimental datasets of harvestable dry matter of perennial rye grass collected in Europe. Since a full description of LINGRA is available in Schapendonk et al (1998)$^{28)}$, the important equations are summarized below.

Total actual vegetation growth, $\Delta W$ $[\mathrm{g}\,\mathrm{d}^{-1}]$, is determined by the balance between assimilate demand (sink), $\Delta W_d$, and assimilate supply (source), $\Delta W_s$. In the following, the subscript $d$ denotes the demand function, and the subscript $s$ denotes the supply function. Newly formed assimilates available for growth are partitioned between the leaves (above-ground biomass) and the roots (below-ground biomass). This partitioning between leaves and roots is independent from limitation factors of the growth (i.e., sink- or source-limited). Therefore, the total assimilate demand for (sink-limited) crop growth, $\Delta W_d$, is:

$$
\Delta W_d = \frac{\Delta LAI_n \cdot \Delta SLA}{f_{lv}} \tag{4-18}
$$

where $\Delta LAI_n$ $[\mathrm{m}^2\,\mathrm{m}^{-2}\,\mathrm{d}^{-1}]$ and $\Delta SLA$ $[\mathrm{m}^2\,\mathrm{g}^{-1}]$ are the daily increase in leaf area index (LAI) and the specific leaf weight of the newly formed leaves, respectively, and $f_{lv}$ the fraction of assimilates that is partitioned to the leaves. Currently, $f_{lv}$ is set to unity based on the assumption that all available carbon is preferentially allocated to leaves, and the rest of carbon in the reserve $\Delta W_{pool}$ in Eq. (4-20) is partitioned to root growth. This assumption may be valid for typical perennial grasslands (Höglind et al 2001$^{29)}$).

There are two sources of assimilate supply $\Delta W_s$ $[\mathrm{g}\,\mathrm{m}^{-2}\,\mathrm{d}^{-1}]$: the amount of assimilates fixed by photosynthesis during the day, $P$ $[\mathrm{g}\text{-C}\,\mathrm{m}^{-2}\,\mathrm{d}^{-1}]$, and the reallocated assimilates from the amount of carbohydrates stored in the reserve pool (i.e., stubble), $\Delta W_{pool}$ $[\mathrm{g}\text{-C}\,\mathrm{m}^{-2}\,\mathrm{d}^{-1}]$:

$$
\Delta W_s = P + \Delta W_{pool} \tag{4-19}
$$

where $P$ is calculated as accumulation of the net assimilation for each time step in vegetation sub-model (Nagai 2004$^{1)}$). In the calculation of $P$, the cold acclimation depending on seasonal air temperature variation is considered via decreasing the maximum catalytic capacity of Rubisco ($V_{cmax}$) by simply multiplying the factors of annual change of photosynthesis (Mäkelä et al 2004$^{30)}$). When snow covers grasses, no photosynthesis is assumed due to low light availability and only soil respiration is considered.

Actual total crop growth rate $\Delta W$ is the minimum of the assimilate demand and the assimilate supply as $\min(\Delta W_d, \Delta W_s)$. Thus, growth takes only place when the supply (photosynthesis plus reallocation from the reserve pool) exceeds or equals the demand function. Conversely, carbohydrates will be stored in the reserve pool $\Delta W_{pool}$ when the photosynthetic supply $(\Delta W_s)$ exceeds the demand $(\Delta W_d)$ as:

$$
\Delta W_{pool} = \Delta W_s - \Delta W_d \tag{4-20}
$$

Net leaf growth of LAI, $\Delta LAI$ $[\mathrm{m}^2\,\mathrm{m}^{-2}\,\mathrm{d}^{-1}]$, is derived from the amount of assimilates available for growth and the death rate of leaves by senescence as:

$$
\Delta LAI = \Delta LAI_n - \Delta LAI_d \tag{4-21}
$$

where $\Delta LAI_d$ $[\mathrm{m}^2\,\mathrm{m}^{-2}\,\mathrm{d}^{-1}]$ is the death rate of leaves calculated from a relative death rate due to internal shading and by water stress. The LAI value updated with $\Delta LAI$ is applied to the vegetation sub-model.

Natural turnover of leaves and roots are modeled using typical life spans in years (Arora and Boer 2005$^{31)}$). The fraction of roots in soil layers and rooting depth are modeled as a function of root biomass (Arora and Boer 2003$^{32)}$).

It is noted that the vegetation growth scheme implemented here is currently available for only grassland ecosystem. Further modification of the allocation scheme is required so that the model is applied to forest ecosystems.

### 4.4. Soil organic carbon cycle

The soil sub-model has been updated to simulate the organic matter decomposition and dissolved organic carbon (DOC) leaching in the aboveground litter layer, the belowground input of carbon from roots, and soil organic carbon (SOC) turnover and DOC transport along water flows throughout the soil profile for three SOC pools (active, slow, and passive, characterized by a turnover time of years, decades, and millennia, respectively) (Ota et al. 2013$^{8)}$). For these three SOC pools, it was assumed that at every time step and every grid within the soil, an immediate equilibrium can be achieved for sorption and desorption of soil C between the solid (SOC contained in the soil constituents) and dissolved (DOC contained in the soil water) phases.

The change in the SOC content for the $i$-th C pool (subscript $i = 1, 2,$ and $3$ for the active, slow, and passive carbon, respectively) at a certain depth in the soil profile is modeled by:

$$
\frac{\partial\rho_b\chi_{ss,i}}{\partial t} = S_{ss,i} - k_{ss,i}\rho_b\chi_{ss,i} \tag{4-22}
$$

where $\rho_b$ is the dry bulk density of the soil $[\mathrm{kg}\,\mathrm{m}^{-3}]$, $S_{ss,i}$ the input rate of carbon as SOC into the $i$-th SOC pool $[\mathrm{kg}\text{-C}\,\mathrm{m}^{-3}\,\mathrm{s}^{-1}]$, and $\chi_{ss,i}$ and $k_{ss,i}$ the SOC content per dry soil mass $[\mathrm{kg}\text{-C}\,\mathrm{kg}^{-1}]$ and the decomposition rate of the SOC $[\mathrm{yr}^{-1}]$ in the $i$-th carbon pool. At the ground surface, dead leaf biomass calculated by $\Delta LAI_d$ and the specific leaf weight in section 4.3 is used as input to the aboveground litter layer.

The transport of DOC for the $i$-th carbon pool in the soil is then modeled by considering the diffusion and advection of the DOC, as well as the loss of DOC via root-water uptake and microbial decomposition as:

$$
\frac{\partial\eta_w\chi_{sw,i}}{\partial t} = \frac{\partial}{\partial z}\left(D_{wsw}\frac{\partial\chi_{sw,i}}{\partial z}\right) - \frac{\partial E_w\chi_{sw,i}}{\partial z} - e_r\chi_{sw,i} - k_{sw,i}\eta_w\chi_{sw,i} \tag{4-23}
$$

where $D_{wsw}$ is the effective diffusivity of the DOC $[\mathrm{m}^2\,\mathrm{s}^{-1}]$, $E_w$ the vertical soil water flux $[\mathrm{m}^3\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}]$, $e_r$ the root-water uptake $[\mathrm{m}^3\,\mathrm{m}^{-3}\,\mathrm{s}^{-1}]$, and $k_{sw,i}$ the decomposition rate for DOC defined according to each DOC pool $[\mathrm{s}^{-1}]$. $\eta_w$, $E_w$, and $e_r$ at each soil layer are calculated in the soil sub-model (Katata 2009$^{2)}$).

**Table 4-1** An example of parameter settings of SOLVEG for alpine grassland ecosystem (Desai et al. 2016$^{12)}$).

| Description | Unit | Value |
|:------------|:-----|:------|
| Initial carbohydrate storage | kgDM ha⁻¹ | 2100 |
| Maximum catalytic capacity of Rubisco at 25 °C | μmol m⁻² s⁻¹ | 60 |
| Initial tiller density | number m⁻² | 600 |
| Dark respiration rate of leaves at 25 °C | μmol m⁻² s⁻¹ | 1.2 |
| Activation energy for dark respiration | J mol⁻¹ | 134.6 |
| Minimum stomatal conductance | mol m⁻² s⁻¹ | 0.0219 |
| Initial leaf area index (LAI) | m² m⁻² | 2.0 |
| Initial root biomass | kgDM ha⁻¹ | 5000 |
| Slope of stomatal conductivity in response to assimilation | - | 9 |
| Phyllochron (interval between leaf appearance) | °C day | 70 |
| Leaf life span | year | 1.5 |
| Root life span | year | 1.0 |
| Maximum drought leaf loss rate | day⁻¹ | 0.005 |
| Shape parameter for leaf loss due to drought | - | 3 |
| Maximum storage carbohydrate fraction | gDM gDM⁻¹ | 0.3 |
| Time constant for storage carbohydrate | day | 1 |
| Specific leaf area (SLA) | m² kgDW⁻¹ | 10 |
| Maximum LAI-induced leaf loss rate | day⁻¹ | 0.06 |
| Minimum threshold temperature for leaf appearance and tillering | °C | 5 |
| Maximum threshold temperature for leaf appearance and tillering | °C | 10 |
| LAI after the grass cut | m² m⁻² | 0.8 |
| **Parameters for soil microbiological module** | | |
| Snow layer thickness | mm | 5 |
| Parameter for the effect of soil specific surface on matric potential due to the presence of ice | - | 8 |
| Irreducible liquid water content in snow | m³ m⁻³ | 0.03 |

## 5. Model code

The model code is written in fortran77 and 90, and executable on over Linux/Unix and Cygwin (Windows) environments. Details of the model code and procedure to run the model are described here. Note that underlined files represent newly incorporated routines in the present study. Flow chart is illustrated in Fig. 5-1.

*[Figure 5-1]* Calculation flow chart of the terrestrial ecosystem model SOLVEG. Two subroutines for vegetation growth and soil carbon cycle are calculated on a day (grey shaded boxes), while other ones are calculated every time step (DELT). Newly incorporated and modified subroutines are underlined in the figure.

### 5.1. Structure of model code

The SOLVEG model mainly consists of four directories for the source code (SRC), input data as upper boundary conditions (INPUT), tables (TABLE), and output data (OUTPUT) under the root directory (SOLVEG). Each directory contains the following files:

**a) Root: SOLVEG/**
- Shell-script for execution `go_1D.sh`

**b) Main source code: SOLVEG/SRC/**
- Shell-script for compilation `Makefile`
- Executable file `solveg`
- Module files (`prm_*`)
  - `prm_grid.f` Common grid parameters
  - `prm_var.f` Common constants
  - `prm_array.f` Common array variables (call prm_grid and prm_var)
  - `prm_gasspc.f` Molecular weight for gas species
  - `prm_iospc.f` Parameters for inorganic aerosol species
  - `prm_nrspc.f` Molecular weight for non-photochemical reactive gas species
  - `prm_snfz.f` Parameters for snow and soil freeze-thaw
  - `prm_soil.f` Parameters for dry soil condition
  - `prm_veg.f` Parameters for vegetation growth
- Program files (`*.f`)
  - `efalbedo.f` Subroutine EALBED: soil surface albedo
  - `ehws.f` Subroutine EHWS: saturated soil water content
  - `eli2va.f` Subroutine ELI2VA: specific humidity in soil pore
  - `eppara.f` Subroutine EPPARA: leaf projection coefficient
  - `espara.f` Subroutine ESPARA: soil heat capacity and conductivity
  - `evpara.f` Subroutine EVPARA: soil vapor diffusivity/evaporation resistance
  - `ewpara.f` Subroutine EWPARA: soil water conductivity and diffusivity
  - `faipsy.f` Functions FAIM, FAIH, PSYM, PSYH, SHMD, and SHMDD: soil surface exchange functions
  - `fcpair.f` Function FCPAIR: specific heat of air
  - `fcw.f` Function FCW: specific heat of water
  - `fdensa.f` Function FDENSA: air density
  - `fl.f` Function FL: latent heat of vaporization
  - `gtable.f` Subroutine GTABLE: soil parameters
  - `gvprofile.f` Subroutine GVPROFILE: vegetation profile data
  - `gvtable.f` Subroutine GVTABLE: vegetation parameters
  - `gzsolveg.f` Subroutine GZSOLVEG: soil and vegetation grid
  - `lineint.f` Subroutine LINEINT: linear interpolation of data
  - `main.f` Main routine SOLVEG
  - `pdebugw0.f` Subroutine DEBUGW: atmospheric variable output
  - `pfluxcal.f` Subroutines SFPR13, FLXCAL, KMHCAL, and SAVEOD: turbulence and variable for the next time step
  - `pgener.f` Subroutines GENER, DIREC1, and DIREC2: diffusion scheme
  - `pinit01.f` Subroutine MSHINT: atmosphere grid
  - `pinitpf.f` Subroutines INITPF and CLSL2A: initial atmospheric variables
  - `pmain03.f` Subroutines UMAIN, TMAIN, EMAIN, and CMAIN: wind, temperature, specific humidity, fog water, turbulence, and $\mathrm{CO}_2$ concentration profile
  - `ppcal.f` Subroutine PCAL: air pressure
  - `ppread.f` Subroutines PREAD: read input parameters and meteorological and atmospheric chemistry data; Subroutine DEWTPM: dew point
  - `ptint.f` Subroutine TIMEINT: read temporal change in meteorological and atmospheric chemistry data
  - `shifi1.f` Subroutine HIFI1: water advection in soil
  - `slco2.f` Subroutine SLCO2: soil $\mathrm{CO}_2$
  - `sliqu.f` Subroutine SLIQU: soil water
  - `solveg.f` Subroutines SLVGIIN and SOLVEG: soil-vegetation processes
  - `solver1.f` Subroutine SOLV1: diffusion scheme
  - `solver2.f` Subroutine SOLV2: diffusion scheme
  - `srad.f` Subroutine SFCRAD: canopy radiation transmission
  - `sradiatn.f` Subroutine RADIATION: solar and long-wave radiation
  - `stemp.f` Subroutine STEMP: soil temperature
  - `svapo.f` Subroutine SVAPO: specific humidity in soil pore
  - `svfogcp.f` Subroutine FOGCAP: cloud water collection rate by leaves
  - `svliqu.f` Subroutine VLIQU: leaf surface water and canopy water flux
  - `svrsco2.f` Subroutine RSCO2: $\mathrm{CO}_2$ assimilation and stomatal resistance
  - `svrsst.f` Subroutine RESISTS: stomatal resistance
  - `svsed.f` Subroutine SED and SEDPM: gravitational settling flux
  - `svtemp.f` Subroutine VTEMP: vegetation temperature
  - `swadsp.f` Subroutine WADSPO: dry soil processes; Function POTEV: potential surface evaporation

**c) Program files (`*.f`) for gas and particle dry deposition: SOLVEG/SRC/GAS-PM**
- `fdist.f` Function FDIST, DGL10, NORM, and DEIR: fogwater size distribution
- `feps.f` Function EPS and BETA: Fogwater and aerosol capture efficiency
- `fvgrv.f` Function VGRV: gravitational settling function
- `gfkappa.f` Subroutine GFKAPPA, GET_D_WET, and ET_RH_EQ: aerosol hygroscopicity
- `hlconst.f` Function HLCONST: Henry's law constant
- `gpsamain.f` Subroutine GASMAIN: gas concentration profile for each chemical species
- `pmmain.f` Subroutine PMMAIN: aerosol concentration profile for each chemical species and mode
- `svgasrwc.f` Subroutine GASRWC: gas transfer resistance
- `svpmcpm.f` Subroutine PMCAPM: aerosol mass collection rate by leaves

**d) Program files (`*.f`) for snow: SOLVEG/SRC/SNOW**
- `faipsysn.f` Function FAIMS, FAIHS, PSYMS, and PSYHS: snow surface exchange functions
- `snliuq.f` Subroutine SNLIQU: snow water content
- `snpara.f` Subroutine SNPARA: snow heat capacity and conductivity
- `sntemp.f` Subroutine SNTEMP: snow temperature
- `snwpara.f` Subroutine SNWPARA: snow water conductivity and diffusivity
- `solver1sn.f` Subroutine SOLV1SN: diffusion scheme for snow
- `solver2sn.f` Subroutine SOLV2SN: diffusion scheme for snow

**e) Program files (`*.f`) for vegetation growth and SOC/DOC: SOLVEG/SRC/VEG_SOC**
- `slorc.f` Subroutine SLORC: soil organic carbon cycle
- `veggrw.f` Subroutine VEGGRW: vegetation growth; Subroutine TILSUB: tillering; Subroutine MOWING: mowing; Subroutine FATALERR and function LINT2, FCNSW, INSW, LIMIT, NOTNUL, REAAND, ILENG, and INTGRL: functions

**f) Input data: SOLVEG/INPUT/**
- `metadata.dat` Meteorological data file (fort.9) (interval of TINTINP)
- `fpmdata.dat` Fine aerosol data file (fort.11) (unequal time interval)
- `cpmdata.dat` Coarse aerosol data file (fort.12) (unequal time interval)
- `gasdata.dat` Gas concentration data file (fort.13) (unequal time interval)

**g) Tables: SOLVEG/PARAMETER/**
- `param_1D` Parameter file (fort.10)
- `zmesh.model_1D` Vertical grid coordinate file (fort.14)
- `BCsoil.table` (old), `vGsoil.table` (new) Soil parameter files (fort.15 and 18)
- `zvoge.table_1D` Vegetation parameter file (fort.16)
- `zvoge.profile_1D` Input LAI and root profile file (fort.17)

**h) Output data: SOLVEG/OUTPUT/**
- `outlist` Standard output files (fort.6)
- `dbout` Meteorological variable file (fort.20)
- `PMINPout` Aerosol concentration input file (fort.21)
- `GASINPout` Gas concentration input file (fort.22)
- `METout` Meteorological input file (fort.23)
- `FLXout` Surface flux file (fort.24)
- `WNDout` Wind speed file (fort.25)
- `ACO2out` Atmospheric $\mathrm{CO}_2$ file (fort.26)
- `BACO2out` Atmospheric $\mathrm{CO}_2$ budget file (fort.27)
- `mnout` Soil variable file (fort.30)
- `TSout` Soil temperature file (fort.31)
- `HWout` Soil water content file (fort.32)
- `QSout` Soil humidity file (fort.33)
- `EBout` Soil evaporation file (fort.34)
- `SFout` Soil surface flux file (fort.35)
- `wcurve` Water retention curve (fort.36)
- `CSRSout` Soil thermal property (fort.37)
- `VGout` Canopy variable file (fort.40)
- `VWout` Canopy water budget file (fort.41)
- `VTout` Canopy heat budget file (fort.42)
- `RADout` Canopy radiation file (fort.43)
- `PREout` Fog deposition and precipitation (fort.44)
- `SCO2out` Soil $\mathrm{CO}_2$ file (fort.50)
- `VCO2out` Canopy $\mathrm{CO}_2$ file (fort.51)
- `PSCO2out` Soil $\mathrm{CO}_2$ production file (fort.52)
- `BSCO2out` Soil $\mathrm{CO}_2$ budget file (fort.53)
- `PMCout` Aerosol concentration profile file (fort.60)
- `PMFLXout` Aerosol flux file (fort.61)
- `VPMout` Canopy aerosol capture file (fort.62)
- `VDGFoutXX` Size-resolved aerosol deposition file (fort.160-) (species number)
- `GASCout` Gas concentration profile file (fort.70)
- `GASFLXout` Gas flux file (fort.71)
- `HIout` Soil ice content file (fort.81)
- `TSNout` Snow temperature file (fort.82)
- `HSNout` Snow liquid water content file (fort.83)
- `SNRout` Bulk snow density file (fort.84)
- `EMLout` Snow phase change rate file (fort.85)
- `WICEout` Snow ice content file (fort.86)
- `GRNout` Snow grain size file (fort.87)
- `VGRWout` Vegetation growth file (fort.91, daily)
- `BIOMout` Vegetation biomass file (fort.92, daily)
- `SISOout` Sink/source strength file (fort.93, daily)
- `SOC1out` Active pool SOC content file (fort.101, daily)
- `SOC2out` Slow pool SOC content file (fort.102, daily)
- `SOC3out` Passive pool SOC content file (fort.103, daily)
- `BSDOCout` SOC and DOC budget file (fort.104, daily)
- `DOC1out` Active pool DOC content file (fort.105, daily)
- `DOC2out` Slow pool DOC content file (fort.106, daily)
- `DOC3out` Passive pool DOC content file (fort.107, daily)
- `tmpout` Temporal output file (fort.99)

### 5.2. Settings and compilation of the model

Before the model users go on to compile and run the model, the `prm_grid.f` file in the SRC directory should be set to correct values of vertical grids for atmosphere (N1 and M1), vegetation (NC) and soil layers (NS). Note that the number of vegetation layers is smaller than that of atmosphere; i.e., NC < N1. The numbers of total horizontal grids NX (x-direction) and NY (y-direction), and the grids for output file IX and JY are set to unity because of a one-dimensional calculation. The parameter NA should be set to the layer number where atmospheric variables are generated at the OUTPUT directory. The number of gas (NGS) and aerosol species (NAS), and bin size for each aerosol species (MANP) are also given for SOLVEG run with gas and aerosol deposition. The species names and concentrations of gases and aerosols must be provided from the files of `gasdata.dat` (gas), `fpmdata.dat` (fine aerosol mode), and `cpmdata.dat` (coarse aerosol mode) in SOLVEG/INPUT directory. The name and parameters of available gas and aerosol species are listed in `prm_gasspc.f`, `prm_nrspc.f`, and `prm_iospc.f`. Tables 5-1, 5-2, 5-3, and 5-4 are examples of input data files.

With above settings, a compilation of the model begins by typing `make clean` and `make` at SOLVEG/SRC directory. After the execution of this script normally terminates, the execution file of SOLVEG named `zsolveg_1D.exe` must be created at the root directory. It should be noted that, if the module files beginning with `prm_` are modified, the user should always require to type `make clean` and then `make` as appropriate compilation.

**Table 5-1** Example of input meteorological data file (`metadata.dat`)

| TIME | P | RS | RL | RR | U | V | T | Q | WL | CO2 | SNR |
|:-----|:---|:----|:----|:----|:----|:----|:-----|:----|:----|:----|:----|
| 2013-01-01_0000 | 943.00 | 0.00 | 237.00 | 0.00 | 0.69 | 0.45 | 270.60 | 3.01 | 0.00 | 400.00 | 0.00 |
| 2013-01-01_0030 | 943.00 | 0.00 | 236.43 | 0.00 | -0.62 | 0.25 | 270.00 | 2.93 | 0.00 | 400.00 | 0.00 |

\* P: surface pressure [hPa], RS: solar radiation flux [W m⁻²], RL: long-wave radiation flux [W m⁻²], RR: rain intensity [mm h⁻¹], U: wind u-component [m s⁻¹], V: wind v-component [m s⁻¹], T: air temperature [K], Q: specific humidity [g kg⁻¹], WL: cloud liquid water content [g m⁻³], CO2: CO₂ concentration [ppmv], and SNR: snowfall rate [mm h⁻¹].

**Table 5-2** Example of input atmospheric gas data file (`gasdata.dat`) with NGS ≤ 7

| TIME | O3 | SO2 | NO2 | NH3 | HNO3 | NO | HCl |
|:-----|:---|:----|:----|:----|:-----|:---|:----|
| 2013-08-01_0000 | 1.00 | 1.00 | 1.00 | 1.00 | 1.10 | 1.00 | 1.00 |
| 2013-08-02_1200 | 0.80 | 1.00 | 1.00 | 1.00 | 1.00 | 1.10 | 1.00 |
| 2013-08-02_1800 | 0.20 | 1.00 | 1.00 | 1.00 | 1.00 | 1.10 | 1.00 |
| 2013-08-03_0000 | 1.50 | 1.00 | 1.00 | 1.00 | 1.00 | 1.10 | 1.00 |

... repeat until the end time of the calculation period

**Table 5-3** Example of input fine aerosol data file (`fpmdata.dat`) with NAS ≤ 8

| TIME | FSO4 | FNO3 | FNH4 | FCL | FNA | FK | FMG | FCA |
|:-----|:-----|:-----|:-----|:----|:----|:---|:----|:----|
| 2013-08-01_0000 | 1.00 | 1.00 | 1.00 | 1.00 | 1.10 | 1.00 | 1.00 | 1.00 |
| 2013-08-02_1200 | 0.10 | 1.00 | 1.00 | 1.00 | 1.00 | 1.10 | 1.00 | 1.00 |
| 2013-08-04_0000 | 1.20 | 1.00 | 1.00 | 1.00 | 1.00 | 1.10 | 1.00 | 1.00 |
| 2013-08-06_1500 | 0.50 | 1.00 | 1.00 | 1.00 | 1.00 | 1.10 | 1.00 | 1.00 |

... repeat until the end time of the calculation period

**Table 5-4** Example of input coarse aerosol data file (`cpmdata.dat`) with NAS ≤ 8

| TIME | CSO4 | CNO3 | CNH4 | CCL | CNA | CK | CMG | CCA |
|:-----|:-----|:-----|:-----|:----|:----|:---|:----|:----|
| 2013-08-01_0000 | 1.00 | 1.00 | 1.00 | 1.00 | 1.10 | 1.00 | 1.00 | 1.00 |
| 2013-08-02_1600 | 0.50 | 1.00 | 1.00 | 1.00 | 1.10 | 1.00 | 1.00 | 1.00 |
| 2013-08-03_0300 | 0.10 | 1.00 | 1.00 | 1.00 | 1.10 | 1.00 | 1.00 | 1.00 |
| 2013-08-06_1200 | 1.50 | 1.00 | 1.00 | 1.00 | 1.10 | 1.00 | 1.00 | 1.00 |

... repeat until the end time of the calculation period

\* The unit is $\mu\mathrm{g}\,\mathrm{m}^{-3}$ for all variables.

### 5.3. Running the model and visualization

In SRC directory, the grid number is set in `prm_grid.f` for your one-dimensional calculation domains.

In INPUT directory, the input file of usually hourly or half-hourly meteorological data (`metadata.dat`) covering throughout the calculation period is necessary for model run.

In PARAMETER directory, vertical mesh sizes should be set in the `zmesh.model_1D` file based on SRC/prm_grid.f. The vegetation profile file (`zvge.profile_1D`) also needs to be modified to specify variations in the whole calculation period by specifying vertical distributions of vegetation type (VTYPE), leaf area density (AZ), and root fraction for each vegetation type. The vegetation type is chosen from the vegetation parameter file (`zvge.table_1D`), which is specified by two integers: the former represents the category of vegetation, and the latter the spatial or temporal variation of them. In `param_1D`, the simulation condition such as calculation period, output interval is specified.

The model execution will begin by typing `./go_1D.sh` or submit as a batch job over SQL environment at the root directory. Several options of modelled processes for sensitivity tests are available in `go_1D.sh`:

- **a) ifog:** Fog deposition calculation (0 = no, 1 = yes)
  - **npdsd:** Droplet size distribution of cloud water (1–4) only work with ifog=1)
- **b) ifdsl:** Dry soil layer (DSL) calculation (0 = no, 1 = yes)
  - **npwrc:** Soil water retention curve (1–2) only work with ifdsl=0)
  - **nstms:** Soil thermal conductivity (1–2) only work with ifdsl=1)
- **c) ifsnw:** Snow/soil freeze-thaw (0 = no, 1 = yes)
  - **nsnfl:** Snowfall input (1–2) only work with ifsnw=1)
- **d) ifco2:** $\mathrm{CO}_2$ exchange (0 = no, 1 = yes)
- **e) ifgas:** Trace gas exchange (0 = no, 1 = yes)
- **f) ifpm:** Particulate matter (PM) deposition (0 = no, 1 = yes)
  - **ifgf:** Hygroscopic growth of aerosols (1 = yes, 0 = no) only work with ifpm=1)
- **g) ifveg:** Plant growth for grassland ecosystem (0 = no, 1 = yes)

For debugging the output data, the core-dump file (core.XXXXX) is created in case there are errors in the program. The user may use debugger programs, e.g., gdb (GNU Project Debugger; https://www.gnu.org/software/gdb/) to find errors in the program. The debug run is available when `ifcore = 1` and the certain number of core-dump file is given to `ncore` in `go_1D.sh`.

The output files of SOLVEG can be visualized by using gnuplot software (freely available at http://gnuplot.sourceforge.net/). Sample programs for R software (freely available at https://www.r-project.org/) is also available in SOLVEG/R directory to visualize model results as shown in Fig. 5-2.

*[Figures 5-2]* Example output of SOLVEG calculations using a sample R shell-script. Panels include net radiation (Rnet), sensible heat flux (H), latent heat (IE), soil heat flux (G), Bowen ratio (H/IE), friction velocity, albedo, snow depth and canopy height, volumetric soil liquid water and ice content, $\mathrm{CO}_2$ flux, leaf area index (LAI), and carbohydrate storage of vegetation.

## 6. Summary

To investigate the impacts of atmospheric pollutants (gases and aerosols) on terrestrial ecosystems, the processes of dry deposition and emission of gases and aerosols, snow accumulation and melting, soil freeze-thaw, vegetation growth, and soil organic carbon cycle were implemented in the ecosystem model SOLVEG. The details of newly incorporated schemes were documented in this report. Further application of the model to various environmental issues will be expected to understand the complicated interaction among human activities, climate changes, and terrestrial ecosystem responses.

## Acknowledgement

This study was partially supported by a Postdoctoral Fellowship for Research Abroad and a Grant-in-Aid for Scientific Research by the Japan Society for the Promotion of Science (JSPS).

## References

1. H. Nagai: "Atmosphere-soil-vegetation model including CO2 exchange processes: SOLVEG2", JAERI-Data/Code 2004-014 (2004), 92p.
2. G. Katata: "Improvement of a land surface model for accurate prediction of surface energy and water balances", JAEA-Data/Code 2008-033 (2009), 64p.
3. G. Katata, H. Nagai, H. Ueda, N. Agam, P.R. Berliner: "Development of a Land Surface Model Including Evaporation and Adsorption Processes in the Soil for the Land-Air Exchange in Arid Regions", Journal of Hydrometeorology, 8, pp. 1307-1324 (2007).
4. H. Nagai: "Validation and sensitivity analysis of a new atmosphere-soil-vegetation model", Journal of Applied Meteorology, 41, pp. 160-176 (2002).
5. H. Nagai: "Validation and sensitivity analysis of a new atmosphere-soil-vegetation model. Part II: Impacts on in-canopy latent heat flux over a winter wheat field determined by detailed calculation of canopy radiation transmission and stomatal resistance", Journal of Applied Meteorology, 42, pp. 434-451 (2003).
6. G. Katata, K. Hayashi, K. Ono, H. Nagai, A. Miyata, M. Mano: "Coupling atmospheric ammonia exchange process over a rice paddy field with a multi-layer atmosphere-soil-vegetation model", Agricultural and Forest Meteorology, 180, pp. 1-21 (2013).
7. H. Nagai: "Incorporation of CO2 exchange processes into a multilayer atmosphere-soil-vegetation model", Journal of Applied Meteorology, 44, pp. 1574-1592 (2005).
8. M. Ota, H. Nagai, J. Koarashi: "Root and dissolved organic carbon controls on subsurface soil carbon dynamics: A model approach", Journal of Geophysical Research, 118, pp. 1646-1659 (2013).
9. G. Katata, H. Nagai, T. Wrzesinsky, O. Klemm, W. Eugster, R. Burkard: "Development of a Land Surface Model Including Cloud Water Deposition on Vegetation", Journal of Applied Meteorology and Climatology, 47, pp. 2129-2146 (2008).
10. G. Katata, H. Nagai, L. Zhang, A. Held, D. Serca, O. Klemm: "Development of an atmosphere-soil-vegetation model for investigation of radioactive materials transport in the terrestrial biosphere", Progress in Nuclear Science and Technology, 2, pp. 530-537 (2011).
11. G. Katata, M. Kajino, K. Matsuda, A. Takahashi, K. Nakaya: "A numerical study of the effects of aerosol hygroscopic properties to dry deposition on a broad-leaved forest", Atmospheric Environment, 97, pp. 501-510 (2014).
12. A.R. Desai, M. Wohlfahrt, M.J. Zeeman, G. Katata, W. Eugster, L. Montagnani, D. Gianelle, M. Mauder, H-P. Schmid: "Montane ecosystem productivity responds more to global circulation patterns than climatic trends", Environmental Research Letters, 11, (2016).
13. B.J. Huebert, C.H. Robert: "The dry deposition of nitric-acid to grass", Journal of Geophysical Research, 90, pp. 2085-2090 (1985).
14. L. Zhang, L.P. Wright, W.A.H. Asman: "Bi-directional air-surface exchange of atmospheric ammonia: A review of measurements and a development of a big-leaf model for applications in regional-scale air-quality models", Journal of Geophysical Research, 115, pp. D20310 (2010).
15. L.W.A. Van Hove, E.H. Adema, W.J. Vredenberg: "A study of the adsorption of $\mathrm{NH}_3$ and $\mathrm{SO}_2$ on leaf surfaces", Atmospheric Environment, 23, pp. 1479-1486 (1989).
16. L. Zhang, S. Gong, J. Padro, L. Barrie: "A size-segregated particle dry deposition scheme for an atmospheric aerosol module", Atmospheric Environment, 35, pp. 549-560 (2001).
17. M.D. Petters, S.M. Kreidenweis: "A single parameter representation of hygroscopic growth and cloud condensation nucleus activity", Atmospheric Chemistry and Physics, 7, pp. 1961-1971 (2007).
18. N.A. Fuchs, A.G. Sutugin: "Highly dispersed aerosols. Hidy G.M., Brock J.R. (Eds). Topics in Current Aerosol Research, vol. 2. Pergamon", New York, pp. 1-60 (1971).
19. C. Fountoukis, A. Nenes: "ISORROPIA II: a computationally efficient thermodynamic equilibrium model for $\mathrm{K}^{+}\text{-}\mathrm{Ca}^{2+}\text{-}\mathrm{Mg}^{2+}\text{-}\mathrm{NH}_4^{+}\text{-}\mathrm{Na}^{+}\text{-}\mathrm{SO}_4^{2-}\text{-}\mathrm{NO}_3^{-}\text{-}\mathrm{Cl}^{-}\text{-}\mathrm{H}_2\mathrm{O}$ aerosols", Atmospheric Chemistry and Physics, 7, pp. 4639-4659 (2007).
20. K.W. Oleson, D.M. Lawrence, G.B. Bonan, M.G. Flanner, E. Kluzek, P.J. Lawrence, S. Levis, S.C. Swenson, P.E. Thornton: "Technical description of version 4.0 of the Community Land Model (CLM)", NCAR Technical Note NCAR/TN-461+STR, National Center for Atmospheric Research, Boulder, CO (2010).
21. R. Jordan: "A one-dimensional temperature model for a snow cover", Technical documentation for SNTHERM.89, CRREL Special Report 91-16, US Army Core of Engineers Cold Regions Research and Engineering Laboratory, Hanover, NH (1991).
22. H. Hirashima, S. Yamaguchi, A. Sati, M. Lehning: "Numerical modeling of liquid water movement through layered snow based on new measurements of the water retention curve", Cold Regions Science and Technology, 64, pp. 94-103 (2010).
23. T. Yamazaki: "A one-dimensional land surface model adaptable to intensely cold regions and its applications in eastern siberia", Journal of the Meteorological Society of Japan, 79, pp. 1107-1118 (2001).
24. W.J. Wiscombe, S.G. Warren: "A model for the spectral albedo of snow. I: pure snow", Journal of Atmospheric Science, 37, pp. 2712-2733 (1980).
25. R. Essery, S. Morin, Y. Lejeune, C.B. Ménard: "A comparison of 1701 snow models using observations from an alpine site", Advances in Water Resources, 55, pp. 131-148 (2013).
26. A. Boone: "Description du schema de neige ISBA-ES (Explicit Snow)", Centre National de Recherches Météorologiques, Météo-France, Toulouse, France (2002).
27. X. Zhang, S. Sun, Y. Xue: "Development and testing of a frozen soil parameterization for cold region studies", Journal of Hydrometeorology, vol. 8, issue 4, pp. 690-701 (2007).
28. A.H.M.C. Schapendonk, W. Stol, D.W.G. van Kraalingen, B.A.M. Bouman: "LINGRA - a source/sink model to simulate grassland productivity in Europe", European Journal of Agronomy, 9, pp. 87-100 (1998).
29. M. Höglind, A.H.C.M. Schapendonk, M. van Oijen: "Timothy growth in Scandinavia: combining quantitative information and simulation modelling", New Phytologist, 151, pp. 355-367 (2001).
30. A. Mäkelä, P. Hari, F. Berninger, H. Hänninen, E. Nikinmaa: "Acclimation of photosynthetic capacity in Scots pine to the annual cycle of temperature", Tree Physiology, 24, pp. 369-376 (2004).
31. V. Arora, G.J. Boer: "A parameterization of leaf phenology for the terrestrial ecosystem component of climate models", Global Change Biology, 11, pp. 39-59 (2005).
32. V. Arora, G.J. Boer: "A representation of variable root distribution in dynamic vegetation models", Earth Interactions, 7, pp. 1-19 (2003).