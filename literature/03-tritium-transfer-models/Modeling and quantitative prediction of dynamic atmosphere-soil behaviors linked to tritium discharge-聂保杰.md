# Modeling and quantitative prediction of dynamic atmosphere-soil behaviors linked to tritium discharge

**Authors**: Baojie Nie*, Haoyang Wu, Yiling Ran, Dezhong Wang  
**Affiliation**: School of Mechanical Engineering, Key Laboratory of Nuclear Power Systems and Equipment of Ministry of Education, Shanghai Jiao Tong University, Shanghai, 200240, China  

**Journal**: Fusion Engineering and Design  
**Volume**: 211 (2025) 114811  

---

## A R T I C L E   I N F O

**Keywords**: Tritium; Atmospheric dispersion; Soil migration and conversion; Advanced nuclear energy systems

---

## A B S T R A C T

Tritiated water vapor (HTO) is the dominant source among the radioactive airborne effluent from commercial nuclear power plants. Gas or liquid metal coolant is recognized to be widely used in the advanced nuclear energy systems and fusion reactor. Elemental tritium (HT) would be the dominant form regarding the environmental effluents of advanced nuclear energy systems under the oxygen-free environment. Additionally, tritium release amount would also be higher than current pressurized water reactor. A dynamic modeling scheme was proposed to simulate tritium migration and conversion behaviors in the atmosphere-soil compartments. Atmospheric tritium concentration level was predicted by hourly-resolution wind field data. With regard to HTO discharge source, HTO concentration level in soil moisture was evaluated with consideration of daily-resolution atmospheric HTO concentration data, daily-resolution precipitation and evapotranspiration data. With regard to HT discharge source, HT concentration in air-filled soil porosity, conversion product known as HTO concentration in air-filled and water-filled soil porosity was predicted from the viewpoint of time series. Influence of key parameters such as HT conversion rate and gaseous fraction of conversion product in the soil on HTO distribution was discussed at last. It was indicated that environmental factors such as wind field, conversion rate, precipitation and evapotranspiration rate, gaseous fraction have a significant influence on tritium distribution in atmosphere-soil compartment. Development of time-varying simulation method adopting the above dynamic environmental factors as input data is beneficial for achieving a refined environmental impact assessment.

---

## 1. Introduction

Tritium is a radioactive isotope of hydrogen with a half-life of 12.3 a, which is mainly currently produced by anthropogenic pathway. Almost all of the world's nuclear power plants adopt water as the coolant. Tritium could be produced from both the fuel elements and water coolant. Small fraction approximately \(1\%\) of the tritium generated in the fuel pellets could be transferred to the coolant when adopting Zirconium alloy cladding [1]. The main chemical form of tritium in water coolant is widely known to be tritiated water (HTO) which is also the main source of airborne and liquid radioactive effluents. Ergo, HTO is the main form of tritium released into the environment regarding the water-cooled reactor [2]. Apart from the commercial thermal reactors, advanced reactors such as fast reactors, molten salt reactors and fusion reactors are also being developed to achieve a sustainable nuclear energy. For most of the advanced reactors, gas or liquid metal would be used as the coolant instead of water. Oxygen-free environment is required for these advanced reactors. Elemental tritium (HT) might be the main form generated from these reactors [3-5]. On the other hand, stainless-steel material is considered a promising cladding material for fast reactors, replacing the Zirconium alloy cladding used in water reactors, due to its superior corrosion resistance, neutron radiation damage resistance and mechanical performance at high temperatures [6]. However, tritium release fraction from stainless-steel cladding \((95\%)\) is approximately to two orders of magnitude higher than that of Zirconium alloy cladding [7]. Regarding the fusion reactor, tritium inventory would reach up to kilograms level which is three orders of magnitude higher than that of typical light water reactor [8]. Risk of large amount of tritium release could not be entirely avoided under some unforeseen accidents. Thus, HT is likely to be the main release source term for the advanced reactors. Tritium environmental behaviors and radiation dose assessment is a classic issue caused wide attentions by the fact that tritium is the most common radionuclide and contributor to the total released radioactivity [9]. Modeling and experimental investigations were performed in the past thirty years [10-12]. These investigations mainly focus on environmental behaviors and radiation dose assessment linked to HTO release source term for the demand-oriented needs of the commercial thermal reactors [13]. Regarding the HTO discharge source, it is still scarce to achieve a dynamic and refined prediction for environmental behaviors driven by time-varying environmental factors as specific activity model widely used in substantive codes failed to obtain time-series tritium concentration distribution. On the other hand, a systematic and dynamic assessment for HT release source term remains largely unexamined considering the complex soil conversion and re-emission behaviors [14]. Significant uncertainty exists in the estimation of environmental distribution linked to tritium discharge.

In view of the above considerations, this study aims to systematically predict tritium migration and conversion behaviors in the atmosphere-soil compartment driven by time-varying environmental factors. Near-surface hourly-resolution tritium concentration was obtained driven by dynamic wind field. Daily-resolution HTO distribution in different soil depth was predicted driven by daily-resolution atmospheric concentration data, precipitation and evapotranspiration rate data. Additionally, a detailed modeling was proposed to describe the migration and conversion behaviors in the atmosphere-soil compartment for HT discharge source. Transfer fraction including re-emission to the air and infiltration to deeper soil was discussed under different meteorological parameters.

---

## 2. Tritium atmosphere-soil behaviors

Key processes in the atmosphere-soil compartment for HTO/HT discharge source term could be summarized as follows. (1) First plume by atmospheric dispersion model. Main differences for HTO and HT are removal velocity, in particular under rainy days [15]; (2) Interface transfer of atmosphere-soil compartment. Generally, a consistent tritium fraction can be reasonably assumed in air moisture and soil moisture under the steady state near-surface HTO concentration. The detailed transfer processes originate from diffusion through air-filled porosity in the soil for gaseous HTO and HT source under non-rainy days, as well as water penetration for HTO source under rainy days; (3) Conversion and migration in the soil. The pathway for HT into the soil is through air-filled porosity. Conversion of HT into HTO would occur including bacterial oxidation and isotope exchange [16,17]. The pathway for HTO into the soil is through air-filled porosity under non-rainy days and water penetration under rainy days. HTO no matter from the first source or conversion products of HT would distribute both in the air-filled and water-filled porosity of soil and reach a balance under some conditions. Isotope exchange effect occurs in the soil for both HTO and HT. Thus, HT atmosphere-soil behaviors are more complex and specially described in the following part.

### 2.1. Brief description of HT atmosphere-soil behaviors

Although radioactivity of tritium is the highest in the airborne radioactive effluents, the annual released tritium quantity for a nuclear power plant site is only approximately at the gram level [18]. Thus, tritium mass fraction in the effluents is so small that the buoyancy effect could be ignored [19]. After released into the atmosphere, tritium concentration could be quickly diluted during the atmospheric dispersion. HT could also be oxidized in the air under room temperature, while the oxidation rate is very small. Additionally, HT could also transfer from air to surface soil through the diffusion process via the soil air-filled porosity. HT in the soil could be oxidized in a relatively fast rate compared with that in the air due to the action of soil microorganisms [20]. A doubtable point is whether physical state of conversion product known as HTO is in gaseous or liquid state. Soil fate of liquid HTO includes evaporation from the surface soil, migration to deep soil along with water flow, as well as root uptake by plants [21]. HTO absorbed by plant roots would transport to other organs such as leaves and fruits. Both part of HTO in the surface soil and plant organs could re-emit into the air along with water evapotranspiration. HTO entering the plants could be partly integrated organic matter in the form of organically bound tritium (OBT) which is another form of tritium in the environment [22] (Fig. 1).

> **Fig. 1.** Environmental behaviors of HT and radiation exposed pathways.
> (The figure illustrates the key processes including atmospheric dispersion, soil diffusion, bacterial oxidation, root uptake, and re-emission.)

### 2.2. Summary of HT conversion rate

In order to investigate conversion behavior of HT, a trace experiment through a 3.54 TBq HT atmospheric release was performed at a site at Chalk River Nuclear Laboratories in 1987. It was indicated that no rapid HT conversion in the air. While the conversion rate in the soil is approximately to \(1.5\% / \mathrm{h}\) and this behavior accounts of the majority of HTO in the air due to the re-emission of the conversion product [23]. Few atmospheric release experiments were reported by other research groups since then. Some laboratory experiments were performed by collecting soil samples in various locations. Different conversion rates from \(29.3\% / \mathrm{h}\) to \(19.6\% / \mathrm{min}\) were provided in these laboratory experiments [20,24-27]. In addition, field experiments were also performed around some nuclear facilities in which tritium was discharged under normal operation [28]. Very low-level conversion rate was given compared with atmospheric release experiments. Thus, conversion behavior of HT in the soil is still a confusing issue as conversion rates with a considerable uncertainty were reported in previous literatures. In order to assess radiation dose due to HT discharge, a variable conversion rates from \(0.1\% / \mathrm{min}\) to \(1\% / \mathrm{min}\) were adopted in this study (Table 1).

---

**Table 1 Summary of HT conversion experiments in the shallow soil layer.**

| Experimental types | Conversion rates | Refs. |
|---|---|---|
| Atmospheric release experiments | 1.5%/h | [23] |
| Laboratory experiments | 20%/h | [25] |
| | 12-66% (0.6-5.4 h) | [26] |
| | 19.6%/min | [20] |
| | 3.8%/min | [24] |
| | 5.8%/min | [27] |
| | 29.3%/h | [28] |
| | 0.6756±0.2715%/min | [27] |
| | 0.19% (CRL chamber experiment on Darlington natural soil following 13 min 36 s exposure, 24 h after exposure) | [28] |
| Field experiments around nuclear facility | 0.00028% (measure at moment of 24 h after 13.6 min exposure time during 0.5 h) | [29] |
| | 0.00015% (CRL field experiment, 30 min exposure, 2 h after exposure) | [30] |
| | 0.00011% (CRL field experiment, 12 days exposure, just after exposure) | [31] |

---

## 3. Material and methods

### 3.1. Overview of model structure

The dynamic atmosphere-soil model structure shown in Fig. 2 includes the following processes. Near-surface tritium concentration could be calculated by atmospheric dispersion model driven by time-varying wind field. As for HT source, dry and wet deposition could be ignored. The transfer from air to soil depends on concentration gradient. HT diffusion in the air-filled porosity of soil obeys the Fick diffusion law. After obtaining HT concentration distribution in the air-filled porosity of soil, HTO could be produced by HT conversion processes including both bacterial oxidation and isotope exchange effects. It is confusing when it comes to physical form of conversion products (HTO) in the soil. We reasonably assumed that part of HTO existed in air-filled porosity and could diffuse in the air-filled porosity and re-emit into the atmosphere. Another part of HTO existed in the soil moisture and would migrate in the soil along with soil water flow. The ratio between gaseous and liquid phase should be validated by future experiments. HTO in soil water could re-emit into the atmosphere through evapotranspiration effect. Both HT in the air and HTO re-emitted from soil can be inhaled and produce radiation dose for HT release source. For HTO release source, a consistent tritium fraction can be reasonably assumed in air moisture and soil moisture under the steady state near-surface HTO concentration. Subsequent HTO behavior in the soil moisture is similar to that of HT conversion product.

> **Fig. 2.** Overview of environmental model structure for HT/HTO release source.
> (The figure presents a flowchart of the modeling framework, linking atmospheric dispersion, soil diffusion, conversion, and re-emission modules.)

### 3.2. Model description

#### 3.2.1. Tritium atmospheric dispersion model

Four types of modes have been proposed to describe atmospheric dispersion behaviors of pollutants. They are Gaussian model, Lagrangian model, Eulerian model and Computational Fluid Dynamics (CFD) method, respectively. A diagnostic wind field and Lagrangian puff model was used in this investigation because of its advantages in real-time meteorological date integration, as well as high meteorological and topographic resolution. The diagnostic wind field model used in this work is the CALMET which is the abbreviation for California Meteorological Model [29]. Wind field could be predicted by solving the mass conservation equation showed in Eq. (1) on the basis of inputting meteorological data from multiple meteorological stations and topographic data. Lagrangian puff model named CALPUFF described by Eq. (2) and Eq. (3) was adopted to assess annual average tritium concentration distribution in the air driven by the hourly-resolution wind field.

\[
\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0 \quad (1)
\]

\[
C_{a,HT} = \frac{Q}{2\pi\sigma_x\sigma_y} g \exp\left[-d_x^2 / (2\sigma_x^2)\right] \exp\left[-d_y^2 / (2\sigma_y^2)\right] \quad (2)
\]

\[
g = \frac{2}{(2\pi)^{1/2}\sigma_z} \sum_{i=-\infty}^{\infty} \exp\left[-(H_e + 2ih)^2 / (2\sigma_z^2)\right] \quad (3)
\]

where, \(u, v, w\) represent wind velocity components \((\mathrm{m/s})\) in the downwind, crosswind and vertical directions, respectively; \(C_{a,HT}\) is the ground-level tritium concentration in the air \((\mathrm{Bq/m^3})\); \(Q\) is the radioactivity of pollutants in the puff \((\mathrm{Bq})\); \(\sigma_x, \sigma_y, \sigma_z\) represent the dispersion coefficients \((\mathrm{m})\) in the downwind, crosswind and vertical directions, respectively; \(d_x, d_y\) are the distance from the puff center to the receptor point in the downwind and crosswind directions \((\mathrm{m})\); \(g\) is the vertical term in the Gaussian formula \((\mathrm{m})\); \(H_e\) is the effective height of the puff center above the ground \((\mathrm{m})\); \(h\) is the mixed-layer height \((\mathrm{m})\); \(i\) is the number of puff reflection by the mixed-layer.

In order to assess the tritium concentration based on the above atmospheric dispersion method, some essential data are needed such as tritium source term, meteorological data, topographical data, as well as release height, etc. The meteorological and topographical data was obtained from the U.S. National Oceanic and Atmospheric Administration (NOAA) database and U.S. Geological Survey (USGS) database, respectively. Tritium release source term and release height were assumed to be \(3.57 \times 10^{14}~\mathrm{Bq/a}\) and \(70~\mathrm{m}\), respectively [21]. Notably, the buoyancy effect could be ignored during tritium atmospheric dispersion as the mass fraction of tritium in the effluents is very low under normal discharge condition.

#### 3.2.2. Soil diffusion model of HT

Aiming at HT transfer in the atmosphere-soil interface, classical advection-dispersion equation showed in Eq. (4) was adopted to calculate HT concentration in the gas-phase of shallow soil. The difference of HT dispersion between continuous media and porous media depends on the selection of dispersion coefficients. Generally, molecular diffusion in the porous media can be estimated by Eq. (5) from the molecular diffusion coefficient in free air [30]. Due to the influence of wind flow, the dispersion coefficients in porous media includes the sum of molecular diffusion coefficient and wind-induced dispersion coefficient. In this case Eq. (4) could be reduced to Eq. (6).

\[
\frac{\partial C_{a,HT}}{\partial t} = D_x \frac{\partial^2 C_{a,HT}}{\partial x^2} + D_y \frac{\partial^2 C_{a,HT}}{\partial y^2} + D_z \frac{\partial^2 C_{a,HT}}{\partial z^2} - w \frac{\partial C_{a,HT}}{\partial x} - R_1 \quad (4)
\]

\[
D_z = 0.66 \epsilon D_0 \quad (5)
\]

\[
\frac{\partial C_{s,HT}}{\partial t} = D_x \frac{\partial^2 C_{s,HT}}{\partial x^2} + D_y \frac{\partial^2 C_{s,HT}}{\partial y^2} + (D_z + D_w) \frac{\partial^2 C_{s,HT}}{\partial z^2} - R_1 \quad (6)
\]

where, \(C_{s,HT}\) is the HT concentration in the air between soil voids \((\mathrm{Bq/m^3})\); \(w\) is the flow velocity of the air between soil voids \((\mathrm{m/s})\), which is influenced by the air flow above the soil; \(D_x\) is the longitudinal dispersion coefficients \((\mathrm{m^2/s})\); \(D_y\) and \(D_z\) are transverse dispersion coefficients in \(y\) and \(z\) directions, respectively \((\mathrm{m^2/s})\); \(R_1\) is the sink term such as oxidation and decay loss of HT \((\mathrm{Bq/(m^3\cdot s)})\); \(\epsilon\) is the gas-filled porosity which is the total porosity for the porous media with no liquid phase; \(D_0\) is the molecular diffusion coefficient of HT in the free air, referred to hydrogen diffusion in the air \((6.5 \times 10^{-5}~\mathrm{m^2/s})\); \(D_w\) is the wind-induced dispersion coefficient \((\mathrm{m^2/s})\).

#### 3.2.3. Migration and evapotranspiration model of conversion product

After obtaining the HT concentration distribution in the air-phase of the porous media, the accumulated HTO production could be solved by Eq. (7). It is a confusing issue that whether the conversion product exists in gas-phase or liquid-phase of the soil, which has a significant influence on tritium concentration distribution. When assuming gaseous-phase fraction of HTO as \(\alpha\), HTO in the air-filled porosity soil could be described by Eq. (8) and Eq. (9). For the other HTO in the water-filled porosity, initial HTO was calculated by Eq. (10). Then, HTO concentration distribution in the soil could be calculated by jointly solving the Richards Eq. (11), convection-dispersion Eq. (12) for solute transport, as well as the plant root water uptake Eq. (13). Re-emission flux of HTO from shallow soil or plant leaves to the air could be calculated by Eq. (14). The near-surface HTO concentration distribution could be predicted by classical advection-dispersion Eq. (15).

\[
C_{SAHTO} = \int C_{s,HT} f_{ext} dt \quad (7)
\]

\[
C_{SgHTO} = \alpha \cdot C_{SAHTO} \quad (8)
\]

\[
\frac{\partial C_{SgHTO}}{\partial t} = D_x \frac{\partial^2 C_{SgHTO}}{\partial x^2} + D_y \frac{\partial^2 C_{SgHTO}}{\partial y^2} + (D_z + D_w) \frac{\partial^2 C_{SgHTO}}{\partial z^2} \quad (9)
\]

\[
C_{SlHTO} = \frac{m \cdot (1 - \alpha) \cdot C_{SAHTO}}{n} \quad (10)
\]

\[
\frac{\partial \theta}{\partial t} = \frac{\partial}{\partial z} \left[ K \left( \frac{\partial h}{\partial z} + \cos A \right) \right] - R_2 \quad (11)
\]

\[
\frac{\partial (\theta C_{SlHTO})}{\partial t} = \frac{\partial}{\partial z} \left( \theta D_s \frac{\partial C_{SlHTO}}{\partial z} \right) - \frac{\partial (q C_{SlHTO})}{\partial z} - \lambda \theta C_{SlHTO} - R_3 \quad (12)
\]

\[
S_p(z,t) = \alpha_p(h,z) \beta(z) T_p \quad (13)
\]

\[
\phi_{s,HTO - a,HTO} = V_{diff} \cdot C_{SgHTO} + V_{eva} \cdot C_{SlHTO} \quad (14)
\]

\[
\frac{\partial C_{a,HTO}}{\partial t} = D_a \frac{\partial^2 C_{a,HTO}}{\partial x^2} - U \frac{\partial C_{a,HTO}}{\partial x} \quad (15)
\]

where, \(f_{ext}\) is the HT oxidation constant in the soil \((\mathrm{h^{-1}})\); \(C_{SAHTO}\) is the accumulated HTO, as air-phase, concentration in the soil produced by oxidation behavior \((\mathrm{Bq/m^3})\); \(C_{SgHTO}\) is the gaseous state HTO concentration in the gas-filled porosity of soil \((\mathrm{Bq/m^3})\); \(\alpha\) is gaseous fraction of oxidation products; \(C_{SlHTO}\) is the accumulated HTO, as liquid-phase, concentration in the soil produced by oxidation behavior \((\mathrm{Bq/L})\); \(m\) is gas-phase volume per soil volume \((\mathrm{m^3/m^3})\); \(n\) is moisture content per soil volume \((\mathrm{L/m^3})\); \(\theta\) is the volumetric water content; \(h\) is the water pressure head \((\mathrm{m})\); \(A\) is the angle between the flow direction and the vertical axis; \(R_2\) is the sink term for root water uptake; \(D_s\) is the hydrodynamic dispersion coefficient; \(q\) is the volumetric flux density; \(\lambda\) is the radioactive decay constant; \(R_3\) is the sink term for root tritium uptake; \(\alpha_p(h,z)\) is the dimensionless root-water uptake water stress response function; \(\beta(z)\) is the spatial root distribution function; \(T_p\) is the potential transpiration rate; \(U\) is the wind velocity \((\mathrm{m/s})\); \(D_a\) is diffusion coefficients of HTO in the air \((\mathrm{m^2/s})\); \(C_{a,HTO}\) is HTO concentration in the air above the soil \((\mathrm{Bq/m^3})\).

Finite element method was adopted to solve the above numerical equations. Key processes and mesh construction for tritium behaviors in the atmosphere-soil compartment were shown in Fig. 3. Tritium migration in water-filled and air-filled porosity of soil were separately calculated with the spatial resolutions of approximately \(1~\mathrm{cm}\).

> **Fig. 3.** Key processes and mesh construction for tritium behaviors in the atmosphere-soil compartment.  
> a) Mesh construction for migration calculation of tritium in water-filled soil porosity;  
> b) Key processes of tritium behaviors in the atmosphere-soil compartment;  
> c) Mesh construction for diffusion calculation of tritium in air-filled soil porosity.

### 3.3. Study area and essential parameters

Some realistic environmental parameters are essential to predict the time-varying atmosphere-soil behaviors associated with tritium discharge. Ergo, realistic study area should be selected. Previous study showed atmospheric HTO and HT concentration measure values were in the same level in the vicinity of Tokai reprocessing plant, Japan [31]. Similar characteristic was also found in the vicinity of Qinshan nuclear power base, China [32]. While these studies failed to report the detailed HT discharge source data. Qinshan nuclear power base was selected in this study to predict tritium atmosphere-soil behaviors based on the above numerical method. Unit gram per year tritium was assumed as the release source term. Generally, tritium concentration distribution is in direct proportion to release source term. Thus, the assumed release source term has no effect on the migration and transformation behaviors. Other essential input parameters were summarized in Table 2.

---

**Table 2 Summary of key input parameters to estimate tritium distribution.**

| Module | Key input parameters | Value |
|---|---|---|
| Atmospheric dispersion | Assumed tritium discharge source term | \(3.57 \times 10^{14}~\mathrm{Bq/a}\) |
| | Release height | \(70~\mathrm{m}\) |
| | Time-varying meteorological data | U.S. National Oceanic and Atmospheric Administration (NOAA) database; Hourly-resolution |
| | Topographical data | U.S. Geological Survey (USGS) database; 3 arc-seconds (Spatial-resolution) |
| Pulse air tritium | Concentration | \(1~\mathrm{Bq/m^3}\) (30 min) |
| Steady air tritium | Concentration | \(1~\mathrm{Bq/m^3}\) |
| HT Oxidation rate | | \(1.6 \times 10^{-4}~\mathrm{s^{-1}}\) |
| Air-filled porosity | | 0.14 (0-30 cm); 0.32 (30-100 cm) |
| Volumetric soil water content | | — |
| Diffusion coefficient of gaseous tritium | | \(6.5 \times 10^{-5}~\mathrm{m^2/s}\) |
| α | | 0.1, 0.5, 0.9 |
| Meteorological data | Precipitation rate | Daily-resolution |
| | Evaporation rate | Daily-resolution |
| | Leaf area index | 1.62 |
| | Wind velocity and near-surface distribution | \(1.62~\mathrm{m/s}\) at 10 m height |

---

## 4. Results and discussion

A computational domain measuring \(160 \times 160~\mathrm{km}\) was selected with the release point as the center. Tritium concentration distribution in the air around the release point could be solved and shown in Fig. 3 driven by the hourly-resolution wind field. The plume trajectory shows that annual average tritium concentration mainly depends on wind direction. Most of tritium would distribute in the SSE direction of discharge point according to annual average data. Tritium distribution characteristics for four seasons were also shown in Fig. 4. Additionally, tritium concentration in the atmosphere is approximate to below \(10~\mathrm{Bq/m^3}\). In order to perform subsequent simulation, time-varying tritium concentration at the point of \(77.8~\mathrm{km}\) in the SN direction and \(79.7~\mathrm{km}\) in the WE direction was obtained with \(1.66~\mathrm{km}\) away from the discharge point and an annual average value of \(1~\mathrm{Bq/m^3}\). The instantaneous value at this point changes with wind field data and the peak value is below \(10~\mathrm{Bq/m^3}\).

> **Fig. 4.** Near-surface tritium distribution around the nuclear power base driven by hourly-resolution meteorological data and topographical data.  
> a) Meteorological characteristics of the selected site;  
> b) Contour map of atmospheric tritium concentration distribution;  
> c) Day-solution atmospheric tritium concentration of selected point.

### 4.2. Tritium concentration in the soil moisture for HTO discharge source

Atmosphere-soil behaviors for HTO discharge source were investigated firstly to make a comparison with HT discharge source. Based on day-solution atmospheric tritium concentration shown in Fig. 4c, HTO concentration distribution in soil moisture was calculated and shown in Fig. 5a by adopting day-resolution meteorological data when assuming tritium stack discharge in the form of HTO. In the first 100 days, tritium level is lowest among the whole year owning to the low atmospheric tritium concentration as tritium flow by other wind direction, as well as initial unbalance state in the calculating scheme. Subsequently, tritium concentration increases from several \(\mathrm{Bq/L}\) to more than \(100~\mathrm{Bq/L}\). The calculation results are slightly higher than the field measurement level (tens of \(\mathrm{Bq/L}\)) owning the assumed higher annual tritium discharge amount [33]. For instance, the publicly available data of gaseous HTO discharge amount during 2022 is \(1.078 \times 10^{14}~\mathrm{Bq/a}\), one third of assumed value in this calculation. Another characteristic is that obvious fluctuation of HTO concentration appears in the shallow soil such as 5 cm of soil depth which indicates that HTO concentration in the shallow soil is easily influenced by the precipitation and evaporation factors.

> **Fig. 5.** Daily-solution HTO concentration in the soil moisture and statistical analyses for transfer fraction of HTO within the depth of \(100~\mathrm{cm}\).  
> a) HTO concentration in soil moisture at different depth;  
> b) Transfer fraction of HTO in soil moisture in the whole year within the depth of \(100~\mathrm{cm}\);  
> c) Relationship between infiltration fraction and ratio of precipitation and evapotranspiration under different years.

Statistical analyses relating to transfer fraction of HTO in soil moisture within the depth of \(100~\mathrm{cm}\) was further conducted and shown in Fig. 5b. It was indicated \(62.4\%\) of HTO in soil moisture migrates into the deeper soil along with water flow in the whole year. Transfer fractions by evaporation into atmosphere and root uptake are \(21.8\%\) and \(15.8\%\) respectively. In order to discuss the HTO migration behavior in the soil under different meteorological conditions, HTO evapotranspiration behavior into the air was further evaluated based on the measurement precipitation-evapotranspiration data from 2009 to 2023. Tritium in the soil within the depth of \(100~\mathrm{cm}\) could migrate into the deeper soil, evaporation into the air and root-uptake by plants. When regarding the sum of infiltration fraction and evapotranspiration fraction is \(100\%\), evapotranspiration fraction includes the re-emission fraction from soil and plants was calculated and shown in Fig. 5c which indicated that more than \(62\%\) tritium would go into the deeper soil owing to the high ratio of precipitation and evapotranspiration. A linear relationship showed in Eq. (16) exists between the evapotranspiration fraction and ratio of precipitation and evapotranspiration. This equation could be used to evaluate the average re-emission fraction meaning that an accurate result could still be obtained if the total annual precipitation and evapotranspiration data is available.

\[
f_{evt} = 0.56 - 0.12 r \quad (16)
\]

where, \(f_{evt}\) is the HTO evapotranspiration fraction; \(r\) is the ratio of precipitation and evapotranspiration.

### 4.3. Tritium concentration distribution in the soil for HT discharge source

#### 4.3.1. HT concentration distribution in the soil air-filled porosity

Dynamic HT diffusion behavior in soil air-filled porosity was simulated for case I and case II, respectively. Wind velocity was assumed to be \(1.62~\mathrm{m/s}\) at the height of \(10~\mathrm{m}\) [34]. The case I means HT concentration in the air last \(30~\mathrm{min}\). It was indicated from the Fig. 6a that HT concentration in the soil porosity with the depth of \(5~\mathrm{cm}\) and \(20~\mathrm{cm}\) could reach the peak value after exposure \(25~\mathrm{min}\) and \(30~\mathrm{min}\), respectively. For the depth of \(50~\mathrm{cm}\) and \(100~\mathrm{cm}\), the peak values reach at the moment of \(38~\mathrm{min}\) and \(83~\mathrm{min}\), respectively. After the pulse exposure, HT concentration at the shallow soil decreases faster than the deep soil because of the wind flow and high conversion rate. It was indicated from Fig. 6b that HT concentration in the shallow soil is higher than that in the deep soil owning to the constant HT exposure. The steady HT concentration at the depth of \(100~\mathrm{cm}\) is \(60\%\) of HT concentration at \(5~\mathrm{cm}\) for case II.

> **Fig. 6.** HT concentration distribution in the soil air-filled porosity with different depth.  
> a) Case I (pulse exposure);  
> b) Case II (steady exposure).

#### 4.3.2. HTO concentration distribution in the soil air-filled porosity

Dynamic HTO concentration distribution in soil air-filled porosity with different depth was calculated and shown in Fig. 7 when assuming HT conversion rate and \(\alpha\) to be \(1\% / \mathrm{min}\) and 0.1, respectively. For case I, peak value of gaseous HTO concentration in the soil porosity could reach \(10^{-3}~\mathrm{Bq/m^3}\). Gaseous HTO concentration in the soil porosity decreases quickly owing to convection-diffusion of wind above the soil. Additionally, HTO concentration in the deep soil would be larger than that in shallow soil owing to the both low gas porosity fraction in the deep soil and strong diffusion in the shallow soil. The low gas porosity fraction in the deep soil means that few gaseous HTO could downward migrate by the diffusion pathway. For case II, HTO concentration in the soil porosity could reach a constant value which means production by conversion equal to loss by diffusion. It is noting to mention that the steady state mainly depends on HT conversion rate and wind profile. In the realistic soil environment, gaseous HTO could still transfer into the soil moisture. This factor was treated as the value of \(\alpha\). Mechanism experiment should be performed to identify this process and the obtain the transfer data.

> **Fig. 7.** HTO concentration distribution at different depth in the soil air-filled porosity.  
> a) Case I (pulse exposure);  
> b) Case II (steady exposure).

#### 4.3.3. HTO concentration distribution in the soil moisture

The initial HT source was also assumed to be a \(1~\mathrm{Bq/m^3}\) air pulse exposure lasting \(30~\mathrm{min}\). \(90\%\) of conversion product distributes in soil moisture (\(\alpha = 0.1\)). Migration behavior of HTO in the soil moisture as the conversion product was simulated and shown in Fig. 8. HTO radioactivity in the air-filled porosity can diffuse and decrease quickly according to Fig. 7a. Contrastingly, HTO in the water-filled porosity migrate relatively slow. In order to investigate migration behavior of HTO in water-filled porosity, accumulation value during the short period reaching steady state was used as the initial value to perform the calculation. It was indicated from Fig. 8a and Fig. 8b that the initial accumulation HTO concentration are in the \(10^{-6} \sim 10^{-3}~\mathrm{Bq/L}\) in the unsaturated soil within the depth of \(100~\mathrm{cm}\). HTO in soil moisture would migrate along with the dynamic precipitation and evapotranspiration factors. For the depth of \(5~\mathrm{cm}\), HTO concentration decreases from \(10^{-3}\) to \(10^{-9}~\mathrm{Bq/L}\) by the factors of precipitation and plant root uptake according to Fig. 8c. HTO concentration could also slightly increase at some specific days, such as 50-75 days, 200-225 days. The reason is that there is almost no precipitation for these days. HTO in the deep soil with high concentration would migrate from down to up due to the evaporation factor. However, the evaporation factor only influences the HTO concentration level in the shallow soil. For the HTO concentration at other depth of soil moisture, the decrease velocity is relatively low compared with that at depth of \(5~\mathrm{cm}\). HTO concentration is almost constant during 50-75 and 260-325 days as precipitation rate is very low during these days. Thus, precipitation is a dominant factor with regard to HTO migration to deep soil moisture.

> **Fig. 8.** HTO concentration distribution at different depth of soil moisture and transfer behavior.  
> a) HTO concentration distribution at different depth for case I;  
> b) Accumulation value as the initial HTO concentration distribution at different depth;  
> c) Dynamic HTO concentration distribution in the soil moisture with the consideration of precipitation and evaporation factors;  
> d) Dynamic transfer fraction of HTO in the soil moisture.

Statistical analysis for HTO transfer fraction was conducted and shown in Fig. 8d. It was indicated that evaporation fraction increased quickly in the first 50 days owning to high HTO concentration distribution in soil moisture and weak precipitation. Subsequently, the infiltration fraction increases along with heavy precipitation during the 75-200 days. Plant root uptake fraction is low in this calculation from the following reasons. The strong transpiration period appears in 120-300 days. Thus, a slightly increase appears since the 100th day. After that, tritium concentration in the soil moisture decreases by several orders of magnitude compared to the initial soil tritium level. Root uptake fraction is still low even under strong transpiration period since the 150th days. Transfer fraction reach steady state in the 150th day due to the low tritium concentration level in soil moisture as well.

#### 4.3.4. Discussion on effects of key parameters

Regarding the above simulation, considerable uncertainty exists in some key parameters such as soil conversion rate of HT, gaseous fraction \(\alpha\) of conversion product. Both the parameters have a proud influence on time-varying tritium concentration distribution in the soil, re-emission source in particular. The effects of the key parameters on soil behaviors of tritium were discussed as follows.

Considering significant uncertainty for conversion rate of HT in the soil, HTO concentration level in both soil porosity and moisture was evaluated and shown in Fig. 9a when assuming the conversion rate to be \(1\% / \mathrm{min}\) and \(0.1\% / \mathrm{min}\), respectively. It was indicated that conversion product is positive correlation with conversion rate.

Before the discussion on effects of gaseous fraction \(\alpha\) of conversion product, a consensus has been that HTO concentration in the air-filled porosity in the soil decreases faster than that in the water-filled porosity in the soil according to the studies shown in Fig. 7a and Fig. 8c. Ergo, most of the conversion product would re-emit into the atmosphere quickly under high \(\alpha\) condition according to Fig. 9b. The re-emission fraction is relatively high as the gaseous HTO is hard to migrate into the deep soil with extremely low air-filled porosity. Contrastingly, HTO in soil moisture can have a long-time retention depending on soil water flow under low \(\alpha\) condition. The total re-emission fraction at this case would be low owing to infiltration into the deeper soil by heavy precipitation shown in Figs. 5 and 8d.

Both HT conversion rate in the soil and gaseous fraction \(\alpha\) of conversion product are dominant factors in estimating HT atmosphere-soil behaviors. Previous studies have usually reported the conversion rate and seldom discussed the effects of physical state of conversion product. More experiments should be performed to reveal the HT migration and conversion mechanism in the soil. For instance, building the relations of conversion rates and environmental factors, identification of gaseous fraction \(\alpha\) of conversion product, etc. Additionally, Experimental measurement accuracy for multi-form tritium is also needed and important for identifying tritium atmosphere-soil behaviors and achieving accurate dose assessment.

> **Fig. 9.** Effects of key factors.  
> a) Conversion products concentration in soil moisture and porosity under different conversion rate;  
> b) HTO re-emission fraction under different \(\alpha\).

---

## 5. Conclusions

This study addresses time-varying atmosphere-soil behavior due to tritium discharge. A simulation frame was proposed involving atmospheric dispersion driven by hourly-resolution wind field data, soil porosity diffusion of gaseous tritium, conversion of HT by bacterial oxidation and isotope exchange, soil migration in both air-filled and water-filled porosity, as well as re-emission into the near-surface atmosphere. Fine-resolution simulation and discussion for tritium migration in the atmosphere-soil compartments were performed. The main findings are:

1) HTO level in soil moisture significantly depends on the precipitation and evapotranspiration rate apart from HTO discharge source term and wind field. For the selected nuclear power case in this study, predictive value by the numerical modeling is roughly estimated to fit well with the measurement data.

2) HTO evapotranspiration fraction into atmosphere depends on the ratio of precipitation and evapotranspiration. Relationship of \(f_{evt} = 0.56 - 0.12 r\) was proposed and could be used to predict HTO re-emission into the air through realistic average precipitation and evapotranspiration rate data.

3) For HT instantaneous discharge, tritium concentration in the shallow soil reaches the peak level quickly and decreases faster owing to the wind profile. While tritium concentration in the deep soil changes relatively flat and higher than that in shallow soil after a period of migration.

4) Environmental factors such as soil conversion rate of HT and gaseous fraction \(\alpha\) of conversion product have significant effects on atmosphere-soil behavior of tritium for the HT discharge source term.

Numerical method driven by high-resolution environmental factors is beneficial to achieve an accurate environmental impact assessment. Additionally, experiments with high measurement accuracy is crucial for determining the key data such as \(\alpha\) and conversion rate, as well as the key processes from the viewpoint of time series.

---

## CRediT authorship contribution statement

**Baojie Nie**: Writing - original draft, Investigation, Conceptualization.  
**Haoyang Wu**: Methodology, Investigation, Data curation.  
**Yiling Ran**: Software, Methodology.  
**Dezhong Wang**: Writing - review & editing, Supervision.

---

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

---

## Acknowledgement

This work was supported by the National Natural Science Foundation of China (Grant No. 12375314).

---

## Data availability

Data will be made available on request.

---

## References

[1] R. Skelton, X. Zhou, R. Karnesky, Molecular dynamics studies of lattice defect effects on tritium diffusion in zirconium, *J. Nucl. Mater.* 555 (2021) 153099.  
[2] J. Zhang, D. Yang, L. Li, et al., Research on gaseous and liquid source term of tritium for pressurized water reactor, *Nucl. Eng. Des.* 426 (2024) 113367.  
[3] L. Candido, C. Alberghi, M. Utili, Design of a hydrogen/tritium permeation sensor for Gen-IV sodium fast reactors, *Vacuum* 191 (2021) 110414.  
[4] W. Cheng, J. Liang, M. Zhang, et al., Radiation dose assessment of tritium released from the thorium molten salt reactor, *Nucl. Sci. Eng.* 197 (2023) 1534-1544.  
[5] M. Nishikawa, T. Kinjyo, Y. Nishida, Chemical form of tritium released from solid breeder materials, *J. Nucl. Mater.* 325 (2004) 87-93.  
[6] Y. Dai, X. Zheng, P. Ding, Review on sodium corrosion evolution of nuclear-grade 316 stainless steel for sodium-cooled fast reactor applications, *Nucl. Eng. Technol.* 53 (2021) 3474-3490.  
[7] W. Luscher, D. Senor, K. Clayton, In situ measurement of tritium permeation through stainless steel, *J. Nucl. Mater.* 437 (2013) 373-379.  
[8] M. Abdou, M. Riva, A. Ying, et al., Physics and technology considerations for the deuterium-tritium fuel cycle and conditions for tritium fuel self-sufficiency, *Nucl. Fusion* 61 (2021) 013001.  
[9] T. Kong, S. Kim, Y. Lee, et al., Radioactive effluents released from Korean nuclear power plants and the resulting radiation doses to members of the public, *Nucl. Eng. Technol.* 49 (2017) 1772-1777.  
[10] S. Kenjo, S. Yokoyama, K. Ochiai, et al., Tritium atmospheric dispersion modelling code, ROPUCO, for A-FNS risk assessment, *Fusion Eng. Des.* 208 (2024) 114653.  
[11] K. Namba, R. Kasada, S. Konishi, et al., Evaluation of tritium transport in the biomass-fusion hybrid system and its environmental impact, *Fusion Eng. Des.* 98-99 (2015) 2162-2165.  
[12] M. Ferreira, A. Turner, E. Vernon, et al., Tritium: its relevance, sources and impacts on non-human biota, *Sci. Total Environ.* 876 (2023) 162816.  
[13] S. Kim, M. Bredlaw, H. Rousselle, et al., Determination of the baseline tritium concentrations (HTO, TFWT and OBT) in soil and plants in Ontario, Canada, *J. Environ. Radioact.* 243 (2022) 106810.  
[14] B. Nie, S. Fang, M. Jiang, et al., Anthropogenic tritium: inventory, discharge, environmental behavior and health effects, *Renew. Sustain. Energy Rev.* 135 (2021) 110188.  
[15] K. Chae, G. Kim, Dispersion and removal characteristics of tritium originated from nuclear power plants in the atmosphere, *J. Environ. Radioact.* 192 (2018) 524-531.  
[16] K. Furuichi, K. Katayama, H. Date, et al., Tritium sorption behavior on the percolation of tritiated water into a soil packed bed, *Fusion Eng. Des.* 109-111 (2016) 1371-1375.  
[17] H. Renard, O. Connan, S. Dizes, et al., Experimental measurements of the bacterial oxidation of HT in soils: impact over a zone influenced by an industrial release of tritium in HT form, *J. Environ. Radioact.* 242 (2022) 106779.  
[18] B. Feng, W. Zhuo, Levels and behaviors of environmental tritium in East Asia, *Nucl. Sci. Tech.* 33 (2022) 86.  
[19] D. Chen, B. Nie, B. Dong, et al., Insights into near-surface distribution characteristics of multi-form tritium with consideration of atmospheric buoyancy and gravitational deposition, *Chemosphere* 312 (2023) 137231.  
[20] M. Ichimasa, Y. Ichimasa, Y. Azuma, et al., Oxidation of molecular tritium by surface soils, *J. Radiat. Res.* 29 (1988) 144-151.  
[21] B. Nie, S. Wu, D. Yang, et al., Quantitative prediction of dynamic HTO migration behavior in the soil and non-negligible evapotranspiration effect, *J. Hazard. Mater.* 425 (2022) 127772.  
[22] S. Kim, N. Baglan, P. Davis, Current understanding of organically bound tritium (OBT) in the environment, *J. Environ. Radioact.* 126 (2013) 83-91.  
[23] C. Burnham, R. Brown, G. Ogram, et al., An overview of experiments at Chalk River on HT dispersion in the environment, *Fusion Technol.* 14 (1988) 1159-1164.  
[24] M. Ichimasa, Y. Ichimasa, Y. Yagi, et al., Oxidation of atmospheric molecular tritium in plant leaves, lichens and mosses, *J. Radiat. Res.* 30 (1989) 323-329.  
[25] J. McFarlane, R. Rogers, D. Bradley, Environmental tritium oxidation in surface soil, *Environ. Sci. Technol.* 12 (1978) 590-593.  
[26] J. McFarlane, R. Rogers, D. Bradley, Tritium oxidation in surface soil, A survey of soils near five nuclear fuel reprocessing plants, *Environ. Sci. Technol.* 13 (1979) 607-608.  
[27] M. Ichimasa, M. Suzuki, H. Obayashi, et al., In vitro determination of oxidation of atmospheric tritium gas in vegetation and soil in Ibaraki and Gifu, Japan, *J. Radiat. Res.* 40 (1999) 243-251.  
[28] S. Kim, M. Stuart, M. Bredlaw, et al., HT to HTO conversion and field experiments near Darlington Nuclear Power Generating Station (DNPGs) site, *J. Environ. Radioact.* 132 (2014) 73-80.  
[29] L. Yang, S. Fang, S. Zhuang, et al., Atmospheric \(^{137}\mathrm{Cs}\) dispersion following the Fukushima Daiichi nuclear accident: local-scale simulations using CALMET and LAPMOD, *Ann. Nucl. Energy* 195 (2024) 110137.  
[30] A. Pourbakhtiar, T. Poulsen, S. Wilkinson, et al., Effect of wind turbulence on gas transport in porous media: experimental method and preliminary results, *Eur. J. Soil. Sci.* 68 (2017) 48-56.  
[31] H. Fujita, Y. Kokubun, J. Koarashi, Environmental tritium in the vicinity of Tokai reprocessing plant, *J. Nucl. Sci. Technol.* 44 (2007) 1474-1480.  
[32] Q. Xu, L. Qin, Z. Xia, et al., Distribution of atmospheric multi-forms tritium in the vicinity of Qinshan nuclear power plants, *Nucl. Tech.* 42 (2019) 070601.  
[33] F. Guo, W. Wu, Y. Feng, et al., Distribution of tritium concentration in the 0-25 cm surface soil of cultivated and uncultivated soil around the Qinshan nuclear power plant in China, *Appl. Radiat. Isotopes* 164 (2020) 109311.  
[34] F. Li, Z. Xie, Y. Yang, et al., Investigations of synoptic wind profile patterns in complex urban areas based on LiDAR measurements, *Build. Environ.* 242 (2023) 110573.

---