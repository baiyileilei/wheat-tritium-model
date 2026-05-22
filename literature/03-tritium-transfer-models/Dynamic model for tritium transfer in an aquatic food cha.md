# Dynamic model for tritium transfer in an aquatic food chain

A. Melintescu · D. Galeriu

Received: 24 August 2010 / Accepted: 2 April 2011 / Published online: 17 April 2011
© Springer-Verlag 2011

**Abstract** Tritium (³H) is released from some nuclear facilities in relatively large quantities. It is a ubiquitous isotope because it enters straight into organisms, behaving essentially identically to its stable analogue (hydrogen). Tritium is a key radionuclide in the aquatic environment, in some cases, contributing significantly to the doses received by aquatic, non-human biota and by humans. The updated model presented here is based on more standardized, comprehensive assessments than previously used for the aquatic food chain, including the benthic flora and fauna, with an explicit application to the Danube ecosystem, as well as an extension to the special case of dissolved organic tritium (DOT). The model predicts the organically bound tritium (OBT) in the primary producers (the autotrophs, such as phytoplankton and algae) and in the consumers (the heterotrophs) using their bioenergetics, which involves the investigation of energy expenditure, losses, gains and efficiencies of transformations in the body. The model described in the present study intends to be more specific than a screening-level model, by including a metabolic approach and a description of the direct uptake of DOT in marine phytoplankton and invertebrates. For a better control of tritium transfer into the environment, not only tritiated water must be monitored, but also the other chemical forms and most importantly OBT, in the food chain.

## Introduction

Tritium (³H), a weak beta emitter (E_max = 18 keV), is released from some nuclear facilities in relatively large quantities. There is a specific interest in tritium, behaving essentially identically to its stable analogue (hydrogen). Tritium can represent a key radionuclide in the aquatic environment, in some cases, contributing significantly to the doses received by aquatic, non-human biota and by humans. Moreover, aquatic organisms are occasionally exposed to elevated tritium concentrations in water when tritium is released accidentally to aquatic ecosystems. However, the rates of uptake of tritiated water (HTO) and formation of organically bound tritium (OBT) are currently not very well understood.

Terrestrial plants and animals, as well as all aquatic organisms, incorporate a fraction of their HTO content into organic compounds in isotopic exchange or enzyme-catalysed reactions (Diabate and Strack 1993; Belot 1986). In exchange reactions, tritium bonds to oxygen, sulphur, phosphorus and nitrogen atoms in the form of hydroxides, thiols, phosphides and amines, respectively. Conventionally, this is termed exchangeable organically bound tritium (OBT). Exchangeable OBT is generally in equilibrium with the HTO in the plant or animal in question and behaves as HTO in all respects. In enzyme-catalysed reactions, tritium forms bonds with carbon chains of organic molecules. This is usually termed non-exchangeable OBT. This is the form of tritium that remains in dry biological matter that has been repeatedly washed with tritium-free water. Non-exchangeable OBT is more strongly attached than exchangeable OBT and has longer retention times; such bonds are only broken during catabolic reactions. It is necessary to have a clear definition of OBT, i.e. carbon-bound and buried tritium formed from HTO in living systems through natural environmental or biological processes. This is being accomplished within the framework of the International Atomic Energy Agency (IAEA)'s EMRAS (Environmental Modelling for Radiation Safety) programme. Buried tritium represents that tritium in exchangeable positions in large bio-molecules in the dry matter of environmental materials that is not removed by rinsing with tritium-free water.

To improve the understanding of tritium dynamics in aquatic ecosystems, the EMRAS programme included a Tritium and C-14 Working Group, which tests the performance of international environmental tritium models under both steady-state and dynamic exposure conditions, as defined in a series of model test scenarios. One such scenario involved the prediction of time-dependent tritium concentrations in freshwater mussels that were subjected to an abrupt change in ambient tritium levels (IAEA 2008; Yankovich et al. 2008; Yankovich et al. 2011). The EMRAS programme also included a "Model Validation for Radionuclide Transport in the Aquatic System 'Watershed-River' and in Estuaries" Working Group; one of the scenarios covered by this Working Group was focused on tritium migration through the Loire River (Luck et al. 2004).

Apparently, tritium is not an issue of major concern in the aquatic environment because of its rapid dilution in water; however, recently, two events occurred that increased the interest in the topic:

1. The necessity to have a robust risk assessment of both routine and accidental emissions of tritium for large nuclear installations;
2. The measurement of some very high OBT concentrations in marine biota at Cardiff Bay (UK), which runs counter the assumption that tritium does not bioaccumulate in aquatic biota (Lambert 2001; Williams et al. 2001).

The study of tritium transfer in aquatic environment started in the 1970s in USA with a series of experiments and a few modelling trials, the results of which have been summarized in a dedicated paper (Blaylock et al. 1986). The conclusion was that the dose to humans coming from the ingestion of aquatic foodstuff is lower than the dose coming from the intake of HTO in water.

The first model of tritium transfer in aquatic organisms was performed for crayfish (Bookhout and White 1976), but did not consider the OBT intake from foodstuff.

In order to update the BURN (Biological Uptake model of RadioNuclides) model (Heling et al. 2002) with a robust tritium sub-model, a new approach was developed within the framework of a contract with KEMA NRG (The Netherlands) (Heling and Galeriu 2002). Further developments of the model have been reported considering the seasonality and adding a metabolic model for the OBT biological loss rate in fish, as well as a first attempt to consider the Cardiff case (Galeriu et al. 2005). More recently, tritium modelling has been considered in the OURSON (French acronym for Tool for Environmental and Health Risk assessment) model applied to the Loire River (Ciffroy et al. 2006), but the fish sub-model is not clearly defined (Siclet F, personal communication, 2009).

In the present study, an updated model of dynamic tritium transfer in the aquatic food chain (AQUATRIT model) is presented, using more comprehensive assessments of the aquatic food chain than before, including the benthic flora and fauna, with an explicit application for the Danube ecosystem, as well as an extension to the special case of dissolved organic tritium (DOT).

## Materials and methods

### Model description

The initial model (Galeriu et al. 2005) describes the trophic pelagic food chain in a simplified manner, but an operational model must consider benthic, pelagic and demersal cases (Brittain et al. 2000; Broenmark and Hansson 1998), and must be adapted to fish species subject to human consumption. In the present study, this model is extended to benthic fish and uses the specific parameters for the Danube River. First, it describes the case where the source of contamination is only HTO in water, and subsequently, the case for DOT is considered.

Based on a review of past experiments (Heling and Galeriu 2002), the tritium in the body water of the animal is considered as being in equilibrium with the HTO in the aquatic environment and is expressed by the following simple relationship (Galeriu et al. 2005):

\[
C_{\text{HTO}} = C_W \times (1 - \text{Dryf}) \times 0.001 \quad (1)
\]

where C_HTO is the HTO concentration in an aquatic organism (Bq kg⁻¹ fresh mass (fm)), C_W is the HTO concentration in water (Bq m⁻³), 0.001 is the transformation m³ L⁻¹, and Dryf is the dry mass (dm) fraction of an aquatic organism.

For describing the OBT dynamics, the primary producers (i.e. the autotrophs, such as phytoplankton and algae) and the consumers (i.e. the heterotrophs) are treated separately.

#### OBT dynamics in phytoplankton

For phytoplankton, the authors derived and compared the following expression with experimental data (Heling and Galeriu 2002; Galeriu et al. 2005):

\[
\frac{\mathrm{d}C_{\text{o,phpl}}}{\mathrm{d}t} = 0.4 \cdot \mu \cdot \text{Dryf} \cdot 0.001 \cdot C_W - \mu \cdot C_{\text{o,phpl}} \quad (2)
\]

where C_o,phpl is the OBT concentration in phytoplankton (Bq kg⁻¹ fm) and μ is the phytoplankton growth rate (day⁻¹).

The phytoplankton growth rate depends on the nutrients in water, light and water temperature. Comparing to complex models (Jorgensen and Bendoricchio 2001; Ray et al. 2001), the updated present model considers an optimal growth rate of phytoplankton, μₒ = 0.5 day⁻¹ and the influence of temperature and light on the growth rate:

\[
\mu = \mu_o \times \text{modlight} \times \text{modtemp} \quad (3)
\]

where μₒ is the optimal phytoplankton growth rate (typically 0.5 day⁻¹), modlight is the seasonal light moderator, and modtemp is the seasonal temperature moderator.

The optimal value of μ chosen in the present study (μₒ = 0.5 day⁻¹) corresponds to a phytoplankton of average weight, living in moderately turbid water, with high light absorption, corresponding to the case of interest (Danube ecosystem).

The relative seasonal variability of light is chosen as follows:

\[
\text{modlight} = \min + (1 - \min) \times \sin \left( \pi \times \frac{\text{julanday}}{365} \right) \quad (4)
\]

where min is the ratio of minimum irradiance (winter time) to maximum irradiance (summer time), chosen as min = 0.3 based on local conditions.

The seasonal variability of water temperature is considered using local data or generic relationships for rivers (Hakanson and Peters 1995), which depend on latitude.

For phytoplankton, the temperature moderator is:

\[
\text{modtemp} = 1.065^{(T - 20)} \quad (5)
\]

where T is the water temperature (°C).

#### OBT dynamics in macrophages

Planktonic organisms and fish consume food, such as macrophages and benthic algae, living on the bottom of water bodies. For the assessment of the OBT concentration in macrophages following an accidental contamination, the model uses the same equation as for phytoplankton Eq. (2), but a specific growth rate. The growth processes of macrophages are described in the literature (Herb and Stefan 2006; Hakanson and Boulion 2002). The growth rate depends on the species, temperature, water turbulence, water depth where the plants grow and water surface irradiance, and these can vary widely, depending on local conditions. For the model application in a specific case, the above general theory (Herb and Stefan 2006; Hakanson and Boulion 2002) is used for local conditions. For example, for the Danube ecosystem, the turbulence is moderate to high and water depth varies considerably. The algae grow more towards the shore, and average characteristics are considered in order to derive a simplified model, where both the temperature and the irradiance are generic parameters. In the present model, benthic algae are considered to have a maximum growth rate of 0.01 day⁻¹ depending on water temperature and daily average irradiance, given by:

\[
\mu_{\text{ba}} = 0.01 \times 1.07^{(T - 8)} \times \text{modlight}^{0.31} \quad (6)
\]

where μ_ba is the growth rate of benthic algae (day⁻¹), T the average water temperature (°C) and modlight the moderator of seasonal irradiance variability, considered the same one as for phytoplankton Eq. (4).

The approach considered in the present model is conservative, ignoring the discrimination factor (i.e. the ratio of tritium to hydrogen, T/H) of about 0.6, used in the recent recommendations (IAEA 2010).

The mass fraction of dry matter in benthic algae has a mean value of 0.08. The growth rate used in the description of the Danube ecosystem is not generally valid, and variations by a factor of 3 in this parameter are expected for other local conditions.

#### OBT dynamics in consumers

For all the other aquatic organisms (zooplankton, crustaceans, molluscs and fish), the OBT concentration dynamics, including the specific hydrogen (tritium) metabolism, is well described in a previous study (Galeriu et al. 2005). The general equation for OBT dynamics in consumers is:

\[
\frac{\mathrm{d}C_{\text{org,x}}}{\mathrm{d}t} = a_x C_{f,x}(t) + b_x C_w(t) - K_{0.5,x} C_{\text{org,x}} \quad (7)
\]

where C_org,x is the OBT concentration in the animal, x (Bq kg⁻¹ fm); C_f,x is the OBT concentration in the food of animal, x (Bq kg⁻¹ fm); a_x the transfer coefficient from OBT in the food to OBT in the animal, x (day⁻¹); b_x the transfer coefficient from HTO in the water to OBT in the animal, x (day⁻¹); and K_0.5,x the biological loss rate of OBT from animal, x (day⁻¹).

For a proper mass balance, it is necessary to introduce the following relationship (Galeriu et al. 2005):

\[
C_f = \sum_{i=1}^{n} C_{\text{prey},i} P_{\text{prey},i} \frac{\text{OBH}_{\text{pred}}}{\text{OBH}_{\text{prey},i}} \quad (8)
\]

where C_f is the OBT concentration in animal's food (Bq kg⁻¹ fm); C_prey,i the OBT concentration in prey, i (Bq kg⁻¹ fm); P_prey,i the preference for prey, i; and OBH_x the organically bound hydrogen (OBH) content in organism, x (prey or predator) (g OBH kg⁻¹ fm).

In the absence of the relevant data, the ratio of OBH in predator and prey can be assessed from the dry matter ratio, with a moderate loss of accuracy.

Equations (7) and (8) refer to a model with a single OBT compartment with more than one source of OBT production: from HTO in water or OBT in food. When HTO dominates as the primary source, the specific activity approach can be used. The specific activity (SA) of tritium is defined as the ratio of the tritium activity to the mass of hydrogen in a specific form. The specific activity ratio (SAR) is the ratio of the SA of OBT in the animal to the SA of HTO in water. Based on a literature review (Heling and Galeriu 2002; Galeriu et al. 2005), the values for SAR in different aquatic organisms when the source is HTO are given in Table 1.

**Table 1. Specific activity ratio (SAR) and standard deviations (sd) for aquatic organisms when the source is HTO**

| Aquatic organisms | SAR (HTO source) ± sd |
| :--- | :--- |
| Zooplankton | 0.4 ± 0.1 |
| Molluscs | 0.3 ± 0.05 |
| Crustaceans | 0.25 ± 0.05 |
| Planktonivorous fish | 0.25 ± 0.05 |
| Piscivorous fish | 0.25 ± 0.05 |

Using the specific activity approach and the equilibrium conditions, the transfer coefficients in Eq. (7) are now defined as:

\[
\begin{aligned}
a_x &= (1 - \text{SAR}_x) \times K_{0.5,x} \\
b_x &= \text{SAR}_x \times K_{0.5,x} \times \frac{\text{SAP}_{\text{pred}}}{111}
\end{aligned} \quad (9)
\]

where SAR_x is the specific activity ratio in animal, x; SAP_pred the specific activity of bound hydrogen (BH) in the predator (kg BH kg⁻¹ fm); and 111 the mass of free hydrogen (kg) in 1 m³ of water.

With the exception of fish fat, SAP_pred is about 0.06 × Dry_pred depending on the dry matter fraction of the predator. For fish fat, a value of 0.08 × Dry_pred is recommended for SAP_pred.

#### OBT dynamics in zooplankton

The OBT biological loss rate, K_0.5 for zooplankton depends on its growth rate and temperature (Ray et al. 2001). At a reference temperature of 20°C and considering the zooplankton volume, the OBT biological loss rate is given by:

\[
K_{0.5,20} = (0.715 - 0.13 \times \log(V)) + (0.033 - 0.008 \times \log(V)) \quad (10)
\]

where K_0.5,20 is OBT biological loss rate at the optimal reference temperature of 20°C (d⁻¹) and V the zooplankton volume (μm³).

In Eq. (10), the first pair of parentheses corresponds to the growth rate and the second to the respiration rate. Generally, the species of zooplankton have the volume between 10 and 10⁴ μm³, and the OBT biological loss rate at the reference temperature, K_0.5,20 varies between 0.19 and 0.7 day⁻¹, with an average of 0.3 day⁻¹. For the present case, the minimum value of K_0.5 is chosen as appropriate for large zooplankton:

\[
K_{0.5} = 0.19 \times 1.06^{(T - 20)} \quad (11)
\]

In Eq. (11), temperature dependence was introduced.

The dry matter fraction of zooplankton varies between 0.07 and 0.2; here, a value of 0.12 is used as a default value.

#### OBT dynamics in zoo-benthos

The benthic fish consume macroinvertebrates and especially aquatic insect larvae of the order Diptera. The most widespread ones are those from the Chironomidae (or chironomid) family, which has two to six life cycles per year. In some lakes, there are insect larvae with a density of 2,000 individuals per m³ (McDermot and Rose 2000). Generally, chironomid larvae are assumed to have a growth rate of 0.05 day⁻¹ and a respiration rate of 0.01 day⁻¹ (Heling 1995). Consequently, the OBT biological loss rate for chironomid larvae, K_0.5 is 0.06 day⁻¹ (Heling 1995). A higher value (K_0.5 = 0.2 day⁻¹) is used in the CASTEAUR (French acronym for Simplified Calculation of radioactive nuclides Transfer in Receiving WATERways) model (Beaugelin-Seiller et al. 2002). In the present application, an average value, K_0.5 = 0.1 day⁻¹ is used. All the previous values for K_0.5 correspond to an average water temperature of 12°C. In the absence of relevant data, for other water temperatures, the temperature correction functions were considered as those for molluscs and crustaceans.

Small molluscs and crustaceans have a very large variability, and the calculations of their OBT biological loss rates must be adapted to different cases. For molluscs, a literature review (Heling and Galeriu 2002) gives a K_0.5 of 0.02 day⁻¹ for a body mass of 1 g fm but a K_0.5 of 0.005 day⁻¹ is used for 30 g of soft tissue. For crustaceans, the same review (Heling and Galeriu 2002) cites an average value of 0.007 day⁻¹ for K_0.5. By comparison, for molluscs, a value of 0.017 day⁻¹ for K_0.5 is given in the literature (Heling 1995). Based on experimental data for the growth rate and the energy content of Mytilus edulis soft tissue (2,386 J per g wet tissue), the following relationship can be derived (Sukhotin et al. 2002):

\[
K_{0.5} = 0.024 W^{-0.246} \quad (12)
\]

where W is the wet mass of mussel soft tissue (g fm).

Recent experiments concerning OBT dynamics for Elliptio complanata, with a total mass of 90 g (40 g wet mass), give a value of 0.02 day⁻¹ for K_0.5 (IAEA 2008; Yankovich et al. 2011), a value that is a few times higher than that for Mytilus edulis (Sukhotin et al. 2002).

For the food chain modelling, molluscs and crustaceans are of interest, since they are consumed by humans and various species of zoo-benthos are consumed by fish. The model has two separate compartments. For human consumption, mussels and crabs of large body mass (about 20 g fm for both mussels and crabs) are included and the model parameters are adapted to approximate this mixture. By default, a biological loss rate of 0.007 day⁻¹ is assumed for OBT, but model users must adapt this value to their specific cases. As fish prey, zoo-benthos of smaller body mass (about 1 g fm) are considered and a range of 0.04–0.1 day⁻¹ is assumed for the OBT biological loss rate. Temperature dependence is introduced as a multiplicative factor, as follows:

\[
\begin{aligned}
K_{0.5} &= F(T) \times K_{0.5\_o} \\
F_{\text{molluscs,crustaceans}}(T) &= \frac{0.043 - 0.0159 \times T + 0.003 \times T^2 - 5.3 \times 10^{-5} \times T^3}{0.51}
\end{aligned} \quad (13)
\]

where F(T) is the temperature correction function and K_0.5_o the OBT biological loss rate at standard temperature (day⁻¹).

The temperature dependence of the OBT biological loss rate for molluscs and crustaceans (Eq. (13)) is considered, based on experimental data for a Tridacna species (Hean and Cacho 2003), without any guarantee that it is correct for the specific applications (i.e. the cases considered in the present study).

There is large variability in the influence of body mass and temperature on aquatic invertebrate respiration (Brey 2010), and in specific cases, the literature must be consulted for improved parameters.

#### OBT dynamics in fish

There are very few experimental data for OBT biological loss rates in fish. For a small goldfish (Carassius auratus) of about 10 g, a biological half-life of 8.7 days has been reported for OBT (Elwood 1971); for small-bodied rainbow trout (Salmo gairdneri) with a body mass between 7 and 16 g fm fed with tritiated amino acids, the OBT biological half-life was about 25 days (Rodgers 1986). In the absence of experimental data, models based on bioenergetics are used here, as it has been experimentally demonstrated that the mass dependence of basal metabolic rate of fish is a combination between the tissue-specific respiration rate and the relative size of different tissues (Oikawa and Itazawa 2003). The same approach as for mammals (i.e. the energy metabolism approach) (Galeriu et al. 2009) can also be considered for aquatic fauna for tritium transfer.

Bioenergetics involves the investigation of energy expenditure, losses, gains and efficiencies of transformations in the body. The basic equation for bioenergetics models (BEMs) of fish growth is as follows (Hanson et al. 1997):

\[
\frac{1}{W} \frac{\mathrm{d}W}{\mathrm{d}t} = [C - (R + S + F + E + P)] \frac{\text{cal}_p}{\text{cal}_f} \quad (14)
\]

where W is the fish mass (g fm), t the time (day), C the consumption (g prey g⁻¹ fish day⁻¹), R the respiration or losses through metabolism (g prey g⁻¹ fish day⁻¹), S the specific dynamic action or losses because of energy costs of digesting food (g prey g⁻¹ fish day⁻¹), F the egestion or losses through faeces (g prey g⁻¹ fish day⁻¹), E the excretion or losses of nitrogenous wastes (g prey g⁻¹ fish day⁻¹), P the egg production or losses through reproduction (g prey g⁻¹ fish day⁻¹), and cal_p, cal_f are caloric equivalents of pray (J g⁻¹) and fish (J g⁻¹), respectively.

The equation for consumption is:

\[
C = C_{\text{max}} \times p \times f_c(T) \quad (15)
\]

where C is the consumption (g prey g⁻¹ fish day⁻¹), C_max the allometric equation for maximum specific consumption rate (g prey g⁻¹ fish day⁻¹), with C_max = aWᵇ where a and b are allometric coefficients for fish, p the proportion of maximum consumption and f_c(T) a temperature-dependent function.

Respiration is measured as oxygen consumption and it is converted to consumed prey, by knowing the energy equivalent of oxygen (13,560 J g⁻¹ O₂) and the prey energy density. Respiration depends on temperature, fish mass (allometric function) and activity:

\[
R = a_r W^{b_r} f_r(T) \text{ACT} \times \text{conv} \quad (16)
\]

where R is the respiration (g prey g⁻¹ fish day⁻¹), a_r and b_r are allometric coefficients (a_r is usually given in units of O₂ consumption per g fish and unit time), f_r(T) the temperature function of respiration, ACT an activity multiplier depending on fish average swimming speed, and conv is the oxygen consumption converted to consumed prey (13,560 J g⁻¹ O₂ cal_p⁻¹).

Note that all the units in Eqs. (14)–(16) are reported on a fm basis.

In many applications, the specific dynamic action (S), the egestion (F) and the excretion (E) depend on consumption, as an overall fraction (ε), and the relative growth rate (RGR) is given by Eq. (17):

\[
\text{RGR} = \frac{1}{W} \frac{\mathrm{d}W}{\mathrm{d}t} = (1 - \varepsilon) C - R \frac{\text{cal}_p}{\text{cal}_f} \quad (17)
\]

The OBT biological loss rate, K_0.5, can be given as:

\[
K_{0.5} = \text{RGR} + R \frac{\text{cal}_p}{\text{cal}_f} \quad (18)
\]

In Eq. (18), the effect of growth dilution (RGR) and the metabolic (respiration) rate must be noted.

At maintenance (RGR = 0) the OBT biological loss rate is given only by respiration. The development and application of BEMs increased substantially in the last decade. BEMs are appealing because they are based on balanced energy-fate equations that have been thought to promote reasonable predictive behaviour. However, most BEMs have not been well evaluated over the ranges of conditions to which they have been applied. Results indicate that many BEMs are substantially inaccurate when predicting fish growth with higher feeding rates or estimating consumption with higher growth rates, even when higher consumption levels or growth episodes are of short duration (Bajer et al. 2004). Further work is needed to evaluate temperature, sub-maintenance feeding and prey-type effects on the performance of BEMs, as well as possible influences of swimming activity level (i.e. ACT in Eq. (16)). In a recent review (Chipps and Wahl 2008), BEMs have been analysed in relation to field and laboratory experimental data. Field tests of bioenergetics models have generally revealed poor fits between model predictions and field estimates; however, a reasonable agreement (15%) was obtained between model and field values for lake trout (Salvelinus namaycush), largemouth bass (Micropterus salmoides) and sockeye salmon (Oncorhynchus nerka) (Chipps and Wahl 2008). Laboratory tests also show poor performance (Bajer et al. 2004). Disagreement between BEMs and laboratory data are largest when attempting to account for a range of temperatures and variable ration levels on model estimates. Subtle physiological adaptations of fish species to local environment can also have an important influence on the accuracy of BEMs predictions.

#### Dissolved organic tritium (DOT)

The model previously described is based on the assumption that the OBT specific activity in fish is directly linked with the HTO in water or the OBT in fish food. This is fully valid if the water contamination is due only to an initial HTO source. Taking into account this supposition, the concentration factor (CF) in fish must be less than or equal to 1. Classically, the concentration factor has been defined as the ratio of the concentration per unit mass of biota at equilibrium to the dissolved concentration per unit volume in ambient water.

For the marine environment at Cardiff, UK, CFs for tritium in biota have been investigated (McCubbin et al. 2001; Williams et al. 2001). For flounder (Platichthys flesus) and mussels (Mytilus edulis), CFs of up to 4 × 10³ (fresh mass equivalent) were reported. The significant increase in CF compared with unity has been attributed to the uptake of tritium in organically bound forms, due to the existence of organic species of tritium in a mixture of compounds in the authorized releases of wastes to the Bristol Channel from the Nycomed-Amersham (now GE Healthcare) radiopharmaceutical plant at Whitchurch, Cardiff, UK. A review of past monitoring results was recently published (Hunt et al. 2010), and difficulties with analytical methods regarding OBT have been pointed out. The extremely large CFs cannot be explained by analytical errors, and many hypotheses have been advanced. These include the concentration of organic tritium by bacteria and subsequent transfer in the food chain; ingestion of contaminated sediment; ingestion of contaminated prey; and direct uptake of DOT from the sea water. It was suggested that bioaccumulation occurs via a pathway for the conversion of the tritium-labelled organic compounds into particulate matter (via bacterial uptake/physico-chemical sorption) and the subsequent transfer to the food chain (McCubbin et al. 2001). Comparison of monitoring data for sediment and suspended matter with data on tritium in benthic fauna shows that the ingestion of sediment or particulate matter is not a reasonable explanation, since the OBT concentration in benthic fauna is much higher than the OBT concentration in both sediments and suspended matter.

Phytoplankton can selectively assimilate dissolved organic carbon (DOC) from water (Neilson and Lewin 1974), and laboratory experiments show that they can do the same for tritiated organics (Strack et al. 1983). The same is true for mussels (Jorgensen 1983). In a review about amino acid transport in marine invertebrates, Wright and Stephens (1982) pointed out that soft-bodied marine invertebrates have the ability to accumulate some radioactively labelled amino acids and most of these soft-bodied marine invertebrates have a net influx. The transport process is transepidermal in nature and can be described by Michaelis-Menten kinetics. Transport rates are related to the levels of metabolic energy, and the accumulated substances are accumulated via general metabolic pathways. It is important to note that this transport process is rarely observed in freshwater invertebrates. Michaelis-Menten kinetics can be described by the following equation:

\[
J^i = \frac{J_{\text{max}}^i [S]}{K_t + [S]} \quad (19)
\]

where Jⁱ is the influx rate of substrate (μmol g⁻¹ h⁻¹), J_maxⁱ the maximal rate of influx (μmol g⁻¹ h⁻¹), [S] the concentration of substrate (μmol L⁻¹) and K_t the concentration of substrate at which the influx is one-half of the maximal value (μmol L⁻¹).

In a review of amino acids uptake (Wright and Stephens 1982), the observed range of J_maxⁱ is 0.1–10 μmol g⁻¹ h⁻¹ and the range of K_t is 1–100 μmol L⁻¹. When the concentration of substrate is much smaller than the half saturation constant, Eq. (19) is simplified and it can be used to define an uptake rate as follows:

\[
V = \frac{J_{\text{max}}^i}{K_t} \quad (20)
\]

In the past, some experiments have been done using marine unicellular algae (Dunaliella bioculata and Acetabularia mediteranea), which have been grown in ten different tritiated organic solutions of amino acids (Strack et al. 1983). The organics have been supplied to the algae culture for 30 min, and the CR (on a fm basis) varied between 0.17 and 122 (i.e. by three orders of magnitude). The maximum CR was for adenine in Dunaliella bioculata. In a separate experiment (Strack et al. 1980), Michaelis-Menten kinetics were analysed for adenine uptake in Dunaliella bioculata and the uptake rate, V, was estimated to be 4,800 L g⁻¹ dm h⁻¹.

The direct uptake of DOT can be introduced in the dynamic equation for phytoplankton Eq. (2) and consumers Eq. (8), respectively:

\[
\begin{aligned}
\frac{\mathrm{d}C_{\text{o,phpl}}}{\mathrm{d}t} &= 0.4 \cdot \mu \cdot \text{Dryf} \cdot 0.001 \cdot C_W + V_{\text{DOT}} \times C_{\text{DOT}} - \mu \cdot C_{\text{o,phpl}} \quad (21) \\
\frac{\mathrm{d}C_{\text{org,x}}}{\mathrm{d}t} &= a_x C_{f,x}(t) + b_x C_w(t) + V_{\text{DOT}} \cdot C_{\text{DOT}} - K_{0.5,x} C_{\text{org,x}} \quad (22)
\end{aligned}
\]

where C_W is the HTO concentration in water (Bq m⁻³), C_DOT the DOT concentration (Bq L⁻¹) and V_DOT the uptake rate of DOT (L kg⁻¹ fm day⁻¹).

## Results

### OBT in phytoplankton and zooplankton

The OBT dynamic equation for phytoplankton (Eq. (2)) was successfully tested with many experimental data (Heling and Galeriu 2002). There are no direct data for OBT biological loss rate in zooplankton, but the dynamics of OBT concentration in a species of zooplankton (Artemia salina) (Komatsu et al. 1981) is consistent with the generic value used in the present model (given by Eq. (11)).

### OBT in molluscs and crustacean

Due to the large variability of respiration rate in invertebrates (Brey 2010) and the paucity of the experimental data for OBT biological loss rate (Heling and Galeriu 2002), it is not possible to use a single robust, generic value. The experimental data for Mytilus edulis are closely reproduced by the present model, but only those for marine clams (Mya arenaria) are predicted within a factor of 2–3, using the available data for respiration.

### OBT dynamics in fish

In a previous study (Galeriu et al. 2005), the OBT biological loss rates for few fish using generic model parameters (McDermot and Rose 2000) have been assessed, but in the present study, only the cases with experimental verification have been selected. An excellent case is for the Pacific herring (Cupea harengus pallasi) (Megrey et al. 2007). In this specific case, the model parameters have been obtained mainly from the laboratory experiments, and the realistic seasonal changes in water temperature and prey availability have been considered. Herring is a pelagic fish and its food consists of various kinds of zooplankton with seasonally varying availability. Prey availability (consumption fraction) and temperature dynamics are the major factors influencing the dynamics of OBT biological loss rate (Fig. 1). For herring masses (in the consumption mass range) (Fig. 2), the OBT biological half-life varies between 60 and 170 days. For another pelagic fish, the Pacific saury (Cololabis saira) near the Japanese coast (Ito et al. 2004), the range of OBT biological half-lives for a similar mass is 40–60 days, due to differences in metabolism, water temperature and prey availability between two species and sets of conditions.

*[Fig. 1. Temperature and prey availability dynamics (consumption fraction is multiplied by 50, in order to have a similar scale with that one for temperature) for Pacific herring]*
*[Fig. 2. Fresh mass and OBT biological loss rate dynamics (multiplied by 10⁴, in order to have a similar scale with that one for mass) for herring in the Pacific Ocean]*

Roach (Rutilus Rutilus) are widely distributed in European freshwater habitats and are included in the present model. Laboratory experiments for consumption and respiration have been done for a mass range of 1.2–300 g and a temperature range of 5–23°C, providing improved parameters (Hoelker and Haertel 2004), hereafter referred to as HH. The improved parameters (HH), as well as an old set of parameters (Horppila and Peltonen 1997), hereafter referred to as HP, have been used to assess the OBT biological half-life. The results are given in Table 2 for a fish of mass 200 g fm, close to the mass of fish sold in markets, for two feeding regimes: at maintenance ration and at half of maximum feeding rate.

**Table 2. OBT biological loss rate of roach for two feeding regimes**

| Temperature (°C) | Maintenance ration¹ (HP²) | Maintenance ration¹ (HH³) | Half maximum feeding rate¹ (HP²) | Half maximum feeding rate¹ (HH³) |
| :--- | :--- | :--- | :--- | :--- |
| 5 | 0.0011 | 0.0016 | 0.0035 | — |
| 10 | 0.0020 | 0.0031 | 0.0065 | — |
| 15 | 0.0036 | 0.0026 | 0.0114 | — |
| 20 | 0.0063 | 0.0061 | 0.0192 | — |
| 25 | 0.010 | 0.008 | 0.028 | — |

¹ Feeding regimes.
² Old set of parameters (Horppila and Peltonen 1997).
³ Improved set of parameters (Hoelker and Haertel 2004).

In the case of roach, it was possible to predict the biological half-life of OBT to within an uncertainty better than a factor 2, using this model, which is remarkable. For a constant mass and diet availability, the temperature effect causes the OBT biological half-life to increase from about 17 days in summertime (fast growth) to 630 days in wintertime (at maintenance ration).

Flounder is a benthic fish that is found throughout Europe and America, in estuaries and shallow coastal zones. Recently, a bioenergetic model was developed for European flounder (Platichthys flesus) (Stevens et al. 2006). For this case, the prey availability is quite constant in the model scenario over the seasons, and the biological loss rate of OBT is influenced mostly by water temperature and is slightly dependent on fish mass. During the wintertime, the minimum temperature was 5°C and during the summertime, the maximum temperature was 16°C. The OBT biological half-lives cover a range of 55–455 days, with an increase in fish mass from 34 g fm (1 January 1974) up to 400 g fm (2 years later). In the case of the Southern flounder (Paralichthys lethostigma) (Burke and Rice 2002), the OBT biological loss rate can vary with a factor of 2 for similar environmental conditions and fish masses.

Similar parameters to those discussed earlier are also needed for smaller-bodied fish species. For example, based on experimental work that was done for mosquito fish (Gambusa affinis) by Chipps and Wahl (2004), an OBT biological half-life of 21 days was estimated for a fish mass of about 1 g fm at a temperature of 15°C as a model parameter. The OBT biological half-life then decreases to 6 days for a temperature of 35°C.

The interest in BEMs is driven by the need to assess the OBT dynamics, and the authors refer to few experimental data. A laboratory experiment was conducted using fathead minnows (Pimephales promelas) in order to study OBT dynamics in fish fed with clean food but that were living in contaminated water (HTO) (Kim SB, personal communication, 2010). In this experiment, the fish mass was about 1.5 g and the fish were kept in water contaminated with 30,000 Bq L⁻¹ of HTO for 43 days at a constant temperature of 25°C. BEM parameters have been taken from literature (Petersen and Paukert 2005), and the energy density was approximated from that of a similar species, the bluntnose minnow (Pimephales notatus) (Ruetz et al. 2009). The model predicts a tritium concentration in the combustion water at the end of experiment of 4,250 Bq L⁻¹, while the experimental data show 2,730 Bq L⁻¹.

For rainbow trout (Oncorhynchus mykiss), the OBT dynamics was studied for juveniles (Rodgers 1986) and adults (Kim SB, personal communication, 2010). Juvenile rainbow trout were kept in tritiated water and/or received a diet labelled with tritiated amino acids at a constant temperature of 15°C. The average mass of fish increased from 7.0 ± 0.2 g fm up to 15.7 ± 0.6 g fm during the course of the 10-week experiment (with 56 days for tritium uptake). Based on the experimental data during exposure to a tritiated diet, the OBT rate constant was 0.0218 ± 0.002 day⁻¹, while in the next 2 weeks after exposure, the estimated value was 0.0308 ± 0.0031 day⁻¹. For the juvenile rainbow trout model in AQUATOX (Park and Clough 2009), the OBT rate constant for the experimental condition, such as mass range and water temperature, considered was close to 0.03 day⁻¹. More recently, an updated model for rainbow trout was successfully used (Tyler and Bolduc 2008). When this last model was applied for OBT dynamics, the rate constant was 0.037 day⁻¹. These results must be considered with caution, however, because under laboratory conditions, the fish activity is lower than under field conditions and the models use a mixture of parameters that are not fully coherent.

### EMRAS mussel scenario

Within the framework of the Tritium and C-14 Working Group coordinated under the IAEA's EMRAS programme, one of the scenarios was dedicated to tritium contamination of mussels (Elliptio complanata) (IAEA 2008; Yankovich et al. 2011). In the first phase of the scenario, the mussels were relocated from a low-background area to a tritium-contaminated lake, and the uptake of tritium, including OBT, was studied for 84 days (uptake phase). In the second phase, mussels grown in a contaminated lake were relocated in clean water, and tritium depuration was studied for 117 days (depuration phase) (Yankovich et al. 2006, 2008). The AQUATRIT model had been tested for this scenario, using its earlier set of parameters (Galeriu et al. 2005) (i.e. K_0.5,0 = 0.022 day⁻¹). For the uptake phase, the model underpredicted the experimental data by a factor of up to 5 for the first 6 days and for the later phase of the experiment, the model's predictions were close to the experimental data (Yankovich et al. 2011). For the depuration phase, the model largely underpredicted the experimental data by a factor of up to 15. By decreasing the biological loss rate used in the model to 0.004 day⁻¹, the agreement between the model predictions and the data is good, but this contradicts the uptake parameter values. It seems that a simple model with only one compartment is not appropriate for such a scenario with abrupt changes in the environmental conditions. After long discussions with the members who participated in the Tritium and C-14 Working Group, more alternatives had been tested. The experimental values for the respiration rate of another species of mussels (Mytilus edulis) indicate an OBT biological loss rate of about 0.01 day⁻¹, which is intermediate between the values of the best fit for the uptake and depuration phases, but still the model performances were not robust enough. Therefore, a two-compartment model was used by one of the participants with good performances for the depuration phase, but with poorer performance for the uptake phase (Yankovich et al. 2006). Model predictions seem to improve when the stomach contents and a single OBT compartment are considered. When the mussels are moved to a contaminated water body, the stomach is saturated with contaminated food within a few hours, and the food gradually passes to the rest of the body. Considering a stomach representing a fraction of 0.3 of the whole body and an OBT biological loss rate of 0.011 day⁻¹, both the uptake and the depuration phases are successfully modelled (the model prediction is within up to a factor of 2).

### Danube ecosystem

There are two CANDU 6 (CANada Deuterium Uranium) reactors operating at Cernavoda (Romania) situated at the Danube River. A scenario for a hypothetical accidental tritium release into the Danube River of 3.7 PBq for 6 h is analysed using the information about the Danube River and Delta ecosystem gathered in a recent environmental impact assessment (ICIM 2003). Seasonal changes in water flows and temperature were considered, and the model parameters were adjusted for predominant species of phytoplankton, zoo-benthos and fish. The Danube ecosystem is oligo-mesotrophic (i.e. an ecosystem with intermediate levels of nutrients and oxygen). The dominant phytoplankton species are diatoms and their density varies between 1.1 and 4.4 mg L⁻¹, while zooplankton is dominated by rotifers and is of low density. For zoo-benthos, the predominant species are Chironomus and zebra mussel (Dreissena polymorpha). The biological loss rate of OBT from zooplankton was set to 0.19 day⁻¹; for zoo-benthos, two values have been used: 0.1 day⁻¹, if Chironomus predominates, and 0.04 day⁻¹, if zebra mussels predominate. The Danube River and Danube Delta are rich in fish species, but this study is focused only on fish consumed by humans. Fishing production data for planktonivorous and omnivorous fish were used in the model as follows: for carp (Cyprinus carpio), 37% from the total fishing production was assumed; for bream (Abramis brama and Blicca bjoerkna), a value of 10% from the total fishing production was assumed; and for gold fish (Carassius auratus gibelio), 3% from the total fishing production was assumed. For piscivorous fish species, the following assumptions were made in the model: 21% from the total fishing production for European catfish (Silurus glanis); 5% from the total fishing production for zander (Stizostedion lucioperca); and 2% from the total fishing production for northern pike (Esox lucius). For modelling purposes, a carp with a mass of about 1,000 g fm was assumed and the bioenergetic parameters given in AQUATOX were used (Park and Clough 2009), adjusting the respiration in order to reproduce recent data on respiration (Ohlberger et al. 2005). The diet of carp consists of 40% benthic algae, 10% zooplankton and 50% zoo-benthos. Pike and zander were selected as a representative predatory fish species for modelling purposes, in the absence of any other relevant data for the European catfish, due to the robustness of available laboratory and field data (Keskinen et al. 2008). For this application, roach was selected as prey fish, with a mass of about 100 g fm, and robust model parameters have been selected (Hoelker and Haertel 2004). The roach diet consists of 60% zooplankton, 30% zoo-benthos and 10% benthic algae. Fish growth for local conditions over 2 years is given in Fig. 3. The biological loss rate for OBT from fish is given in Fig. 4. It is interesting to note the similarity of the values for roach and carp, despite the relatively large differences in the body masses between the two species. The effect of seasonal temperature on the biological loss rate for OBT is stronger than the effects of changes in the diet or body mass. Assuming a tritium release of 3.7 PBq on August 1 and a river flow of 6,000 m³ s⁻¹, the dynamics of OBT concentration in different types of aquatic organisms is given in Fig. 5.

*[Fig. 3. Fish growth (fresh mass) for local conditions in the Danube ecosystem and for 2 years]*
*[Fig. 4. Fish OBT biological loss rate for Danube ecosystem]*
*[Fig. 5. The dynamics of OBT concentrations in different aquatic organisms in the Danube ecosystem]*

In practice, an incident with tritium release in Danube River can occur at any time and it is useful to understand the seasonal effect of a release on human exposure to tritium through dietary composition of fish. Between years, the flow and temperature in the Danube River vary and for the same 3.7 PBq tritium release over 6 h the OBT in fish also varies (Table 3). Water temperature has a large influence on the OBT content in fish, and the highest effect is in late summer (September 15).

**Table 3. Model results for a hypothetical tritium release of 3.7 PBq for 6 h at different times of the year in Danube River**

| Date of release | River flow (m³ s⁻¹) | River temperature (°C) | Ingested activity of fish (Bq)¹ | % OBT² |
| :--- | :--- | :--- | :--- | :--- |
| February 15 | 3,000 | 3 | 22,844 | 3 |
| April 15 | 5,000 | 10.5 | 14,348 | 7.3 |
| May 15 | 3,500 | 17 | 21,831 | 13 |
| July 15 | 1,500 | 24 | 63,377 | 30 |
| September 15 | 1,000 | 20 | 92,430 | 28 |
| October 15 | 1,500 | 15 | 53,790 | 17.5 |
| December 15 | 1,500 | 5.5 | 46,415 | 4.4 |

¹ 0.5 kg of a mixture of carp and zander.
² Percentage of OBT coming from the ingested fish activity intake.

### Dissolved organic tritium (DOT)

For the Cardiff case, noted previously, the tritiated waste from GE Healthcare (formerly, Nycomed-Amersham) includes not only HTO and the by-product coming from the radiopharmaceutical industry but also highly bioavailable tritiated organic molecules (i.e. hydrocarbons, amino acids, proteins, nucleotides, fatty acids, lipids and purines/pyrimidines). For a local phytoplankton species (Isochrysis galbana) incubated with exposure to different tritiated compounds over a period of 10 days, the concentration ratio (on a dry mass basis) was 670 for protein precursors, 410 for lipids/fatty acids and much lower for other chemical forms (Williams J, personal communication, 2002). These results limit the range of the uptake rates of DOT, V_DOT to 15–80 L kg⁻¹ fm day⁻¹, which are in the low range of the literature values. Using the little information found in the literature (Flynn and Syrett 1986), there is likely some influence of temperature and light availability on the uptake rate of DOT. In the present study, the same modifying factors were assumed as those previously used for phytoplankton Eqs. (2) and (4). In the absence of relevant local data for zooplankton, the biological half-life used is that for phytoplankton (Isochrysis galbana).

For other invertebrates, some data for mussels (Mytilus edulis) were used (Williams J, personal communication, 2002). After an incubation of nine days, the concentration ratio (dry matter) was 238 for protein precursors and for synthetic chemicals, and much lower for other chemical forms. This indicates a range of 2–7 L kg⁻¹ fm day⁻¹ for V_DOT, which is much lower than those found in literature (Jorgensen 1983).

Model input parameters included the annual average of total tritium and organic tritium releases from the emissions of GE Healthcare, whereas the tritium concentration in sea water and the monitoring data for mussel and flounder were taken from the literature (Hunt et al. 2010; Croudace and Warwick 2005; Warwick et al. 2002; Leonard et al. 2001; Morris 2006; RIFE-14 2009). Since April 2003, 70% of the total release was in the form of OBT, whereas 80% of the highly bioavailable, tritiated organic molecules have been removed (Morris 2006). For the uptake rate of DOT, a value of 45 L kg⁻¹ fm day⁻¹ was assumed for phytoplankton and half of this value for zooplankton. Mussels (Mytilus edulis) are often used for monitoring purposes and in the present model, the DOT uptake rate was assumed to be 15 L kg⁻¹ fm day⁻¹ with a biological loss rate of OBT corresponding to a soft mass of 10 g fm (see Eq. (13)). The zoo-benthos includes crustaceans with low accumulation of DOT, and consequently, the DOT uptake rate is considered to be half that of the mussel. The zoo-benthos is an unknown mixture of many species (mussels, crabs, winkles, etc.), and consequently, the OBT biological loss rate is difficult to assess. Therefore, a range of 0.01–0.04 day⁻¹ was considered. For flounder (Platichthys flesus) with the mass of about 300 g fm, the fish bioenergetics parameters have been taken from literature (Stevens et al. 2006).

Using the available input data, the model successfully predicts the trend in total tritium (mostly as OBT) concentration in mussels (Fig. 6) and flounders (Fig. 7).

*[Fig. 6. Comparison between model results and monitoring data for total tritium in mussels (Mytilus Edulis) in Cardiff Bay]*
*[Fig. 7. Comparison between model results and monitoring data for total tritium in flounder (Platichthys flesus) in Cardiff Bay]*

Intensive monitoring activity carried out in 1999–2000 (Leonard et al. 2001) shows that the pelagic fish have a tenfold lower tritium concentration than that of the benthic flounder. This is also seen in the model outputs (considering herring as a pelagic fish).

Despite the uncertainty in parameter values, the above results demonstrate that the direct uptake of DOT by phytoplankton and invertebrates is the most probable explanation for the OBT dynamics in fish species in the Cardiff area.

## Discussion

### OBT dynamics in fish

In the literature (Blaylock et al. 1986), biological loss rate of OBT of about 5 days⁻¹ for a mosquito fish (Gambusa affinis) is reported, although the fish body mass and water temperature are not reported. Using the present model and bioenergetics parameters for mosquito fish (Chipps and Wahl 2004), a biological loss rate of 5 days⁻¹ has been estimated for OBT for a fish body mass of 0.5 g fm at a water temperature of 25°C. For a small-bodied goldfish (Carasius auratus), an OBT biological loss rate of 8.7 days⁻¹ has been reported in the literature (Elwood 1971), but again, the details regarding the fish body mass and the water temperature were not reported. It is possible to closely compare the results from the present model for Cyprinidae, with the experimental data for the biological loss rate of OBT for small-bodied fish, by a factor of 2.

Experimental data for larger fish are not reported in the literature, but there is work in progress to quantify these parameters (Kim SB, personal communication, 2010) for rainbow trout with a body mass of about 400 g fm at a water temperature of 15°C. For this case, the present model predicts an OBT biological loss rate of about 40 days⁻¹.

The sensitivity studies performed for the present model results suggest that under field conditions, the major factors influencing the OBT biological loss rate are temperature and prey availability.

### Danube ecosystem

The model results are influenced by uncertainty in parameters values. It is hard to identify the correct value to use for both OBT uptake and the biological loss rate of benthic algae under conditions of variable water depth and turbidity. By varying the values for benthic algae parameters by a factor of 10, the total OBT intake from fish ingestion varies by less than 10%. The predominant species of the zoo-benthos can vary in different locations within the river, also. That said, when the OBT biological loss rate of Chironomus is changed to the value for Dreissena polymorpha, the intake activity from fish consumption varies by less than a factor of 5.

Fish OBT biological loss rate can also vary under field conditions. For example, the metabolic rates reported in the literature for zander and pike can vary by at least a factor of 2. The carp metabolism also adapts to various environmental conditions, and the values used in the present model have not been tested for the Danube ecosystem. All the fish OBT biological loss rates have been varied by a factor of 3, and the model results have been compared with the initial selection of model parameters (Galeriu et al. 2005) with respect to OBT activity intake. The lowest OBT activity from fish ingestion by humans occurred when all the rates were increased by a factor of 3, at a value of 70% from the initial selection of model parameters (Galeriu et al. 2005). The OBT activity intake by humans increases by 5% when the carp biological loss rate is decreased by a factor of 3. The model was used also to maximize the activity intake, allowing the key parameters to cover all the physical ranges. The maximum intake increased by only 15% compared with the values in Table 3.

After a hypothetical accidental release of HTO into the Danube River, the total tritium intake by reference persons in the absence of countermeasures includes that from drinking water and from the crops contaminated by irrigation. Preliminary results show that the total tritium intake is about four times higher than the intake coming only from the ingestion of fish with an effective dose of about 0.01 mSv. Based on the outcomes of the hypothetical scenario that was tested by the EMRAS Tritium and Carbon-14 Working Group, the radiological impact of an atmospheric release of the same amount of tritium (3.7 PBq) is expected to be at least 100 times higher (IAEA 2009).

Due to the high dilution of tritium in the Danube River, the consequences of an accidental release would be minor, but this cannot be taken as general rule for all ecosystems or situations, and each particular case must be tested separately.

### Dissolved organic tritium (DOT)

In the Cardiff area, the specific molar activity of dissolved organic matter (DOM) releases from the radiopharmaceutical factory is extremely high (up to 1000 GBq mmol⁻¹); however, the high dilution in sea water gives a very low value (on the order of pmol L⁻¹), resulting in a relatively minor contribution to the natural concentration of DOM. For these values, Eqs. (21) and (22) can be applied.

The previous model results must be considered with some restrictions:

(a) seasonal variability of tritium release (including organic tritium) is not known and the type of organic molecules released can vary over a year—detailed information is not available;
(b) DOT transfer to marine phytoplankton and invertebrates is less well documented in relation to biological species and chemical forms of organic tritium—uncertainty in model parameters is high and difficult to assess;
(c) monitoring results for tritium are relatively few, with a spread of values that ranges by a factor of at least 3 amongst the providers (e.g., regulatory bodies, utilities, research institutions) and this would be expected to affect the relevance of the annual average of tritium concentration in the food chain.

In the absence of any explicit information, it is assumed that about half of the released organic tritium was in bioavailable forms before April 2004, but much less afterwards. The annual averages of tritium releases were used as model input values, in the absence of relevant monthly data. The measurement of DOT in sea water is difficult and generally, not reported in the literature, but with respect to the model input data, the same ratio of DOT: total tritium released was assumed as that assessed for the initial release (Morris 2006). In the model, the first year of release was 1983 (Day 100 in Figs. 6 and 7 is summer 1983). Before 1983, the tritium releases were low and they are not considered in the present study. It was estimated that before May 1998, 30% of tritium discharges were in organic forms rising to 80% after May 1998 (Morris 2006). From 1998, the tritium discharges were reduced for forms such as HTO and tritiated methanolic wastes. In April 2002, a new wastewater treatment unit was commissioned and some of the bioavailable organic tritium was retained. Since April 2003, the releases contain 70% OBT, but 80% of the bioavailable OBT releases were removed from the total releases and stored on-site. Since January 2004, the organic fraction in the releases was 30% (Morris 2006). In the model input data, the changes in the organic fraction have been considered only at mid-year, without refined details. The accumulation of organic species in sediment and the subsequent transfer to benthic fauna are ignored because the monitoring results show that the concentration of OBT in benthic fauna is much higher than in the sediment. Therefore, the direct uptake of DOT by marine invertebrates and the subsequent transfer in the food chain remain the major pathways in this case.

It is important to note that marine bivalves transport amino acids through the cell membranes against concentration gradients of 1:1 × 10⁷ mol L⁻¹, with the energy derived from the down-gradient co-transport of several Na⁺ ions into the organism. In brackish water or freshwater, in which down-gradient co-transport of Na⁺ is impossible because the ambient concentrations of Na⁺ ions in the ambient environment are similar to or less than those in the organism, the marine bivalves significantly reduce their gross uptake of amino acids (Baines et al. 2005). Direct uptake of DOM has been reported in saltwater, although an exception was noted for the zebra mussel (Baines et al. 2005).

## Conclusions

In late 1980, aquatic pathways were not considered of relevance to human dose after releases of tritium (HTO) (Blaylock et al. 1986), and simple models were used to predict tritium concentrations in biota, based on the specific activity approach. The occurrences of high concentration factors in Cardiff area later generated debate and public concern for the development of nuclear pharmaceutical production, since relatively high-activity concentrations of OBT were measured in benthic fish living in the receiving environment down-gradient of the Nycomed-Amersham (now GE Healthcare) radiopharmaceutical plant. The model described in the present study intends to be more specific than a screening-level model, including a metabolic approach, with the consideration of direct uptake of DOT by marine phytoplankton and invertebrates. The high concentration factors found in the Cardiff area are not a general problem in the nuclear industry. Instead, the Cardiff case reflects a specific biological process in marine invertebrates. In order to have better control of tritium release into the environment, not only tritiated water must be monitored, but also the other chemical forms and most importantly OBT, in the food chain.

**Acknowledgments** For the early phase of this research (2002–2005), we are grateful to Dr. Rudi Heling (KEMA NRG, The Netherlands). The Romanian Ministry of Education and Research partially funded the work described herein. We are very grateful to all the members of the Tritium and C-14 Working Group established in the frame of the EMRAS I programme (2002–2007), coordinated by IAEA Vienna, as well as to all the members of the Tritium "Accidents" Working Group established in the frame of the EMRAS II programme (2009–2011), coordinated by IAEA Vienna, for their fruitful discussions and collaboration. We are grateful to Dr. John Hunt (Centre for Environment, Fisheries and Aquaculture Science, UK) for his discussions and contribution to this topic. We wish to thank Dr. Sang Bog Kim (Atomic Energy of Canada Limited, Canada) for sharing with us some of his experimental results and his valuable comments, and to Dr. Julie Williams (GE Healthcare Amersham, UK) who provided us the useful local experimental data. We wish to thank the Food Standards Agency (UK) for providing us all their research reports on this topic. Last but not least, we are very grateful to Dr. Stuart Conney (Legislation and Environmental Hazards, UK) for his valuable comments and English revision.

## References

[List of references as in original text...]