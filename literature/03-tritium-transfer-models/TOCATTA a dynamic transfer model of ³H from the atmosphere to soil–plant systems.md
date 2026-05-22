# TOCATTA: a dynamic transfer model of ³H from the atmosphere to soil–plant systems

**Authors**: S. Le Dizes, C. Aulagnier, P. Henner, M. Simon-Cornu

**Affiliations**:
- Institut de Radioprotection et de Sûreté Nucléaire (IRSN), PRP-ENV, SERIS, LM2E, 13115 Cadarache, France
- Institut de Radioprotection et de Sûreté Nucléaire (IRSN), PRP-ENV, SERIS, L2BT, Cadarache, France

**Published in**: Journal of Environmental Radioactivity, Volume 124, pp. 191-204 (2013)

**DOI**: (not provided, but journal is Elsevier)

**Received**: 31 July 2012  
**Received in revised form**: 22 March 2013  
**Accepted**: 22 April 2013  
**Available online**: 26 June 2013

**Keywords**: Plant compartment model, TFWT, OBT, Accidental scenarios

---

## ABSTRACT

This paper describes a dynamic compartment model (TOCATTA) that simulates tritium transfer in agricultural plants of several categories including vegetables, pasture and annual crops, exposed to time-varying HTO concentrations of water vapour in the air and possibly in irrigation and rainwater. Consideration is also given to the transfer pathways of HTO in soil. Though the transfer of tritium is quite complex, from its release into the environment to its absorption and its incorporation within the organic material of living organisms, the TOCATTA model is relatively simple, with a limited number of compartments and input parameters appropriate to its use in an operational mode. In this paper, we took the opportunity to apply the model to a real case where tritium was released accidentally over several weeks (or months). More specifically, the model's ability to provide hindsight on the chronology of the release scenario is discussed by comparing model predictions of TFWT and OBT activity concentrations in the plant leaves with measurements performed on three different leaves characterized by different developmental stages. The data-model comparison shows some limitations, mainly because of a lack of knowledge about the initial conditions of the accident and when it actually started and about the processes involved in the transfer of tritium. Efforts are needed in both experimental and modelling areas for future evaluation of tritium behaviour in agricultural soil and plants exposed to gaseous HTO releases and/or to irrigation with contaminated water.

© 2013 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

Tritium (³H, T) is a radioactive form of hydrogen that is naturally present in the environment but also routinely released by almost all nuclear facilities. In future fusion power plants, tritium inventory will increase to an amount comparable to the global tritium inventory coming from actual nuclear fission power plants. This has raised concerns on how tritium could migrate in the environment under normal operating conditions or after potential accidental releases from facilities for which the accidental health impact on humans is mainly driven by tritium, such as heavy water nuclear power plants, fuel reprocessing plants, tritium defence facilities and the ITER fusion facility (Gariel et al., 2009; Guétat et al., 2008b; Gulden and Raskob, 2005; IAEA, 2012; Okada and Momoshima, 1993).

Once released into the environment, tritium has a complex behaviour. It is extremely volatile and has the ability to substitute for stable hydrogen atoms in the composition of water (liquid water or water vapour). Therefore, tritiated water released as HTO from nuclear facilities is easily incorporated into water within living organisms as tissue-free water tritium (TFWT) and may then label the organic matter as organically-bound tritium (OBT) through metabolic processes, especially photosynthesis in the case of plants. Equilibrium is thought to be quickly reached between TFWT and tritiated water in the environment; therefore this fraction of free tritium is said to be representative of instantaneous tritium levels (Boyer et al., 2009a; Vichot et al., 2008). Conversely, OBT results from non-equilibrium processes and remains in the organisms for a long time, giving insight into the chronology of retrospective events and the consequent dose estimation for humans near nuclear plants (Boyer et al., 2009a; Choi et al., 2002; IAEA, 2012; Vichot et al., 2008). Its "non-exchangeable" fraction is of primary interest since it represents the incorporation of TFWT within the organic fraction during growth of organisms and more generally throughout their lives. Therefore, non-exchangeable OBT is a good indicator of tritium contamination (Guenot, 1984). Several studies estimated that the contribution of plant OBT to the ingestion dose would be about 20-30% in case of chronic exposure and about 60%-80% in case of accidental exposure (Guétat et al., 2008a,b; Raskob and Barry, 1997).

In this context, a mathematical model to predict the radioecological impact of tritium on agricultural plants is a prerequisite to assessing ingestion doses for humans. However, the dynamic movement of tritium through the different pools (i.e. air, soil, plant tissue free water and organic matter) is not easy to model because hydrogen - and hence tritium - take part in the water cycle, which affects all pools of the biosphere. More specifically, tritium transfer to crops is subject to changing environmental conditions (e.g. local meteorology, relative humidity, soil characteristics) affecting the plant physiological processes and strongly depends on the magnitude and time history of the release. Moreover, very few experimental data exist on short and long term tritium exposures to support models available in the literature (ASN, 2010; Boyer, 2009; IAEA, 2012; Thompson et al., 2011). Consequently, an increased knowledge of mechanisms of tritium transfer to plants with regard to tritium exposure and metabolic processes involved is essential for the management of potential accident situations, to obtain a (moderately) conservative assessment of doses to members of the public and to prepare the conditions for the management of the emergency situations (IAEA, 2012).

A great number of dynamic modelling approaches to predict the transfer of tritium to plants, soil and animals have been developed over the last two decades, ranging from the very simple specific activity models to more complex process-oriented models. The latter type of models such as UFOTRI (Galeriu et al., 1995; Raskob, 1990, 1993; Täschner et al., 1997), ETMOD (Russell and Ogram, 1992), NORMTRI (Raskob, 1994), SOLVEG-II (Ota and Nagai, 2011) or the FDMH (Food Dose Module Tritium) model in RODOS (Galeriu et al., 2000) simulate the detailed movement of tritium through the different pools using hourly meteorological data. However, these detailed models are not practical for calculating the doses some weeks or months after the release since they require a long computation time and a large amount of input data (Keum et al., 2006) that often are not easily available. In order to deal with the uncertainties involved in modelling the behaviour of tritium in the environment after an accident, the EMRAS II (Environmental Modelling for Radiation Safety) international programme in 2008-2012 has formulated the requirements to obtain a harmonised approach concerning the development of a robust, transparent and relatively simple model with a limited number of input parameters to be used for a quick and straightforward assessment after an accidental tritium release.

The main part of this paper is dedicated to the description and critical analysis of a dynamic compartment model (TOCATTA) for evaluating the tritium behaviour in agricultural soil and plants exposed to spray irrigation with contaminated water and/or to gaseous HTO releases from nuclear facilities. This description is made in continuity to the previous paper regarding the modelling of ¹⁴C transfer with TOCATTA (Le Dizes et al., 2012) and is considered as a first step towards future model developments. Processes considered in this paper are assigned to two major submodels: (1) a plant sub-model that estimates the aboveground biomass and the dynamics of tritium activity concentration in various categories of agricultural plants, (2) a soil sub-model that simulates tritium dynamics in soil water exchange processes at the soil/canopy atmosphere interface. Tritium transfer to animals is not described. The related objectives are (1) to document the scientific basis, major assumptions, conceptual modelling and mathematical formulations of the tritium transfer in soil-plant systems, (2) to discuss the weaknesses and future developments of the model to improve its predictive capability. The model was applied to the case of a real accident involving tritium releases that occurred over several weeks (or months) in 2010, the specificity of which, compared to usually treated accidental scenarios, being that the chronicle of releases prior to the identification of the contamination was not known. Thus the objective is to discuss the comparison of the model outputs with measurements so as to find clues about the most likely scenario regarding the exposure of operators within the industrial facility that may have occurred in the six months period prior to the discovery of the accidental tritium contamination.

---

## 2. Model description

### 2.1. Main assumptions and characteristics

The model is based on a daily time step and is mainly driven by daily atmospheric tritiated water vapour concentration and agrometeorological data. The main chemical forms of tritium released from nuclear power plants (fission and fusion types) and fuel reprocessing plants are tritiated hydrogen (HT), tritiated methane (CH₃T) and tritiated water vapour (HTO) (Akata et al., 2011; Bartels et al., 1998; Belot et al., 1996; Koarashi et al., 2004; Ota et al., 2012), the latter being the only form of atmospheric emission taken into account in the model. The other forms play no role in photosynthesis and therefore may not be directly transferred to plants. Previous studies have confirmed that plant OBT is essentially formed through photosynthesis from airborne HTO and, to a negligible extent, from airborne tritiated hydrogen (HT) (Belot et al., 1996). For that species, the only pathway leading to plant contamination would be through the chemical transformation by microorganisms of a deposit of atmospheric HT on the soil into tritiated water, and the following uptake of the water by plant roots (Ota et al., 2007). The HTO in surface soil may also eventually be converted to organically bound tritium, a main contributor to doses resulting from tritium exposures (Atarashi-Andoh et al., 2002; Belot et al., 1996; Boyer et al., 2009b; Raskob and Barry, 1997; Thompson et al., 2011). Yet, all these processes and associated kinetics were not considered in our application. Consequently, as a first approximation, the model does not consider any releases of molecular tritium-HT or tritiated methane-CH₃T nor their behaviour in the environment. Only the tritium released into the air in the form of tritiated water vapour (HTO) and associated transfers into plant non-exchangeable OBT and soil HTO are taken into account, with an explicit consideration of an isotopic fractionation during OBT formation in plants. Moreover, given the 12-year radioactive half-life for tritium, the model also considers its radioactive decay since the simulations performed by the model might exceed the time scales of years. The model has been implemented in the SYMBIOSE modelling and simulation platform that aims to assess the fate and transport of a wide range of radionuclides in various environmental systems, and their impact on humans (Gonze et al., 2011). It is parameterized for various types of agricultural plants - annual crops, vegetable crops and pasture grass - according to categories defined in the platform (Calmon, 2009). The TOCATTA model computes daily activity concentrations of tritium in various types of agricultural soil, as well as plant and animal products. The subsequent calculation of tritium transfer to man and assessment of doses are performed within the SYMBIOSE platform, based on a typical terrestrial food-chain scenario. The model has been successfully used with SYMBIOSE to perform an area-wide dose assessment around a French nuclear power plant (Mourlon et al., 2011). It has the following main characteristics, most of which are similar to those used for modelling the transfer of ¹⁴C (Le Dizes et al., 2012):

- A dynamic approach based on time-dependent growth curves for plants is adopted, on a daily basis. Moreover, the model estimates the net primary productivity (i.e. the net balance between photosynthesis and foliar respiration) from the simulated growth rate and quantity of dry matter, either derived from experimental data or from predefined plant growth curves.
- The assumption is made that an isotopic equilibrium between the organic plant compartment and canopy atmosphere is reached at each time step of the simulation (e.g. 1 day). Consequently, the quantity of newly created plant biomass has the same isotopic ³H/¹H ratio as the surrounding air, corrected by a discrimination factor for tritium relative to the stable hydrogen during OBT formation in vegetation.
- The model uses the same conceptual and mathematical modelling approaches as defined in SYMBIOSE (Le Dizes et al., 2012): the conceptual framework is based on the interaction matrix formalism, while the mathematical model is implemented as a series of first-order differential equations, defined for time-varying release conditions and expressing conservation of radionuclide activity for each compartment of the conceptual model.
- Another important feature of TOCATTA, specific to the modelling of tritium, is the explicit separation between the TFWT (including exchangeable-OBT) and the OBT compartments in plants. Consequently, the mass balance equation applies separately to both TFWT and OBT plant compartments for the calculation of the dynamics of [TFWT]P and [OBT]P concentrations, expressed in mol kg⁻¹ water or mol kg⁻¹ DW, respectively.

**Table 1. Key features of the ³H soil-plant transfer in the TOCATTA model.**

| Type of contamination | Gaseous atmospheric releases of ³H and/or spray irrigation with contaminated water |
| --- | --- |
| Driving variables (inputs) | Daily atmospheric tritiated water vapor (HTO) concentration, monthly data on climate (e.g. temperature, rainfall) and, if irrigation, tritium concentration in irrigation water (HTO) and monthly irrigation water height |
| Plant growth | Predefined plant growth curve patterns for all vegetation categories. Possibility of using empirical dry biomass data for grass if available. |
| Mass balances | Mass conservation equations applying to concentrations and/or stocks of TFWT and OBT in vegetation separately, to HTO in soil and to dry plant biomass |
| Operation (time-step) | Daily fluxes relative to stable and radioactive H, daily plant growth patterns |
| Outputs | Concentrations, activities, stocks and fluxes of plant TFWT and OBT and of soil HTO, plant growth rate and quantity of dry matter |
| Modelling strategy | Use objective-oriented programming (C++) approach. Model compartments are represented as object classes, allowing easy maintenance and development. |

### 2.2. Conceptual modelling

**Table 2. Compartments (diagonal elements) and mass transfer processes (off-diagonal elements) defined in the TOCATTA model for agricultural soils and plants contaminated through gaseous releases in air and/or spray irrigation.**

| SOURCEᵃ | CANOPY ATMOSPHERE | SOIL WATERᶜ | ABOVE-GROUND PLANT MATERIAL WATERᵈ | ABOVE-GROUND PLANT MATERIAL DRY MATTER | REST OF PLANTᶠ | SINKᵍ |
| --- | --- | --- | --- | --- | --- | --- |
| Gas dispersion (HTO) | → | Surface exchange (HTO) | | | | |
| Wet input (HTO, via precipitation and spray irrigation) | → Interception by soil | | | | | |
| Wet input (HTO, via precipitation and spray irrigation) | → Interception by plant | | | | | |
| CANOPY ATMOSPHERE | | Surface exchange (HTO) | Foliar absorption (TFWT) | Net primary production (OBT) | | |
| SOIL WATERᶜ | | | Root uptake (HTO) | | | |
| ABOVE-GROUND PLANT MATERIAL WATERᵈ | | | Translocation (TFWT) | | Biological loss (HTO) | |
| ABOVE-GROUND PLANT MATERIAL DRY MATTER | | | | | Biological growth | |
| | | | | | Litterfall, Cutting/Grazing (grass) | |

ᵃ Tritiated water present in the atmosphere (air & water droplets) or in irrigation water.  
ᵇ Tritiated water vapour in the vegetation canopy atmosphere.  
ᶜ Dissolved HTO in the soil pores.  
ᵈ Tissue Free Water Tritium (TFWT) in leaves or edible organs (fruits, grains, roots, tubers, etc.).  
ᵉ Non-exchangeable Organically-Bound Tritium (OBT) in dry matter of leaves or edible organs.  
ᶠ The REST OF PLANT compartment includes all tissues constituting the plant, with the exception of the water and dry matter compartment of aboveground parts.  
ᵍ The SINK compartment represents anything outside the system of interest.

---

## 3. Sub-models description

**Table 3. Major soil-plant transfer processes considered in TOCATTA following a gaseous release of ³H in atmosphere and/or spray irrigation, modelling approaches, and original sources.**

| Process | Approach | Sources |
| --- | --- | --- |
| Growth of a plant | Based on predefined plant growth curves for dry biomass evolution: shaped logistical equations (annual crops), linear (vegetables), exponential or user-defined data (grass) | Le Dizes et al. (2012) |
| Net primary production | Based on an isotopic equilibrium hypothesis between newly created plant biomass and surrounding air, corrected by a discrimination factor of tritium relative to stable H during OBT formation in vegetation (Eq. (2)) | Le Dizes et al. (2012) |
| Foliar absorption | Based on an isotopic equilibrium hypothesis between free water tritium in plant and tritiated water vapour in surrounding air (Eq. (3)) | — |
| Translocation | Based on the calculation of an equilibrium translocation factor as a function of biological loss kinetics and hydrogen concentration at equilibrium (Eq. (4)) | — |
| Wet inputs to plant and soil | Based on radioecological calculations of interception factors by vegetation and wet inputs associated with rain and/or spray irrigation (Eq. (5) and Eq. (12)) | — |
| Interception by vegetation & soil | Estimated as a function of plant dry biomass | Chamberlain (1970) |
| Root uptake | Based on a single exponential function characteristic by a first-order rate constant (Eq. (7)). A passive transfer of tritium is assumed at a rate equal to the average flux of plant transpiration. | — |
| Biological loss | Based on a single exponential function characteristic by a first-order rate kinetic formulation (Eq. (9)). Biological loss rate is determined from the transpiration flux (Eq. (10)). | — |
| Litterfall | Assumed constant for grass and related to crop yield and the amount of crop not removed for other plant categories | Sheppard et al. (2006a, 2006b) |
| Surface exchange | Based on the Fick's diffusion law between the surface atmosphere and the underlying soil with a constant exchange rate (Eq. (14)) | — |
| Migration in soil | Based on a single exponential function characteristic by a first-order rate constant (Eq. (15)) | — |
| Radioactive decay | Based on exponential functions characterised by a first-order rate constant determined by half-life for tritium | — |

### 3.1. Plant ³H sub-model

#### 3.1.1. Input data

The starting point of the assessments in TOCATTA is the tritiated water vapour (HTO) concentration in the vegetation canopy atmosphere after a gaseous release of tritium to the atmosphere; in particular, the gaseous forms of tritium (i.e. HT and CH₃T) as well as atmospheric transport and dispersion processes are not explicitly taken into account in the current version of the model. Consequently, input data for the TOCATTA model when used for operational applications within the SYMBIOSE platform are the activity concentration of HTO in the vegetation canopy atmosphere and/or the activity concentration of HTO in irrigated water, both as a function of time and space.

#### 3.1.2. Plant growth and development

A modelling approach of plant growth and phenological development similar to the one used for simulating C (and hence ¹⁴C) transfer fluxes is used and described in detail by Le Dizes et al. (2012). For each vegetation type, the plant growth patterns may be either derived from a predefined growth curve of dry biomass or user-defined from empirical biomass data when available. The relative growth rate (d⁻¹) for the plant category P is calculated by:

$$\lambda_P^{\text{Gro}}(t) = \frac{1}{\chi_P} \left[ \frac{d\chi_P}{dt} \right]^{\text{Gro}} \quad (1)$$

where $\chi_P$ is plant areal density (or dry biomass, kg DW m⁻²).

#### 3.1.3. Net primary production

The net foliar assimilation flux of OBT by plants may be expressed, on a dry weight basis, as follows (mol kg⁻¹ DW d⁻¹):

$$\text{TOTB}_{\text{Air},P}^{\text{Npp}} = \frac{(1-f_P^S)}{f_P^S} \times \lambda_P^{\text{Gro}} \times [H]_P \times D_{lP} \times \left\{ \frac{p_{\text{HTO}} \cdot [^3H]_{\text{Air}}}{[H]_{\text{Air}}} + \frac{p_{\text{HTO}}' \cdot [^3H]_{\text{Irrtwat}}}{[H]_{\text{Irrtwat}}} \right\} \quad (2)$$

where: $f_P^S$ (kg DW kg⁻¹ FW) is the dry/fresh weight ratio for plant products, $\lambda_P^{\text{Gro}}$ (d⁻¹) is the relative plant growth rate, $D_{lP}$ (dimensionless) is the isotopic discrimination factor, $[H]_P$ (mol kg⁻¹) is the stable hydrogen concentration in plant water, $[^3H]_{\text{Air}}$ and $[^3H]_{\text{Irrtwat}}$ (mol m⁻³) are the concentrations of tritium in the plant canopy atmosphere and in irrigation water, $[H]_{\text{Air}}$ and $[H]_{\text{Irrtwat}}$ (mol m⁻³) are the concentrations of stable H (in the form of H₂O) in air and in irrigation water, and $p_{\text{HTO}}$ and $p_{\text{HTO}}'$ (dimensionless) are the proportions of tritium released as tritiated water (HTO) in air and irrigation water, respectively.

#### 3.1.4. Foliar absorption

Absorption of atmospheric tritiated water vapour by plant leaves is expressed as:

$$\text{TFWT}_{\text{Air},P}^{\text{Abs}} = \lambda_P^{\text{Gro}} \times [H]_P \times \frac{p_{\text{HTO}} \times [^3H]_{\text{Air}}}{[H]_{\text{Air}}} \quad (3)$$

#### 3.1.5. Translocation

The translocation factor is expressed as:

$$\text{FTeq}_{P}^{\text{Tra}} = \delta_{\text{Cropping}=1} \left\{ \frac{\lambda_P^{\text{Bio}} + q_P^{\text{Tr}}}{v_S^{\text{Infl}}} \times \frac{[H]_P}{\text{THW}_{\text{Air},P}^{\text{Win}} + \text{THW}_{\text{Air},S}^{\text{Win}}} \right\} \quad (4)$$

#### 3.1.6. Wet inputs to plant foliage and translocation

The flux of atmospheric tritiated water vapour "captured" by the aerial parts of the plant is:

$$\text{THTO}_{\text{Air},P}^{\text{Win}} = \left( F_{P}^{\text{Rcap}} \cdot \text{TH3}_{\text{Air},P}^{\text{Rain}} \right) + \delta_{P=\text{Vegetable or AnnualCrop}} \left( F_{P}^{\text{Icap}} \cdot p_{\text{HTO}}' \cdot \text{TH3}_{\text{Air},P}^{\text{Irt}} \right) \quad (5)$$

The flux of tritiated water deposited onto plant foliage and translocated to plant edible organs is:

$$\text{TFWT}_{\text{Air},P}^{\text{WinTra}} = \text{THTO}_{\text{Air},P}^{\text{Win}} \times \text{FTeq}_{P}^{\text{Tra}} \quad (6)$$

#### 3.1.7. Root uptake and translocation

A passive transfer of tritium from soil to vegetation is assumed at a rate equal to the average flux of plant transpiration:

$$\text{THTO}_{S,P}^{\text{Up}} = \delta_{\text{Cropping}_P=1} \left( q_P^{\text{Tr}} \times [\text{HTO}]_S \right) \quad (7)$$

The flux of tritiated water taken up by plant roots and translocated to edible organs is:

$$\text{TFWT}_{S,P}^{\text{UpTra}} = \text{THTO}_{S,P}^{\text{Up}} \times \text{FTeq}_{P}^{\text{Tra}} \quad (8)$$

#### 3.1.8. Biological loss

Loss of tritiated water from plant material by biological decay is described by first-order kinetics:

$$\text{TFWT}_{P,\infty}^{\text{Bio}} = \lambda_P^{\text{Bio}} \times [\text{TFWT}]_P \quad (9)$$

where the biological loss rate is:

$$\lambda_P^{\text{Bio}} = \delta_{\text{Cropping}=1} \left( \min \left( \rho_W \times \frac{q_P^{\text{Tr}}}{\chi_{P,\text{Wat}} + \epsilon'}, 14\ \text{d}^{-1} \right) \right) \quad (10)$$

#### 3.1.9. Radioactive decay

Losses due to radioactive decay are modelled by a first-order decay rate constant.

#### 3.1.10. Litterfall

The loss of plant aboveground dry biomass through the processes of litterfall is:

$$\left[ \frac{d\chi_P}{dt} \right]^{\text{Litt}} = T^{\text{Litt}} \times f_P^S \quad (11)$$

### 3.2. Soil ³H sub-model

#### 3.2.1. Input data

Input data are the tritium activity in rain and/or irrigation water versus time.

#### 3.2.2. Wet input to soil

The flux of atmospheric HTO entering the soil is:

$$\text{THTO}_{\text{Air},S}^{\text{Win}} = (1 - F_{P}^{\text{Rcap}}) \cdot \text{TH3}_{\text{Air},P}^{\text{Rain}} + \delta_{P=\text{Vegetable or AnnualCrop}} \left( (1 - F_{P}^{\text{Icap}}) \cdot p_{\text{HTO}}' \cdot \text{TH3}_{\text{Air},P}^{\text{Irt}} \right) \quad (12)$$

#### 3.2.3. Surface exchange

The net flux of tritiated water vapour between air and soil is:

$$\text{THTO}_{\text{Air},S}^{\text{Exch}} = \nu^{\text{Exch}} \cdot \left\{ p_{\text{HTO}} \cdot [^3H]_{\text{Air}} - \epsilon^{-1} \cdot \rho_S \cdot [\text{HTO}]_S \right\} \quad (14)$$

#### 3.2.4. Root uptake

Uptake of soil HTO by plant roots is described as a passive transfer at a rate equal to the average plant transpiration flux (Eq. (7)).

#### 3.2.5. Migration

Losses of HTO by vertical migration into deeper soil horizons:

$$\text{THTO}_{S,\infty}^{\text{Mig}} = \nu_S^{\text{Mig}} \times [\text{HTO}]_S \quad (15)$$

#### 3.2.6. Radioactive decay

Loss of tritiated water from soil by radioactive decay is modelled by a first order decay.

---

## 4. Case study

### 4.1. Context and objective

In this part, the application of the TOCATTA model is illustrated through a case study. Tritium was emitted accidentally over several weeks (or months) in 2010 in a building of a company then into the environment. Starting at an unknown date, after April 29, the release occurred until November 4, the closing day of the company following the discovery of accidental contamination of tritium (IRSN, 2010a; IRSN, 2010b).

**Table 4. List of the main parameters and values used for the current application of the model to the ARECA palm tree**

| Symbol | Units | Definition | Value | References |
| --- | --- | --- | --- | --- |
| **Atmospheric and irrigation parameters** | | | | |
| [H]Air | mol m⁻³ | Concentration of stable hydrogen (in the form of H₂O) in air | 0.88 | see §4.3.1 |
| [H]IrrWat | mol m⁻³ | Concentration of stable hydrogen in irrigation water | 0.11 | - |
| [³H]Air | mol m⁻³ | Daily tritium concentration in plant canopy atmosphere | As a function of time | see §4.3.1 |
| [³H]IrrWat | mol m⁻³ | Tritium concentration in irrigation water | As a function of time | see §4.3 |
| p_HTO | - | Proportion of tritium released as HTO in air | 1 | - |
| p'_HTO | - | Proportion of tritium released as HTO in irrigation water | 1 | - |
| Q_irr | L m⁻² week⁻¹ | Quantity of irrigation water brought to the indoor plant | 0.5 | - |
| ρ_Air | kg m⁻³ | Absolute humidity of air | 8.10⁻³ | - |
| **Plant parameters** | | | | |
| D_l | unitless | Isotopic discrimination ratio | 0.9 | Peterson and Davis (2002) |
| f_P^S | kg kg⁻¹ FW | Dry/fresh weight ratio of plants | 0.25 for young developing and mature leaves, 0.18 for old leaves | Measurements |
| h_P | m | Height of the soil horizon associated with the potted palm tree | 0.4 | - |
| [H]_P | mol kg⁻¹ water | Stable hydrogen concentration in plant water | 110 | - |
| λ_P | d⁻¹ | Relative growth rate | As a function of time | Modelling scenarios |
| **Soil parameters** | | | | |
| q_P^Tr | m³ water m⁻² d⁻¹ | Average rate of leaf transpiration | 4.32 × 10⁻⁴ | Kramer (1959) |
| ε | - | Isotope separation factor between tritiated water vapour and liquid water | 1.099 | Belot et al. (1996) |
| ν_Exch | m³ m⁻² s⁻¹ | Exchange rate of tritiated water vapour between soil surface and canopy atmosphere | 0.015 | Yokoyama and Noguchi (2002) |
| ν_S^Mig | m³ m⁻² d⁻¹ | Infiltration rate of water in the soil | 0 | - |
| h_S | m | Soil layer height | 0.4 | - |
| ρ_S | m³ m⁻³ | Absolute humidity of soil air | 8.10⁻⁶ | - |
| θ_S | m³ m⁻³ | Soil water content | 0.4 | Kutilek and Nielsen (1994) |
| **Others** | | | | |
| λ_Rad | s⁻¹ | Rate of radioactive decay of tritium | 1.78278596 × 10⁻⁹ | - |
| MoTtoBq_³H | Bq mol⁻¹ | Coefficient of conversion of Becquerels to Mol for tritium | 1.08 × 10¹⁵ | - |
| ρ_W | kg m⁻³ | Water density | 1000 | - |

### 4.2. Sampling and measurements

**Table 6. Measurements of tissue free water tritium (TFWT) and organically bound tritium (OBT) and the ratio of activity concentrations between the organically bound tritium activity (Bq/L) and the activity of the tissue water (Bq/L) (OBT/TFWT) in different types of ARECA palm leaves.**

| Leaf age | TFWT (MBq/L) | TFWT (MBq/kg FW) | OBT (MBq/kg DW) | OBT (MBq/kg FW) | OBT/TFWT ratioᵃ |
| --- | --- | --- | --- | --- | --- |
| Old leaf fully developed | 221 | 181.5 (±6%) | 120 | 21.4 (±6%) | 0.9 |
| Young mature leaf | 170 | 130 (±6%) | 7.95 | 2.18 (±6%) | 0.08 |
| Young developing leaf | 69.8 | 50.9 (±6%) | 8.05 | 2.18 (±8%) | 0.19 |

ᵃ Estimated from measurements of tritium expressed on the basis of volume of water (MBq/L) and the assumption of a conversion factor of 0.6 L water of combustion per kilogram of dry matter.

### 4.3. Modelling assumptions and parameter values

**Table 5. List of the main parameters and values used for the current application of the model to the ARECA palm tree (symbols in alphabetic order, P = ARECA Palm tree, S = Soil)**

(see Table 4 above for details)

### 4.4. Modelling results and analysis

**Figure 1. Evolution of the TFWT activity measured in the Areca palm leaves as a function of the length of leaves (and their age).**

**Figure 2. Measured and simulated TFWT and OBT activities in the Areca palm leaves for four accident scenarios, i.e. the combination of different durations of exposure (i.e. Long or "Short" signifies a contamination starting in April or in October, respectively) with different watering scenarios: tap water (■) or process water (watering).**

The measured OBT activity, in Bq per kg of fresh material, is an order of magnitude greater in the oldest leaf than in the younger one. This would suggest that the source of contamination was already present when the oldest leaf was growing actively, thus indicating that the most likely scenario would be a contamination beginning in April.

The model does not reproduce a pattern of TFWT and OBT activities similar to the measurements: those simulated by TOCATTA are greater in the young developing leaf than in the oldest leaf. The fact that we do not know the watering characteristics (frequency, volume, and origin) makes it very difficult to simulate the TFWT activity based on an isotopic equilibrium with the air and soil (tritiated) water pools.

---

## 5. Conclusion and perspectives

The TOCATTA model described in this paper aims to simulate dynamics of tritium transfer in agricultural soil and plant ecosystems exposed to time-varying HTO concentrations in air water vapour and possibly in irrigation and rainwater. The model is part of a collaborative effort to achieve a better understanding of important biological and environmental processes of mass transfer between biotic and non-biotic compartments that constitute the biosphere. In this context, the main challenge was the development of a model designed to be comprehensive enough without being too complex, i.e. based on a limited number of compartments and input parameters required, to be used in an operational mode.

In the present study, the model was applied to a real accident case involving tritium releases. The model's ability to provide hindsight on the chronology of the accidental release scenario has been investigated by comparing model predictions of TFWT and OBT activity concentrations in the leaves of an indoor palm tree exposed to the release with measurements performed on three different leaves characterized by different development stage. The modelling results have only been rough estimates based on simplifying assumptions regarding the growth of palm leaves, the watering characteristics (frequency, volume, and origin) and a predefined chronology of atmospheric source term; therefore they need to be taken with a degree of caution. Simulated tissue free water tritium and organically bound tritium activities within three palm leaves of different age have been compared against measurements, considering four possible accident scenarios (involving two different watering characteristics and two different exposure durations). With only three measurements carried out on three leaves of different age, constructing the retrospective chronology of the accident is challenging. There are some indications of a longer exposure than the supposed 15 days (e.g. ten times higher OBT activity in the oldest leaf than in the younger ones) but they are inconclusive as uncertainties remain about the kinetics of tritium absorption through leaves and roots and the conversion of TFWT into OBT within the leaves. In these circumstances the TOCATTA model proves to be inadequate to help reproduce the chronology of the contamination, no matter the assumptions. However this exercise throws light upon the efforts needed to produce more conclusive future experimental and modelling studies.

The model application to the case study presented here has allowed the identification of some of the model weaknesses, such as 1) a low sensitivity to soil processes (and associated transfer pathways), 2) an overriding predominance of plant coarse growth dynamics over other parameters in the simulation of the dynamics of TFWT and OBT activities and 3) an inadequate assumption that TFWT and OBT follow separate, uncorrelated pathways whilst OBT is generally thought to be produced from TFWT. Above all, the water cycle within vegetation needs to be refined in the model.

---

## Acknowledgements

The authors wish to express their thanks to Philippe Guétat for his advice and remark concerning this work.

---

## References (selected)

Akata, N., et al., 2011. Deposition velocity of HTO and HT on various types of soil. Fusion Sci. Technol. 60, 1051-1054.

Atarashi-Andoh, M., et al., 2002. Formation and retention of organically bound deuterium in rice in deuterium water release experiment. Health Phys. 82, 863-868.

Bartels, J.R., et al., 1998. Tritium in the environment. Fusion Technol. 34, 859-864.

Belot, Y., et al., 1996. Le tritium de l'environnement à l'homme. Éditions de Physique.

Boyer, C., 2009. Etude des transferts du tritium atmosphérique chez la laitue: étude cinétique, état d'équilibre et intégration du tritium sous forme organique lors d'une exposition atmosphérique continue (in French). PhD Thesis.

Boyer, C., et al., 2009a. Tritium in plants: a review of current knowledge. Environ. Exp. Bot. 67, 34-51.

Boyer, C., et al., 2009b. Tritium in plants: a review of current knowledge. Environ. Exp. Bot. 67, 34-51.

Calmon, P., 2009. SYMBIOSE: a platform for environmental assessment. IRSN Report.

Choi, Y.H., et al., 2002. Tissue free water tritium and organically bound tritium in the rice plant acutely exposed to atmospheric HTO vapor under semi-outdoor conditions. J. Environ. Radioact. 58, 67-85.

Galeriu, D., et al., 1995. UFOTRI: A model for assessing the off-site consequences from accidental tritium releases. Fusion Technol. 28, 840-845.

Galeriu, D., et al., 2000. The FDMH model for tritium in RODOS. Radiat. Prot. Dosim. 92, 131-136.

Gariel, J.C., et al., 2009. Tritium in the environment: sources, transfers and impacts. IRSN Report.

Gonze, M.A., et al., 2011. SYMBIOSE: a modelling and simulation platform for environmental impact assessment. IRSN Report.

Guétat, P., et al., 2008a. Contribution of OBT to the ingestion dose after an accidental release of tritium. Radioprotection 43, 145-152.

Guétat, P., et al., 2008b. Tritium in the environment: from source to dose. IRSN Report.

Gulden, W., Raskob, W., 2005. Environmental release targets for fusion power plants. Fusion Eng. Des. 75-79, 1211-1216.

IAEA, 2012. Transfer of Tritium in the Environment after Accidental Releases from Nuclear Facilities. IAEA-TECDOC-1738.

Keum, D.K., et al., 2006. Prediction of tritium level in agricultural plants after short term exposure to HTO vapor and its comparison with experimental results. Health Phys. 90, 42-55.

Koarashi, J., et al., 2004. Deposition velocity of HTO and HT on soil. J. Nucl. Sci. Technol. 41, 1230-1235.

Le Dizes, S., et al., 2012. TOCATTA: a dynamic transfer model of ¹⁴C from the atmosphere to soil-plant systems. J. Environ. Radioact. 105, 40-51.

Mourlon, C., et al., 2011. Area-wide dose assessment around a French nuclear power plant using SYMBIOSE. Radioprotection 46, S213-S218.

Okada, S., Momoshima, N., 1993. Overview of tritium: characteristics, sources and problems. Health Phys. 65, 595-609.

Ota, M., Nagai, H., 2011. Development and validation of a dynamical atmosphere-vegetation-soil HTO transport and OBT formation model. J. Environ. Radioact. 102, 813-823.

Ota, M., et al., 2007. Importance of root HTO uptake in controlling land-surface tritium dynamics after an acute HT deposition: a numerical experiment. J. Environ. Radioact. 98, 234-248.

Ota, M., et al., 2012. Importance of root HTO uptake in controlling land-surface tritium dynamics after an acute HT deposition: a numerical experiment. J. Environ. Radioact. 109, 94-102.

Peterson, S.R., Davis, P.A., 2002. Modeled concentrations in rice and ingestion doses from chronic atmospheric releases of tritium. Health Phys. 78, 533-541.

Raskob, W., 1990. UFOTRI: program for assessing the off-site consequences from accidental tritium releases. KfK 4605.

Raskob, W., 1993. Description of the new version 4.0 of the tritium model UFOTRI including user guide. KfK 5194.

Raskob, W., 1994. NORMTRI: A model for assessing the consequences from normal releases of tritium. KfK 5274.

Raskob, W., Barry, P.J., 1997. Importance and variability in processes relevant to environmental tritium ingestion dose models. J. Environ. Radioact. 36, 237-251.

Russell, S.B., Ogram, G.L., 1992. ETMOD: a new environmental tritium model. Fusion Technol. 21, 645-650.

Täschner, M., et al., 1997. Measurements and modeling of tritium reemission rates after HTO depositions at sunrise and at sunset. J. Environ. Radioact. 36, 219-235.

Thompson, P.A., et al., 2011. Levels of tritium in soils and vegetation near Canadian nuclear facilities releasing tritium to the atmosphere: implications for environmental models. J. Environ. Radioact. 140, 105-113.

Vichot, L., et al., 2008. Organically bound tritium (OBT) for various plants in the vicinity of a continuous atmospheric tritium release. J. Environ. Radioact. 99, 1636-1643.

Yokoyama, S., Noguchi, H., 2002. Re-emission of heavy water vapour from soil to the atmosphere. J. Environ. Radioact. 71, 201-213.