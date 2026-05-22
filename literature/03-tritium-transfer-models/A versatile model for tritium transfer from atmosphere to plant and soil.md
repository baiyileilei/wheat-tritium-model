# A versatile model for tritium transfer from atmosphere to plant and soil

A. Melintescu and D. Galeriu

National Institute for Physics and Nuclear Engineering "Horia Hulubei", Life and Environmental Physics Department, 407 Atomistilor St., Bucharest-Magurele, POB MG-6, 077125, Romania

**Abstract.** The need to increase the predictive power of risk assessment for large tritium releases implies a process level approach for model development. Tritium transfer from atmosphere to plant and the conversion in organically bound tritium depend strongly on plant characteristics, season, and meteorological conditions. In order to cope with this large variability and to avoid also, expensive calibration experiments, we developed a model using knowledge of plant physiology, agrometeorology, soil sciences, hydrology, and climatology. The transfer of tritiated water to plant is modelled with resistance approach including sparse canopy. The canopy resistance is modelled using Jarvis-Calvet approach modified in order to directly use the canopy photosynthesis rate. The crop growth model WOFOST is used for photosynthesis rate both for canopy resistance and formation of organically bound tritium, also. Using this formalism, the tritium transfer parameters are directly linked to known processes and parameters from agricultural sciences. The model predictions for tritium in wheat are closed to a factor two to experimental data without any calibration. The model also is tested for rice and soybean and can be applied for various plants and environmental conditions. For sparse canopy the model uses coupled equations between soil and plants.

## 1. INTRODUCTION

There are three phases in the dynamics of tritium in SVAT (soil-vegetation-atmosphere transport). The first one treats the period of active deposition when the cloud of tritiated water travels the study area and the atmospheric concentration is the driving source of tritium. The last one starts few days after cloud passage, when the soil water tritium is the driving force. The middle stage takes care of the reemission of HTO from vegetation and surface soil into the atmosphere, a fast process immediately after cloud passage, slowing down later. The active and transition phase are sensitive to actual meteorological parameters (sunshine, humidity, temperature, and rainfall) as were as on plant physiological characteristics and growth stage. In the later stage the processes to be considered are movement of tritiated water in root soil, depth distribution of roots, evapotranspiration and plant photosynthesis. This can be modeled with a slow dynamics, using climatic data and approximate dynamics of some plant parameters. After an atmospheric dry deposition episode the tritiated water concentration in plant is decreasing fast, while the OBT concentration in whole plant will decrease very slow but will be translocated to storage plant parts. For crops harvested one time in the year, most of tritium in the harvested plant will be in form of OBT, while for continuously harvested plants as grass and leafy vegetable, in the first few days after the accident, the concentration of HTO is high. An operational model must include both situations under various agrometeorological conditions. The well-known model UFOTRI was built to cope with these requirements and sensitivity and uncertainty has been analysed [1] showing reliability for maximum exposed individual (worse case) as required for a facil design and licencing. This study and discussions in the IAEA-EMRAS Tritium group pointed also that some processes can be of variable importance in a different context and that more research is needed for case application in accident preparedness and management. Photosynthesis and partitioning of newly formed dry matter are basic processes driving tritium transfer. We have demonstrated previously [2] that the WOFOST crop growth model: (i) gives predictions comparable with more complex specific species photosynthesis models; (ii) can describe C3 and C4 plant growth under various climatic conditions. The application of the WOFOST crop model to derive tritium transfer from atmosphere to plants is reported here with an extension of the SVAT model for tritium including sparse canopies.

## 2. THE RESISTANCE APPROACH FOR TRITIUM TRANSFER ATMOSPHERE-SOIL-PLANT

The driving equation for the transfer of HTO from atmosphere to leave is:

\[
\frac{dC}{dt} = \frac{V_{exc}}{M_w} (C_{air} - 0.91\rho C) + \frac{V_{exc}}{M_w} (\rho_s - \rho)C_s \quad (1)
\]

with:

- \(C\) - HTO concentration in plant water (mainly leaf water) (Bq / kg)
- \(C_{air}\) - HTO concentration in air (Bq / m³)
- \(C_s\) - HTO concentration in the sap water (transpiration water), resulting from water extraction of roots at different depths (Bq / kg)
- \(\rho_s\) - saturated air humidity at vegetation temperature (kg / m³)
- \(\rho\) - air humidity at reference level (kg / m³)
- \(M_w\) - mobile water mass in vegetation leaves on a unit soil surface (kg / m²)
- \(V_{exc}\) - exchange velocity atmosphere to canopy (m / s)

The above equation is used for all canopy, ignoring the transfer of air HTO to stream, as the exchange velocity is smaller with one order of magnitude. Initial diffusion of leaf water to steam is also ignored due to the slow velocity and the flushing of steam by sap flux with definitely less HTO concentration in the active phase. In the transition period, steam water and leaf water equilibrate gradually with root soil water and we ignored the details of this period for steam due to minor contribution to plant water concentration. The last term in equation (1) includes in fact the transpiration flux. In order to assess the HTO concentration in sap water, the tritium dynamics in soil and rooting characteristic must be known. At the soil surface we have:

\[
\frac{dC_{w,t}}{dt} = \frac{V_{ex,s}}{M_{ws}} (C_{air} - 0.91\rho_{sat}(T_s)C_{w,t}) - DF \quad (2)
\]

where:

- \(C_{sw,1}\) - HTO concentration in the first soil layer at the interface with in-canopy air (Bq / kg)
- \(V_{ex,s}\) - exchange velocity in-canopy atmosphere to soil (m / s)
- \(\rho_{sat}(T_s)\) - saturated air humidity at soil surface temperature (kg / m³)
- \(M_{ws}\) - mass of water in the surface soil layer
- DF - net flux of HTO at the bottom interface of the first soil layer

The exchange velocity from atmosphere to plant depends on canopy resistance, while the exchange velocity from atmosphere to soil depend on soil resistance. We will discuss in more details both resistances.

### 2.1 Soil resistance \(R_s\)

While for maximum possible exposure the soil-plant pathway has little contribution to the ingestion dose [1], for other situations it can contribute more than 50%. The flux from atmosphere to soil strongly depends on so called "soil resistance", a semi-empirical quantity to avoid modeling of very complex processes. There is a tremendous amount of various expressions of soil resistance [3] spanning orders of magnitude and having limited applicability. To be able to have a more general parameterization, we analyzed experimental data obtained by Kondo [4] and observed some regularities linked with soil properties. Eventually we obtained a unique relationship as:

... (text continues with detailed derivation)

Working on this expression we used the well known relation \(R_d = A_{m,g} / 9\) and we observed that \(A_{min} = 4.7 / A_{m,g}\) using the initial Jacobs expressions and parameters. We obtain a condensed formula.

Finally, the water vapor conductance is obtained, with the correction due to evaporation, as in Jacobs [5]. In our context, we can ignore the variation of CO₂ concentration in the canopy, affecting \(C_s\) and we can integrate the above expression on the whole canopy height. This gives the canopy conductance as function of canopy gross photosynthetic rate. In spite of using the Jacobs leaf photosynthesis expression, with unknown plant specific parameters, we can now use the canopy gross photosynthetic rate as given in the WOFOST crop growth model when a large database for European crop exists [7]. The other parameters needed, namely \(f_o\) and \(D_{max}\) are kept at recommended values for C3 and C4 plants. We have the following comparison between model results and observations of maximum stomatal resistance:

**Table 1. Comparison between experimental and theoretical data for maximum stomatal resistance.**

| Plant type | Experimental val. (s/m) | Theoretical val (s/m) | References |
| :--- | :--- | :--- | :--- |
| Wheat, vegetative stage | 41 – 52 | 56 | Baldocchi, 1994 |
| Wheat, anthesis | 62 – 100 | 60 | Baldocchi, 1994 |
| Maize, vegetative | 121 – 131 | 111 | Baldocchi, 1994 |
| Wheat | 17 – 20 | 18 | Choudhury, 1998 |
| Potatoe | 100 – 130 | 130 | Vos, 1987 |
| Alpha-alpha | 100 – 120 | 110 – 130 (dep. VPD) | Saugier, 1991 |
| Soya | 66 | 70 | Oliosa, 1996 |
| Grass C3 | 74 | 74 – 120 (dep. VPD) | Knap, 1993 |
| Grass C4 | 151 | 156 – 178 (dep. VPD) | Knap, 1993 |

The model results are close with experimental values, better than 50%.

### 2.3 OBT production in crops

Photosynthesis rate and HTO concentration in plant water are driving the OBT production in crops [3]. With the improved model, as above, the experimental data on wheat [8] are satisfactory reproduced, without parameters' optimization.

**Table 2. Comparison between experimental data and model predictions for wheat.**

| Time | Rel TWT at end exposure % (Exp) | Rel TWT at end exposure % (Model) | TWT half time (1h after end) min (Exp) | TWT half time (1h after end) min (Model) | REL OBT at harvest % (Exp) | REL OBT at harvest % (Model) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| DAWN | 26-74 | 21-40 | 40-60 | 60-100 | 0.29 | - |
| DAY | 53-100 | 35-50 | 20-49 | 30-50 | 0.23 | 0.36 |
| DUSK | 20-26 | 10-20 | 230-600 | 200-300 | 0.35 | - |
| NIGHT | 18-19 | 5-15 | ? | 400-600 | 0.27 | 0.36 |

The model predicts lower uptake than experimental data. Partly this can be explained by the reference concentration: in the experiment the HTO concentration in air moisture was measured at canopy top, while in the model we considered it at a higher reference level. The model predictions must be corrected with the effect of atmospheric resistance and are increased by 40% in the day and near 10% in the night. The temperature difference between the experimental chamber and model explain most of the discrepancy in the uptake fraction.

## 3. EXTENSION OF SPARSE CANOPY APPROACH FOR TRITIATED WATER TRANSFER: THE CASE OF TWO LAYERS (SOIL-VEGETATION)

In recent years the coupling between soil and canopy was more and more used in the frame of "sparse canopy" theory [9]. We have adapted the formalism for tritium uptake by plants, in order to investigate the usefulness for an operational radiological assessment model.

Using the partition between soil and vegetation in the sparse canopy approach (see Figure 2) we can write the equations for the concentration difference air-vegetation and air-soil as:

\[
F_c(R_{aa} + R_{ab} + R_{ac}) + F_s R_a = C_a - C_c; \quad F_c R_a + F_s(R_{aa} + R_{as} + R_{ss}) = C_a - C_s \quad (7)
\]

where:

- \(C_a\) - HTO concentration in air
- \(C_c\) - HTO concentration in vegetation
- \(C_s\) - HTO concentration in soil
- \(R_{aa}\) - atmospheric resistance between reference level and canopy source height
- \(R_{ac}\) - boundary layer resistance
- \(R_{sc}\) - canopy resistance
- \(R_{as}\) - atmospheric resistance between canopy source height and soil surface
- \(R_{ss}\) - soil resistance
- \(F_c\) - flux atmosphere - vegetation
- \(F_s\) - flux atmosphere - soil

With the following notation, the solution is easy expressed:

\[
\frac{dC}{dt} = \frac{1}{M_w}\{F_{tr}C_s + V_{ex}\} ((C_a - 0.91\rho_s C_s) - \frac{R_{aa}}{R_s} (C_a - 0.91\rho_s C_{ss})) \quad (8)
\]

where \(F_{tr}\) is the transpiration flux, \(C_{ss}\) is the HTO concentration at the soil surface and

\[
V_{ex} = \frac{0.95R_1}{R_c}; \quad R_1 = \frac{R_c R_s}{R_c R_s - R_{aa}^2}; \quad R_c = R_{aa} + R_{ab} + R_{ac}; \quad R_s = R_{aa} + R_{as} + R_{ss} \quad (9)
\]

Equation (8) is solved coupled with the equations describing the dynamics of HTO in soil [10], starting with the soil surface where the flux \(F_s\) is used as boundary condition. The importance of coupling between the vegetation layer and the soil surface, intermediated by the in canopy air (see Figure 2), is illustrated in Figure 3, for a wet and a dry soil surface and for plant canopy with a low (1) and high (5) Leaf Area Index.

*[Figure 2. Schematic diagram of energy partition for sparse vegetation.]*
*[Figure 3. Vegetation HTO concentration in the sparse canopy approach.]*

In Figure 3 we observe that the coupling between soil surface and vegetation layer has a significant influence on canopy HTO concentration at both low and high Leaf Area Index, so more studies are justified.

## 4. DISCUSSION

The Aiken List was divided in 1990 to help decide which transport processes should be investigated experimentally as to derive the greatest improvement in performance of environmental tritium assessment models and was revised few years ago [1]. The importance of each process depends on case application. We tried to improve in this paper the modeling of soil canopy resistance and to have a preliminary study of the application of sparse canopy approach for the transfer of HTO in atmosphere-plant-soil continuum. Adapting Jacobs-Calvet model for stomatal conductance and combining with the WOFOST photosynthesis model and database, we are able to make reliable predictions for the dynamics of HTO and OBT in crops under the atmospheric forces. The new parametrisation for soil resistance offers more flexibility in various soil types. The extension of sparse canopy approach to HTO transfer reveals the role of vegetation-soil coupling and it needs further studies, in order to be included in operational codes. In the same time, it can give solutions for condensation dew and wet deposition for tritium transport. The present paper is not exhausting all possibilities of important processes for tritium transport.

## References

[1] Raskob W., Barry P., Importance and Variability in Processes Relevant to Environmental Tritium Dose Assessment Models, JER, Vol. 136, pp.237-251, 1997.
[2] A. Melintescu, D. Galeriu, E. Marica, "Using WOFOST Crop Model for Data Base Derivation of Tritium and Terrestrial Food Chain Modules in RODOS", P. C1-1241-C1-1246, Radioprotection, Numero special 37, C1, "The Radioecology - Ecotoxicology of Continental and Estuarine Environments ECORAD 2001", 2002.
[3] D. Galeriu, A. Melintescu, C. Turcanu, W. Raskob, "FDMH - The Tritium Module in RODOS", Workshop on Environmental Behavior and Biological Effects of Tritium, 8-9 May 2000, P.86, Kurri, Kumatori, Osaka, Japan, Ed. M. Saito, S. Kimura, and T. Takahashi ISSN 0287-0852 [KURRI-KR-61].
[4] Kondo J, Saigusa N and Sato T "A parameterization of evaporation from bare soil surfaces" J Apl Meteorol 29, 385.
[5] Jacobs C. M. J., Direct impact of atmospheric CO₂ enrichment on regional transpiration, PhD. Thesis, Agricultural University, Wageningen (1994).
[6] Calvet J. C., Agricultural and Forest Meteorology 103, 229 (2000). Vol. 103, pp.229-247.
[7] Boogaard H. L, User's guide for the WOFOST 7.1 crop growth simulation model and WOFOST Control Center 1.5 Technical Document 52 DLO Winand Staring Centre, Wageningen, 1998.
[8] Diabate, S. and Strack, S. "Organically bound tritium in wheat after short-term exposure to atmospheric tritium under laboratory condition", Journal of Environmental Radioactivity, 1997, 67, 211.
[9] Wallace J.S., Verhoef A., Modelling interactions in mixed plant communities: light, water and carbon dioxide in Leaf Development and Canopy Growth, Edited by Bruce Marshall and Jeremy A. Roberts, 2001.
[10] Melayah A., Bruckler L., Modeling the transport of water stable isotopes in unsaturated soils under natural conditions, Water Resources Research, Vol. 32, No. 7, pp.2047-2054, 1996.