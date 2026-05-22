# Study on tritium transfer from soil to plants and its existence form

**Michael Oftosu Portuphy**

*Ph.D. Dissertation, Kyushu University, September 2024*

## Abstract

In deuterium-tritium fusion reactors, substantial amounts of tritium are expected to be circulated and generated during operation. Since tritium is a radioactive substance, establishing the technology to confine it within facilities and handle it safely is the most important issue. To realize fusion reactors, it is necessary not only to advance technology but also to improve social acceptance, and the safety of fusion reactors must be explained to society. Therefore, in addition to establishing technology to safely confine tritium, it is also necessary to assess the impact on workers, the surrounding environment, and the public if tritium leaks outside. Tritium released into the environment goes through many migration processes before being taken into the human body. To improve the accuracy of human impact assessment, it is necessary to increase the reliability of individual migration models. Tritium is one of the radioactive substances produced in nuclear fission reactors and is present in the reactor cooling water. Additionally, large amounts of tritium are handled in the nuclear fuel reprocessing process. New knowledge about predicting the behavior of tritium in the environment will contribute to improving the accuracy of safety assessment for tritium not only in future fusion reactor facilities, but also in existing nuclear fission reactors, spent nuclear fuel handling facilities, accelerator facilities and so on.

Some of the tritium released into the atmosphere from fusion reactors permeates into the soil as tritiated water with rainfall. Additionally, since large amounts of tritiated water are handled, it is possible that tritiated water could be released into the surrounding soil in the event of an accident. Some calculation codes have been developed to predict the behavior of tritium released into the atmosphere, and estimate its transfer to food, and evaluate its impact on humans. However, the tritium transfer model used here is a simple model that uses water transfer and tritium/hydrogen ratio as mass transfer parameters and does not consider physical phenomena such as tritium incorporation in soil particles. When tritiated water is present in the soil, plants will incorporate tritium with absorption of water. Most of the tritium transferred to plants exists in a form referred to as tissue free water tritium (TFWT), which is not bounded to tissues. Some exists as organically bound tritium (OBT) which is bounded to plant tissues by photosynthesis. Since TFWT is not bound to tissues in plants, it is easily excreted outside the plant. On the other hand, OBT has a much longer residence time than TFWT and can be directly ingested by the human body as an organic substance. Therefore, it is considered that the biological effects are large, and it is important to evaluate the amount of OBT in plants. Although analytical data on tritium incorporated into the plants surrounding nuclear facilities have been collected, it is still not sufficient to develop highly accurate mass transfer model.

In this study, the behavior of tritium in peat and vermiculite, which are soils widely used for planting, was investigated. Then, Komatsuna and tomato were grown in the soil containing tritium and investigated the amount of tritium transferred from the soil and its existence form. Furthermore, the release behavior of tritium from tritium-contaminated soil to the gas phase was investigated.

**Chapter 1** elaborates the background and objectives of the study. By revisiting its natural inventory, current use and future planned activities especially in fusion technology, tritium and tritiated waste was discussed. Further, literature review on tritium cycle in the environment was discussed. Additionally, the tritium forms of interest to the radiological interest were highlighted with emphasis on TFWT and OBT. Also, environmental models for explaining and predicting tritium dynamics in planned and accidental exposure scenarios were discussed.

**Chapter 2** indicates characterization of peat and vermiculite for tritium behavior. Their physical and chemical forms were discussed with analysis for water content. Further, tritium behavior in peat and vermiculite was done by performing immersion in tritiated water, tritium release and tritium percolation experiments. From a simple intrusive immersion, isotope exchange capacities were obtained to be $4.95 \times 10^{-2}\,\mathrm{mol}\text{-}\mathrm{T}_2\mathrm{O}/\mathrm{g}$ in peat and $3.38 \times 10^{-2}\,\mathrm{mol}\text{-}\mathrm{T}_2\mathrm{O}/\mathrm{g}$ in vermiculite. Tritium release behavior on immersed soil samples was observed by heating to $1000^{\circ}\mathrm{C}$. Prior Ar purge released significant amounts of HTO. Tritiated methane release was observed around $500^{\circ}\mathrm{C}$ which indicated the occurrence of non-exchangeable OBT formed in the soil. Finally, tritium percolation experiments considering Darcy flow under gravity was considered. The fluxes and hydraulic conductivity were used in evaluating the sorption capacity and to confirm the porosity.

**Chapter 3** explained the experimental set-up, tritium exposure methods and fraction analysis in Komatsuna. Six plants cultivated in pot were placed in an airtight glove box installed in an incubator. Tritiated water was supplied directly to the soil in each pot. TFWT and OBT in Komatsuna were investigated by four methods: immersion in tritium free water, vacuum drying, air exposure, and combustion. There was no significant difference in tritium release behavior between stems and leaves during water immersion, and retention amounts were similar. The amount of TFWT in Komatsuna depended on the tritium concentration in the soil, and that tritium concentration in the stems and leaves decreased as the tritium concentration in the soil decreased. The amounts of tritium released from the roots were much less than that from the stems and leaves.

**Chapter 4** described tritium uptake in tomato after being exposed to soil contaminated with $0.12\,\mathrm{MBq}/\mathrm{cm}^3$ tritiated water. A fully matured tomato plant was used for tritium exposure and analysis. High concentration tritiated water was poured once on the soil with sampling of fruits, leaves and stem done from day 2 to day 14. TFWT and OBT present in leaves, stems, fruits, and roots of Tomato were evaluated by drying and combustion. TFWT in leaves decreased with cultivation time, while TFWT in fruits tended to increase. OBT in leaves and fruit tended to decrease with cultivation time. Tritium in roots was higher than in other parts.

**Chapter 5** discusses tritium transfer from soil to the gas phase during plant cultivation and post-cultivation. The former was evaluated from tritium concentration loss monitored in soil as well as concentration measured from water filled bubblers. For post-cultivation, a separate experiment was conducted by placing sample soil in a hermetically sealed tube and subjecting it varying treatments using Ar and $\mathrm{Ar}/\mathrm{H}_2\mathrm{O}$. The behavior of tritium in the soil during tomato cultivation experiments were analyzed and the mass transfer from the soil to the gas phase was discussed.

**Chapter 6** gives a summary, conclusions and the future work.

---

## Chapter 1: Introduction

### 1.1 Tritium Production and Inventory

Tritium (T) is radioactive and the heaviest hydrogen isotope with a physical half-life of 12.32 years. It decays to helium-3 by beta ray emission with an associated release of 18.6 keV as its maximum energy. Naturally, tritium is produced by cosmic interactions with gaseous components in the upper atmosphere.

$$
\begin{aligned}
^{14}\mathrm{N} + \mathrm{n} &\rightarrow \mathrm{T} + ^{12}\mathrm{C} \\
^{16}\mathrm{O} + \mathrm{n} &\rightarrow \mathrm{T} + ^{14}\mathrm{N}
\end{aligned} \tag{1.1}
$$

Artificially, tritium is produced when fast neutrons bombards targets such as boron or lithium. In nuclear fission reactors, neutron irradiation of rods in the reactor core converts uranium to tritium in ternary fission processes. Also, boron absorbers used in controlling chain reactions produce tritium by-products after absorbing neutrons and this process is known to be the prominent route of tritium production. The global steady state inventory of tritium (3 kg) [1] is lower than man-made sources and therefore presents low risks. However, as well as tritium released from past nuclear weapons tests, large tritium amount required in proposed fusion reactors such as the approximately $18\,\mathrm{kg}$ [2,3] in the International Thermonuclear Experimental Reactor (ITER) is likely to reach or exceed natural levels hence pose radiological challenges. Sources of tritium include commercial nuclear reactors and research reactors, and their reprocessing plants and government weapons production plants. Tritium may be released as steam from these facilities or may leak into the underlying soil and ground water.

### 1.2 Tritium from Fusion Reactors

Fusion reaction involves the combination of two lighter nuclei to produce a heavy nuclide with a release of approximately 17.6 MeV energy. In the proposed fusion reactor, tritium and deuterium are the main fuel sources and which require extremely high temperatures to force their collision. Below are the fusion equations and their resultant energy.

$$
\begin{aligned}
\mathrm{D} + \mathrm{T} &\rightarrow {}^{4}\mathrm{He} + \mathrm{n} + 17.6\,\mathrm{MeV} \\
\mathrm{D} + \mathrm{D} &\rightarrow {}^{3}\mathrm{He} + \mathrm{n} + 3.27\,\mathrm{MeV} \\
\mathrm{D} + \mathrm{D} &\rightarrow \mathrm{T} + \mathrm{P} + 4.03\,\mathrm{MeV} \\
\mathrm{D} + {}^{3}\mathrm{He} &\rightarrow {}^{4}\mathrm{He} + \mathrm{P} + 18.3\,\mathrm{MeV}
\end{aligned} \tag{1.6}
$$

The D-T reaction has a larger cross section and requires less energy for the reaction than eqn. 1.4-1.6. The D-D reaction has the slowest reaction rate and requires elevated temperatures $>10^{9}\,^{\circ}\mathrm{C}$ to induce a collision making it quite challenging.

### 1.3 Tritium Usage

Apart from the proposed use of tritium to produce energy in fusion reactors, it has several uses across different industries as highlighted below.

- Used as radio luminescent light source for watches and jewelry.
- As a tracer for biological, pharmaceutical and environmental studies.
- As a component in nuclear weapons to boost the efficiency and yield in fission bombs.
- Due to its association with water molecule, it is used as radioactive tracer in medical and scientific settings.
- To create glow-in-the-dark lighting such as exit signs, emergency lighting in buildings, and airport runway lights.

### 1.4 Tritium and Tritiated Waste—Current Evidence and Predictions

Tritium contamination may be through routine releases by nuclear power facilities which are strictly regulated or through nuclear related accidents. During reactor operations, some components are exposed to tritium which require non-destructive detritiation in case of reuse. Incineration has been proposed as the best detritiation technique for soft housekeeping components such as gloves, aprons and clothes [4,5]. The Fukushima Daiichi accident presents a modern-day evidence of tritium waste and the need to strengthen evidence for effective public engagement. The Advanced Liquid Processing System (ALPS) treated water still contains tritium which is highly diluted with seawater to about 1/7 below standard limits [6] before release. However, public perception remains negative even with technical assurances from the highest levels. With global concerns for energy and climate coupled with rising energy insecurity and climate change, the need for nuclear power is predicted to grow [7] with nuclear fusion seen as safer alternative.

### 1.5 Tritium in the Environment

#### 1.5.1 Environmental Cycle

Tritium is very mobile in environmental compartments. It behaves similarly as hydrogen and can be found in water pools as tritiated water (HTO) or in the atmosphere as gaseous HTO or tritiated gases (HT and $\mathrm{CH}_3\mathrm{T}$). By this association, tritium is involved in the water cycle, transferring between biotic and abiotic components. As shown in figure 1.1, about $30\%$ tritium in soil is absorbed and taken up by plants roots though root hair to various parts of the plant. Through transpiration and evaporation, some of the tritium is released and re-emitted into the atmosphere. Through photosynthesis, plants use tritiated water, carbon dioxide and light to produce tritiated photosynthates which are distributed to the fruits, leaves and stems. Tritium deposition from the atmosphere is either by dry or wet deposition depending on precipitation patterns.

For dry deposition, plant specialty cells such as the epidermis directly traps gaseous tritium or deposited on soil surfaces. In wet deposition, water molecules in rain, fog or snow traps suspended tritiated gases and gets deposited on plant and soil surfaces. Once on the soil surface, tritium infiltrates into subsurface water pools which are either absorbed by plant roots/microorganism or transported to ocean reservoirs through run-off [8,9].

*[Figure 1.1]* Illustration of tritium cycle in the environment.

### 1.6 Tritium Fractions in Biological Organisms

Biological organisms take up tritium through different routes. Plants do this through root uptake, photosynthesis or direct diffusion through cuticular exchanges. For other organisms, it may be through ingestion, inhalation or absorption through the skin. Once in the tissues, tritium either joins the water pool as Tissue Free Water Tritium (TFWT) or labels organic components primarily through photosynthesis to form Organically Bound Tritium (OBT) [10,11]. TFWT is the dominant fraction in most plant studies [12,13,14,15] due to the large water composition of its fresh biomass. However, the concentration tends to decrease over time as metabolic processes induce its loss either by transpiration, growth dilution or other biological processes.

Depending on the type of plant and the stage of development, it ranges from $85\%$ in fruits to less than $10\%$ in seeds. OBT is further classified based on its association with certain elements and its ease of removal. Exchangeable-OBT (E-OBT) refers to tritium bound to sulphur, oxygen or other non-carbon atoms which could be easily removed by isotopic exchange techniques. Non-exchangeable OBT (NE-OBT) is tritium bound to carbon held in strong covalent bonds which can be liberated by combustion or degradation of the carrier molecule.

Further, a different form of NE-OBT, the so-called Buried Tritium (BT) was proposed [16] after denaturing experiments were conducted on hydroponically grown maize and barley exposed to tritiated water vapor. This tritium fraction has tritium incorporated into large biomolecular such as proteins, nucleic acids and lipids, not bound to carbon and do not participate in isotopic exchange process. They could be removed by enzymatic opening or degradation hence behaving similarly as NE-OBT. Buried tritium was confirmed in OBT analysis of water milfoils and apples sampled from areas near nuclear powerplants [17].

Also, E-OBT tends to be in equilibrium with TFWT and difficult to accurately quantify. Due to its behavior, TFWT tends to be easily removed and is not considered significant in dose estimation.

*[Figure 1.2]* Illustration of tritium fractions.

#### 1.6.1 Tritium in Plants

Extensive tritium exposure experiments had been conducted in plants in field or confined environments using tritiated water vapor [8,18]. In cases of national or experimental restrictions, heavy water (HDO) had been used as substitutes [19,20,21]. Due to the low solubility of HT, tritium uptake in plants is either by root uptake of liquid HTO or atmospheric foliar uptake of gaseous HTO. Tritiated hydrogen (HT) is only made accessible after oxidation to HTO by soil microorganisms [22]. To compare tritium uptake during day and night, experiments on wheat indicated a lower tritium uptake in leaves undergoing senescence and a lower TFWT uptake in wheat leaves, wheat ears and stem during the night due to stomatal closure [23]. Boyer et al [24] determined the tritium incorporation rate in lettuce under long term exposure in natural conditions and at equilibrium to be between 0.13 and $0.16\%\,\mathrm{h}^{-1}$. Experiments in tomato confirmed the role of light during photosynthesis in OBT formation [25]. Matano et al conducted tritium exposure under fusion conditions to Arabidopsis and calculated up to $9.5\%$ NE-OBT presence which is markedly higher than the reported $<1\%$. This indicates higher tritium concentrations as proposed in fusion related exposures may significantly amplify the NE-OBT fraction in plant compartments.

The concept of Translocation Index (TLI) was introduced for robust intercomparison under different experimental conditions [23]. This is defined as the percentage of the OBT concentration in plant tissue at harvest ($\mathrm{Bq}\,\mathrm{cm}^{-1}$ water of combustion) related to the TFWT concentration in leaves ($\mathrm{Bq}\,\mathrm{cm}^{-1}$) at the end of exposure to HTO. Below is a summarized table of various tritium exposure in plants and exposure routes.

**Table 1.1** Sample plant tritium exposure experiments.

| Plant | Experiment | Exposure route |
|:------|:-----------|:---------------|
| Tomato | S.B. Kim 2010, 2011 | HTO vapor/Field |
| Tangerine | Ichimasa et al., 2005 | D₂O vapor/Field |
| Lettuce | Boyer et al., 2009 | HTO vapor near Nuclear Power Plant |
| Cabbage | Choi et al., 2005 | HTO vapor/Glovebox |
| Arabidopsis | Matano et al, 2021 | HTO vapor/Glovebox |
| Radish | Atarashi-Andoh et al, 2002 [26] | HT and HTO vapor/Field and Glovebox |
| Rice | Atarashi-Andoh et al, 2001; Ichimasa et al, 2001 | D₂O vapor/Greenhouse |
| Wheat | Diabate and Strack, 1997 | HTO vapor/Greenhouse |
| Komatsuna | Portuphy et al, 2024 | HTO liq./Glovebox |
| Soybean | M. Ichimasa et al, 2002; IAEA, 2008 [27] | D₂O/Greenhouse; HTO vapor/Glovebox |

#### 1.6.2 Behavior of Tritium in Soil

Soil is one important route for tritium cycling in the environment. After deposition on surface layers, tritium could remain in soil layers and be absorbed by plants roots. It could also be evaporated into the atmosphere or be percolated into deeper layers. HT penetrates to shallow depths of approximately $2.5\,\mathrm{cm}$ due to faster oxidation to HTO induced by soil microorganisms [28]. HTO in turn has been identified to stay in up to $25\,\mathrm{cm}$ of the topsoil in cultivated and uncultivated soils [29,30]. These values hold for moist soils, however HTO is found to persist further for dry sandy soils. Tritium behavior in soil has been studied through retention, percolation, and transport experiments.

Modelling experiments from aquifers to land surfaces compared different soil HTO transport scenarios but was inconclusive on tritium concentration profiles near soil surface layers [31]. For short term monitoring, HTO and Organically Bound Tritium (OBT) profile concentrations showed no significant differences but, for a five-year monitoring period, OBT tends to migrate to deeper soil. Most HTO in the soil is reemitted into the atmosphere at a rate of approximately $1\%$ under steady state. An important parameter here is the isotope exchange capacity (IEC), which refers to the ability of soil to exchange hydrogen with tritium in its surroundings.

### 1.7 Analyzing Tritium Fractions in Plants and Soil

It is important to accurately quantify OBT to help guide routine operations and predict exposures in accidental situations. It is important to note that the total tritium is the sum of TFWT and OBT. Based on this simple relation, quantification can be broadly separated into two compartments—the TFWT and OBT fraction. Figure 1.3 is a simplified approach to separation and quantification of tritium fractions.

*[Figure 1.3]* Scheme for TFWT and OBT Extraction and Analysis.

Freeze drying or lyophilization is done to remove TFWT [23, 33]. This process involves freezing samples and eventually dehydrating it at low temperatures and pressure to remove water by sublimation. For high tritium contamination, rinsing surface with tritium-free water is done before freeze drying [14,15]. The resultant loss in weight confirms the TFWT removal.

Isotopic exchange techniques are used for E-OBT removal which is enabled by immersion in tritium-free water for a period. This intrusive method sometimes leads to coloration due to discharge of sample pigments that needs to be separated before counting. Non-intrusive techniques include exposure to tritium-free air to enable isotopic exchange with free hydrogens in its component water vapor. For low tritium contaminations, the intrusive method is desirable where immersion is done for a long time to enhance the isotope exchange reaction [33].

NE-OBT is extracted by completely combusting the sample to break the C–T and C–H bonds to liberate the tritium which is trapped in tritium free water filled bubbles [34,35]. The combustion water is either analyzed directly or pre-concentrated to enhance tritium counting. Methods for combustion have evolved over time with three key techniques used (Figure 1.4). They include,

- The use of quartz tube which could be adapted in size to take up to a $100\,\mathrm{g}$ of sample and produce up to $50\,\mathrm{cm}^3$ combustion water. However, this process is manual and required monitoring.
- The use of commercially available Parr bomb which takes limited amounts and produce up to $5\,\mathrm{ml}$ combustion water. This apparatus has the advantage of combusting within a short time hence a lot of samples could be analyzed.
- The use of an automatic pyrolizer which could produce about $10\,\mathrm{ml}$ combustion water.

*[Figure 1.4]* Combustion techniques a) quartz tube combustion b) Parr bomb technique c) pyrolizer technique [41].

Attempts have been made to standardize OBT measurements by the following items.

- Harmonizing the tritium fraction extraction method.
- Providing a standard reference material.
- Developing robust models for predicting doses in planned and accidental scenarios.

The French developed the XP M 60-824 (2016) standard for tritium measurements in the environment which has been adapted and modified by other countries including Canada and Belgium. Over the past 3 decades, various meetings had been held to harmonize and improve OBT analysis through intercomparison exercises with different laboratories [36-41].

### 1.8 Modelling OBT Behavior

Various models have been advanced to explain past data as well as predict doses due to tritium under different scenarios. OBT modelling is largely compartmentalized into three namely: air, soil and water, and which could be sub-classified based on the model parameters. Depending on the extent of exposure, a specific activity or dynamic model is used in respect of either a chronic or an acute situation [8,41]. This is interdisciplinary in nature with data needed across spectrums of meteorology, food science, botany, etc. Below is a table summarizing some models.

**Table 1.2** Summary of Tritium Transfer Models for Different Routes.

| Model Name | Type | Description |
|:-----------|:-----|:------------|
| **Aquatic Transfer Models** |||
| AQUATRIT, Romania | Dynamic | Assumes that both water temperature and HTO concentration to be spatially constant. Growth patterns are assumed for mature animals. |
| Safety Reassurance Academy (SRA), Kyoto University, Japan | Dynamic | 2-compartment model that uses transfer coefficients, accounting for the difference in specific activity between the environment and the body of the aquatic organism. |
| EDF, France | Dynamic | Evaluates tritium concentrations in the aquatic and terrestrial environment resulting from liquid discharges. |
| BIOCHEM, Germany | Steady state | Accounts for the differences in exchangeability between E-OBT and NE-OBT that occur in living systems. |
| National Institute of Radiological Sciences (NIRS) Model, Japan | Dynamic | Based on the Environmental Radionuclide Movement Assessment ERMA system developed by NIRS. Assumes HTO concentration. |

### 1.9 Biological Effects

Beta ($\beta$) rays emitted by tritium has a short range and can be stopped by dead skin cells. This implies tritium is generally safe outside the human body unless it is internally exposed to cells via ingestion or inhalation. Due to its association with water molecules, it is easily distributed within the human body and could lead to tritium exposure. The HTO biological half-life of approximately 8.5 days is enough contact time to induce a biological effect. Further, OBT is persistent for over 40 days in biological systems and thus of greater concern. It is believed doses to humans and biota have been underestimated due to the difficulty of accurately determining OBT concentrations. Though no direct effect has been studied in human, study on other non-human biota had been conducted on bivalves, rodents and fish [42].

### 1.10 OBT and its Relevance in Dose Estimation

After labelling molecules, OBT tends to be translocated to other parts of the organism hence of radiological significance. Due to equilibrium exchanges between TFWT and E-OBT fractions, the NE-OBT fraction is of greater concern. For tritium dose estimation, models describing OBT contribution to the tritium activity must be considered. For radionuclide dose estimation, two basic models—the No Dilution Model and Specific Activity model are generally used but with varying adaptations [43]. No dilution model considers exposure to members of the public at the point of discharge whiles in specific activity models, radionuclides are cycles through the environment and eventually enters biota through its association with water—hence some form of dilution. Since OBT has a biological half-life three (3) to six (6) times greater than HTO, it is important to consider its transfer parameters [44] in various components such as milk and meat. For OBT ingestion, it is recommended to multiply the dose factor for HTO by a factor of between 1.8 (three-month-old infant), 2.5 (adult) and 2.8 (10-year-old child) [45].

### 1.11 Decontamination of Spent Soil

Tritium removal from contaminated media has been a subject of interest to regulators and radioecologists. Advances has been made for tritium removal from air streams and to a limited extent of tritiated water. Examples of such technologies are highlighted below:

- Use of Zirconium alloy getters for non-oxidative extraction of HT.
- Use of molecular sieves for HTO removal.
- Water distillation to remove tritium from D₂O in Heavy water reactors at low throughput.
- Cryogenic distillation coupled with Vapor phase catalytic exchange (VPCE), Liquid phase catalytic exchange (LPCE) or combined electrolysis and catalyst exchange (CECE) [46].

Tritium removal of soil must consider the tritium form, the type of soil, and the distribution and migration of the source. Due to its relatively short half-life, it can be contained in dedicated depositories and allowed to decay to low levels. However, for regulatory and safety purposes, it is desirable to reduce the concentration prior to disposal or storage.

Jackson et al [47] used a thermal removal technique on contaminated concrete and soil obtained from heavy-water moderator operations at the Savannah River Site. Thermal detritiation was done by heating the contaminated samples in enclosed concrete wall fabrication of about 8.5 m × 7.3 m (Figure 1.5). Following the treatment, tritium concentrations had been reduced significantly from $9287\,\mathrm{Bq}/\mathrm{g}$ to $0.044\,\mathrm{Bq}/\mathrm{g}$ in soil and from $62160\,\mathrm{Bq}/\mathrm{g}$ to $2516\,\mathrm{Bq}/\mathrm{g}$. This demonstrated that tritium can be effectively removed from concrete rubble and soil using thermal heating.

*[Figure 1.5]* Soil and Concrete treatment enclosure proposed by Jackson et al [47].

### 1.12 Research Objectives

The tritium transfer route from soil to plant needs more data to build robust models. However, the difficulty with conducting open field tritium experiments means a lot more lab-scale exposure experiments with its associated limitations needs to be done. This study aims to further bridge this gap by proving more data and which may be essential for radioecological models.

- **Planting Material and Soil Characterization (Chapter 2):** This aims to understand the properties of peat soil and vermiculite and their impact on tritium retention and release under different conditions. Isotopic exchange is one prominent phenomenon in tritium behavior analysis, and which is dependent on tritium residence and moisture contents in the environment. This chapter therefore seeks to establish the soil parameters of interest to evaluating the Isotopic exchange Capacity of peat soil and vermiculite.

- **Tritium exposure in Komatsuna (Chapter 3):** This chapter aims to understand the dominant tritium form in this plant through the soil exposure route. As a largely herbaceous species which is eaten at different growth stages, establishing this fact is beneficial for modelers.

- **Tritium exposure in Tomato (Chapter 4):** This chapter is to evaluate the tritium distribution in the plant tissues after soil exposure. The main objective is to establish the translocation factor as an environmental determinant of OBT persistence. Additionally, the soil tritium evacuation rate under canopy and non-canopy conditions will be established.

- **Tritium removal from spent soil (Chapter 5):** This chapter aims to explore tritium remediation method on a contaminated cultivated soil though a combination of drying, heating and isotopic exchange to evaluate tritium transfer to the gas phase. The method that gives a high gas phase tritium concentration relative to the initial soil concentration could be optimized in future.

### References (Chapter 1)

[1] P-E Oms et al., Sci Total Environ., 656 (2019), 1289-1303.
[2] M. Glugla et al., Fusion Eng. Des., 82 (2017), 472-48.
[3] R.J. Pearson et al., Fusion Eng. and Design, 136 (2018), 1140-1148.
[4] J. Pamela et al., Fusion Eng. and Design, 93 (2015), 51-56.
[5] X. Lefebvre and K. Liger, Fusion Eng. Des., 87 (2012), 104.
[6] IAEA Report, 2024.
[7] IAEA Report 2022.
[8] Boyer et al, Environmental and Experimental Botany, 67 (2009), 34-51.
[9] Murphy, C.E., Health Phys, (1993) 65, 683-697.
[10] S. Diabaté, and S. Strack, Health Phys., 65 (1993), 6, 698-712.
[11] IAEA 2007.
[12] M. Atarashi-Andoh et al., Fusion Sci. Technol., 48 (2005).
[13] Y. Choi et al, J. Env. Rad., 84 (2005), 79-94.
[14] Matano et al., Fusion Engineering and Design 173 (2021), 112787.
[15] Portuphy et al., Fus. Sci. Tech., 80 (2024), 276-284.
[16] F. Baumgartner and W. Donhaerl, Anal. Bioanal. Chem., 379 (2004), 204-209.
[17] A-L Nivesse et al., Chemosphere, 269 (2020), 128676.
[18] Galeriu et al, J. Env. Rad., 118 (2013), 40-56.
[19] M. Ichimasa et al., Fusion Sci. Technol. 41 (2002), 393-398.
[20] Y. Ichimasa et al., Fusion Sci. Technol. 48 (2005), 775-778.
[21] M. Atarashi-Andoh et al., Health Phys. 82 (2002), 863-868.
[22] N. Momoshima et al, J. Nucl. Sci. Tech., (1992), 29(10), 1011-1017.
[23] S. Diabate and S. Strack, J. Environ. Radioact. 36 (1997), 157-175.
[24] C. Boyer et al., Radioprotection, 44 (2009), 671-676.
[25] Kim, S.B., 2011.
[26] M. Atarashi-Andoh et al., Fusion Sci. Technol., 41 (2002), 427-431.
[27] IAEA, 2008. Soybean Scenario.
[28] C. W. Sweet and C.E. Murphy, Environ. Sci. Technol, 15 (1981), 12, 1485-1487.
[29] J. Liang et al., J. Environ. Radioact. 106957 (2022), 251-252.
[30] F. Guo et al., Applied Radiation and Isotopes 164 (2020) 109311.
[31] Y. Belot et al, J. Env. Rad., 84 (2005), 259-270.
[32] M. J. Wood et al., Health Phys., 65 (1993), 610-627.
[33] A-L Nivesse et al., Talanta, 224 (2021) 121803.
[34] F. Pointurier et al., Appl. Radiat. Isotopes 61 (2004), 293-298.
[35] J. Vagner et al, Applied Radiation and Isotopes 118 (2016) 136-139.
[36] S. Hisamatsu et al., Radioisotopes, 39 (1990), 457.
[37] W.J.G. Workman et al., Fusion Technology, 48 (2005), 1, 763-766.
[38] S. B. Kim and J. Roche, Journal of Environmental Radioactivity, 122 (2013), 79-85.
[39] N. Baglan et al., Radioprotection, 48 (2013), 1, 127-144.
[40] N. Baglan et al., Journal of Environmental Radioactivity 18 (2018), 52-61.
[41] Proceedings of the 9th OBT workshop, May 10th-12th 2023, Belgium.
[42] M.F. Ferreira et al., Science of the Total Environment 876 (2023) 162816.
[43] IAEA 2001, Generic models.
[44] AECL, 1994. Tritium Transfer Parameters for Routine Release of OBT.
[45] ICRP, 1996.
[46] IAEA, 2004, TRS 421, Management of waste containing tritium and carbon14.
[47] Jackson et al, 2013.

---

## Chapter 2: Planting Materials and Soil Characterization

### 2.1 Choice of Plant and Growing Conditions

In this experiment, two widely eaten vegetables in Japan were selected as suitable bioindicators for tritium uptake. Komatsuna (Brassica Rapa var. perviridis) is a green leafy plant that is easily grown and can be eaten at all stages of growth. Cherry tomato (Solanum lycopersicum var. cerasiforme) is a small-type regular tomato easily grown all seasons except winter. Komatsuna seeds were initially nursed for 5 days in water-soaked Jiffy-7 peat pellets. After sprouting to about $5\,\mathrm{cm}$, they were transferred to a $70\,\mathrm{cm}^3$ pot half-filled with peat-vermiculite soil. A light source was installed at the upper part of the growth set-up and automatically programmed to provide photo and dark periods necessary for growth. The room temperature was maintained between $25^{\circ}\mathrm{C} - 28^{\circ}\mathrm{C}$ with humidity range between $60\% - 80\%$ monitored using a hygrometer. $500\,\mathrm{cm}^3$ non-tritiated water was supplied once a day to the plants with soil moisture maintained and monitored using soil moisture meter. To ensure optimal growth, Hyponex liquid vegetable fertilizer containing 6:10:5 N:P:K was diluted to about 1ml:1000ml water and 100ml supplied once every 3 days.

For tomato, seeds were obtained from the Tomato Mutants Archive (TOMATOMA) project [1]. This variety was selected for the following reasons:

- short growing time of up to 90 days,
- short height makes it suitable for glovebox experiments,
- produces a lot of small fruits, and
- the ongoing phenotypic and genotypic experiments on this variety opens a future prospect in determining radiation-dependent exposures.

The seeds were initially soaked in distilled water prior to 3-day nursing in a process like that described above for Komatsuna. The installed lighting system was set for 16 hours and 8 hours photo and dark period respectively. Bottom watering was done in 3-day interval except for situations of dryness. After fully maturing, the plants were transferred to the Kyushu University, radioisotope center for tritium exposure experiments.

*[Figure 2.1]* a) Fully Matured Komatsuna, b) Fully Matured Microtom.

### 2.2 Peat and Vermiculite Soils

Peat soil is widely used in commercial and household farming and has been known to cover about $4.23 \times 10^6\,\mathrm{km}^2$ of the earth's surface [2] representing about $8\%$ of earth's surface with high geographical distribution in Canada, Russia, Finland and in the northern part of Japan [3]. It is made of dead and decomposed organic materials thereby serving as a rich source of nutrients for plants. It is known to generally have high moisture content ($90\% - 120\%$), high pH (7-8) and low density (0.02-0.98 g/cm³) [4] which varies depending on the stage of decomposition. Peat soil samples used were commercially produced by the Oishi Bussan company limited, Japan.

Vermiculite is an inorganic monoclinic clay material with a silicate base usually added to peat soil as water holding medium. Chemically, it has a sheath of water around it $(\mathrm{Mg}, \mathrm{Fe}^{2+}, \mathrm{Fe}^{3+})_3[(\mathrm{Al},\mathrm{Si})_4\mathrm{O}_{10}](\mathrm{OH})_2 \cdot 4\mathrm{H}_2\mathrm{O}$ enabling further water absorption or release. Due to its medium shrink-swell capacity, vermiculite tends to absorb and swell in a moist environment and shrink in dry situations but under limited conditions. Exfoliated vermiculite was used in this study was produced by the Engeishizai Gurinkitakyu Company Limited.

### 2.3 Properties of Peat and Vermiculite

#### 2.3.1 Moisture

Soil water is loosely held by soil interlayers as capillary moisture or strongly adhered in thin films or pores as hygroscopic moisture. Soil moisture content was determined gravimetrically $(\theta_g)$ using the natural convection oven drying method [5,6]. Moist soil samples $(\mathrm{S}_m)$ were initially weighed with a can $(\mathrm{M}_c)$ and then heated steadily to $105^{\circ}\mathrm{C} \pm 5^{\circ}\mathrm{C}$ using the Isuzu Kosumosu VTN-115 model for 48 hours to evaporate the water molecules. Finally, the dry soil $(\mathrm{S}_d)$ was reweighed, and the moisture content calculated from the ratio of the mass of water to the mass of dry soil as shown in equation 2.1,

$$
\theta_g = \frac{S_m - S_d}{S_d - M_c} \tag{2.1}
$$

The calculated moisture content was $114\%$ and $0.5\%$ respectively for peat and vermiculite. The oven drying method is known to effectively remove physically and chemically adsorbed water molecules but unable to remove structurally adsorbed water in clay layers. An alternative method using the microwave technique with the Shimadzu MOC63u resulted in a $19\%$ moisture content value. This low value was because of the rapid drying which causes uneven drying across the sample.

*[Figure 2.3]* Graph of Capillary and Hygroscopic Moisture in Peat and Vermiculite.

As described by Nishikawa et al [7] Physically adsorbed water is related to the capillary moisture and is easily removed at low temperatures without heating. Chemically adsorbed water is hygroscopically bound to molecules and could be removed only by heating. Structurally adsorbed water exists deep in inner layers and cannot be removed by heating. An intrusive isotopic exchange method readily accesses this "buried" water.

*[Figure 2.4]* Illustration of Forms of Adsorbed Water.

#### 2.3.2 Organic Content

Total organic contents are determined by thermal oxidation of soil samples and is considered the most effective as compared to other techniques such as chemical treatment [8]. Organic content of peat soil and vermiculite was analyzed by combustion using $20\%$ $\mathrm{O}_2/\mathrm{Ar}$ over a temperature range of $100^{\circ}\mathrm{C} - 600^{\circ}\mathrm{C}$ for 1.5 h. Prior to this, moisture was removed by oven convection method. By determining the weight before and after ashing, the percentage loss is calculated as the total organic content. As expected, peat soil showed a high organic content of $85\%$ as compared to the non-detection of same in vermiculite.

#### 2.3.4 Soil Gradation

This classifies coarse soils based on their particle size. For mechanical purposes, determining the particle size distribution gives a good indication about ground water parameters such as hydraulic conductivity and compressibility. Gradation is classified based on the Unified soil classification system [9] as "poorly graded" if there is non-uniform distribution on a predetermined mesh size. It is well graded when a sieving experiment indicates a uniform distribution.

The sieving method using the AS ONE MVS-1 mini sieve shaker equipped with sieves of different mesh sizes. Sieving experiment was done for only vermiculite due to its coarse nature as compared to the fibrous peat. Vermiculite sample is poured on top of the minishaker and shaken through a series of decreasing mesh apertures as shown in fig 2.5 to sort grains based on sizes. The amount of soil size retained on each mesh is weighed and the fraction to the initial weight calculated after which grain size distribution was plotted as shown in fig 2.5. The distribution shows a poorly graded gravel-type soil due to non-uniform distribution across all mesh sizes. It was expected that vermiculite will have a faster drainage capacity and less compressible hence an impact on its hydraulic conductivity.

*[Figure 2.5]* a) Gradation Set-up b) Vermiculite Grain Size Distribution.

#### 2.3.5 Specific Surface Area Analysis

This is a property of the soil and refers to the aggregated surface area of all particles in the soil usually measured in $\mathrm{m}^2/\mathrm{g}$. The Brunauer-Emmett-Teller (BET) surface area analysis theory [10] postulates that the gas molecules form a monolayer on the surface. Once the first layer is formed, subsequent adsorption layers can form on top of it. The following BET equation was used.

**Table 2.1** A Summary of the Physical Characterization of Peat and Vermiculite.

| Sample | Peat | Verm |
|:-------|:-----|:-----|
| BET surface area [m²/g] | 1.37 | 5.57 |
| Pore volume [cm³/g] | $4.81 \times 10^{-3}$ | $1.933 \times 10^{-2}$ |
| Pore size [Å] | 141 | 132 |
| Density [g/cm³] | 0.4 | 0.12 |
| Moisture content [%] (gravimetric) | 114 | 0.7 |
| Organic content [%] | 85.1 | - |

*[Figure 2.6]* BET Surface Area Isotherm Plots for Peat and Vermiculite.

### 2.6 Tritium Exposure in Soil

To estimate tritium behavior in contaminated soil, immersion, tritium release and percolation experiments were performed to evaluate tritium existence forms, isotopic exchange capacities and spatial variations. Tritium quantification was done on liquid treatment aliquots using liquid scintillation counting (LSC).

Liquid scintillation counting is a radioanalytical technique used to measure the radioactivity of liquid samples containing primarily beta as well as some alpha particles. It involves mixing samples with adequate volumes of a liquid scintillator which role is to absorb beta particle energy and convert to light. Recently, the scintillators are in the form of cocktail pre-mixed with solvents and surfactants.

Sample aliquots are placed in transparent or translucent vials prior to scintillator addition before a suitable counting time is selected. In the counting process, beta particles are emitted from the source sample to the solvent which also transfers to the scintillator and emits photons. The emissions are detected by photomultiplier tubes in the LSC. In this research the low-background Aloka AccuFLEX 7200 counter with a measurement efficiency of $>60\%$ was used. Its detection limit is 0.01 Bq. The external standard method for calibration was done using standard reference material 4947C from the National Institute of Standards and Technology. Also, quench correction was done using an external standard channel ratio technique with an unquenched standard from the Japan Radioisotope Association. PerkinElmer® superpolyethylene 20-mL vials were filled with a 1-mL water sample mixed with an 8-mL PerkinElmer® EMULSIFIER-SAFE™ scintillation cocktail. Because of the high tritium concentration used in this experiment, direct counting was performed on water sample fractions with no pretreatment at a counting rate of 3 min/sample.

#### 2.6.1 Immersion Experiment

Immersion experiments aim to study isotopic exchange phenomenon after a period of contact between samples and tritiated solutions. This could be intrusively where liquid tritiated water (HTO) is allowed to permeate samples directly to enhance the exchange between tritium in HTO and exchangeable hydrogens in soil. Alternatively, a non-intrusive method involves subjecting samples to a tritiated atmosphere e.g., HT or gaseous HTO.

Since this study focused on soil tritium contamination under nuclear fusion reaction conditions, the intrusive method was considered to investigate the tritium sorption behavior. The samples of peat and vermiculite were immersed in tritiated water in polyethylene vials, capped (Figure 2.7) and placed in a hood. $12\,\mathrm{cm}^3$ of $61.8\,\mathrm{kBq}/\mathrm{cm}^3$ of HTO was added to $1.5\,\mathrm{g}$ peat and $0.5\,\mathrm{g}$ vermiculite. After shaking vigorously and allowing to settle, $1\,\mathrm{cm}^3$ aliquots were sampled from each vial after 1 hour and 696 hours for liquid scintillation counting.

*[Figure 2.7]* Illustration of Isotopic Exchange During Immersion.

The immersion technique enhances isotopic exchanges between tritium in liquid tritiated water and exchangeable hydrogen atoms in soil samples. At the end of the immersion period, tritium equilibrium is established between the solid and liquid phases [12, 13].

$$
\mathrm{HTO} + \mathrm{H}_2\mathrm{O} \rightleftharpoons \mathrm{HHO} + \mathrm{HTO} \tag{2.6}
$$

$$
\left(\frac{T}{H}\right)_l = \left(\frac{T}{H}\right)_s \tag{2.7}
$$

By immersion of soil into tritiated water, a decrease in tritium concentration in the aqueous phase confirms an isotopic exchange occurred. The immersion conditions and derived isotope exchange capacity (IEC) is shown in Table 2.1. The amount of tritium lost by radioactive decay during the 29-day immersion period was evaluated to be 276 Bq. Figure 2.8 compares initial tritium concentration, after 1 h and, 696 h for Peat soil and Vermiculite. For Peat, tritium concentration decreased quickly within 1 h and then slightly decreased after 696 h. Peat has a high moisture content, indicating that it retains a large amount of adsorbed water. When the peat was immersed in tritiated water, it is considered that tritium in the water and hydrogen in the water adsorbed on the peat were exchanged quickly, and tritium concentration decreased.

**Table 2.1** Incorporated Tritium and Isotope Exchange Capacity in Peat and Vermiculite.

| Sample | Peat1 | Peat2 | Verm1 | Verm2 |
|:-------|:------|:------|:------|:------|
| Sample weight [g] | 1.64 | 1.46 | 0.628 | 0.498 |
| Water amount [cm³] | 11.9 | 12.0 | 11.2 | 12.3 |
| Immersion time [hour] | 1 | 696 | 1 | 696 |
| Tritium concentration [Bq/cm³] (0 h) | 61800 | 61800 | 61800 | 61800 |
| Tritium concentration [Bq/cm³] | 56600 | 55400 | 59900 | 60000 |
| Decay for 696 hours (Bq) | 276 | 276 | 276 | 276 |
| Incorporated T [Bq/g-soil] | 47700 | 50900 | 32300 | 40600 |
| T/H ratio in water [10⁻¹⁰] | 4.61 | 4.64 | 5.01 | 5.02 |
| IEC [mol-T₂O/g] | $4.81 \times 10^{-2}$ | $5.10 \times 10^{-2}$ | $3.00 \times 10^{-2}$ | $3.77 \times 10^{-2}$ |
| Averaged IEC [mol-T₂O/g] | $4.95 \times 10^{-2}$ | | $3.38 \times 10^{-2}$ | |

The subsequent gradual uptake of tritium may be due to isotope exchange with hydrogen in clay minerals included in the peat. The sorption rate of tritium to the vermiculite was slower than that to the peat. Since the water content in the vermiculite was small, it is considered that tritium was captured by an isotope exchange reaction with hydrogen, which is chemically bonded to the crystalline water in the phyllosilicate structure of vermiculite. As shown in Table 2.1, the average amount of incorporated tritium in the peat samples were $493\,\mathrm{kBq}/\mathrm{g}$-soil and that in the vermiculite samples were $365\,\mathrm{kBq}/\mathrm{g}$-soil.

*[Figure 2.8]* Tritium concentration in Liquid phase after 1 hr. and 696 hr.

Assuming the T/H ratio in the water and the T/H ratio in the sample have reached equilibrium after $696\,\mathrm{h}$, the isotope exchange capacity of each sample was obtained to be $4.95 \times 10^{-2}\,\mathrm{mol}\text{-}\mathrm{T}_2\mathrm{O}/\mathrm{g}$ for peat and $3.38 \times 10^{-2}\,\mathrm{mol}\text{-}\mathrm{T}_2\mathrm{O}/\mathrm{g}$ for vermiculite on average. The obtained values are compared to various materials in Fig. 2.9. The values in natural soils were calculated from tritium vapor exposure experiments to natural soil collected near a non-tritium producing facility [14].

The values in cement paste, mortar, sand [15] and Pt-MS5A [16] were obtained by exposure to tritiated water vapor rather than liquid tritiated water. It was found that the values of the isotope exchange capacity for tritium in peat and vermiculite were an order larger than "natural soil" and 2 orders larger than sand and PT-MS5A. This could be related to the ease of access to hydrogen sites in molecules during the more intrusive liquid water immersion procedure as compared to vapor immersion [12] which limits isotopic exchange.

*[Figure 2.9]* Comparison of Isotope Exchange Capacities for different media.

#### 2.6.2 Tritium Release Experiment

Tritium release behavior was investigated on the immersed peat and vermiculite to access the extent of tritium trapping, retention and release with respect to varying temperatures. The wet samples were scooped from tritiated water in the immersion vials, soaked up with tritium-free water and then placed in quartz tubes. After purging with Argon for 18 hours, they were heated to $1000^{\circ}\mathrm{C}$ in an electric furnace with continuous Argon flow. Released tritium was collected in two series of water bubblers.

Although HT and $\mathrm{CH}_3\mathrm{T}$ cannot be distinguished using the catalyst oxidation method applied in this work, it is expected that $\mathrm{CH}_3\mathrm{T}$ is released rather than HT from peat containing a large amount of organic matter. No significant amount of tritium was collected in 2nd bubbler from vermiculite, which contains almost no organic matter.

*[Figure 2.10]* Tritium Release Curve for Peat Soil.

*[Figure 2.11]* Expanded Tritium Release curve Showing a Tritiated Carbon.

A significant release peak of tritium was observed only from $75^{\circ}\mathrm{C}$ to $125^{\circ}\mathrm{C}$ as HTO. Originally, the moisture content of vermiculite was as low as $0.7\%$, but by immersion in tritiated water, it is considered that a certain amount of adsorbed water was formed. Some of them might be difficult to remove even by an Ar gas purge at room temperature for 18 hours.

*[Figure 2.12]* Tritium Release Curve for Vermiculite.

The tritium fraction observed in the 2nd bubbler around $500^{\circ}\mathrm{C}$ was suspected to be tritiated hydrocarbon because HT is released at low temperatures. The $\mathrm{CH}_3\mathrm{T}$ released indicates the presence of OBT in soil which hitherto has been attributed to photosynthetic production mechanisms. This opens an interesting issue about the role of soil microorganisms in OBT formation. From a radiation protection viewpoint, it is unlikely natural soil temperatures would rise so high to affect its release.

#### 2.6.3 Tritium Percolation in Soil

Solute transport varies for different soil media and is dependent on characteristics such as chemical composition, moisture and porosity. By monitoring percolated tritiated water at arbitrary depths, tritium mass transfer coefficient representing the isotope exchange reaction [15,16] could be evaluated. Assuming a direct deposition of tritiated water on a soil surface, there is an initial infiltration followed by solute spreading in different directions influenced by capillary action or diffusion.

Percolation experiments gives a good estimate of the flow characteristics. A fluoroscopic tube was partially filled with tritium-free sample soil of height $L$ (cm), $z_1$ and $z_2$ representing the bottom and topmost part of the soil. Tritiated water was rapidly poured at the top to an initial head height $b_0$ and the falling head $b_1, b_2 \ldots b_x$ (cm) monitored with a camera.

**Table 2.2** Soil percolation tube and packing characteristics.

| Sample | Peat | Verm | Peat-Verm (4:1 wt.%) |
|:-------|:-----|:-----|:---------------------|
| Tube column height [cm] | 20 | 20 | 20 |
| Internal diameter [mm] | 7.35 | 7.35 | 7.35 |
| Sample mass used [g] | 1.69 | 0.991 | 1.43 |
| Packing height [cm] | 7.5 | 7.7 | 10 |
| Packing density [g/cm³] | 0.530 | 0.303 | 0.336 |
| Input water [cm³] | 12 | 10.0 | 10.0 |
| Tritium concentration [Bq/cm³] | 6100 | 5810 | 5800 |

Since no tritium solutes exist in the flow path, the water potential in the sample soils is influenced by both the hydrostatic pressure and gravitational potential. For z-flow considerations using head terms, this potential is indicated as the hydraulic head $H$ (cm). Assuming an even soil particle size and porosity distribution, the HTO flux $J_w$ (cm s⁻¹) which is a property of the soil was evaluated after determining the gradient $G$ and the hydraulic conductivity $K_s$ where

$$
J_w = -G K_s \tag{2.8}
$$

The negative sign indicating the downward z-flow direction.

The gradient is evaluated from the ratio of the hydraulic head to the arbitrary soil column z as shown in equation 2.9,

$$
G = \frac{\Delta H}{\Delta z} \tag{2.9}
$$

$K_s$ measures the ease of solute flow in porous media and is also a property of the soil. It can be determined empirically by evaluating soil physical characteristics such as size distribution, texture, porosity and other physical parameters. Experimentally, the falling head [17-19] or constant head [20] methods may be used. In this study, the falling head method was used with a derivation (appendix) of the hydraulic conductivity from the Darcy law [25] which is based on the pressure differential at both ends of the soil.

$$
K_s = \frac{L}{t_1}\ln\frac{b_0 + L}{b_1 + L} \tag{2.10}
$$

*[Figure 2.13]* Set-up and Schematic for the Soil Percolation using the Falling-Head Method.

Figure 2.14 shows the falling head rate of tritiated water in the three soil samples. The faster percolation rate in vermiculite is related to its larger pore volume. Experimental flux values $J_w$ using the falling head method in the soil samples generally agrees with the numerical values using the slope of the height-time curves as shown in Table 2.3.

**Table 2.3** Experimental and Numerical Flux Values.

| Soil Sample | db/dt (falling head) | Numerical |
|:------------|:---------------------|:----------|
| Peat | -0.02063 | -0.0273 |
| Verm | -0.254 | -0.3143 |
| 4:1 P/V | -0.1282 | -0.1504 |

*[Figure 2.14]* Falling Head Rate for Peat, Vermiculite and Peat/Vermiculite Mixture.

Fig. 2.15 shows the HTO breakthrough concentrations for the soil samples. Since the output tritium concentration is less than the input concentration, it is implied that some tritium is exchanged in the soil samples. The short percolation period also observed confirms the fact that isotopic exchange reaction occurs fast. The reduction of tritium concentration in effluent water from peat was larger than that from vermiculite. This was confirmed post percolation using a distilled water purge as on vermiculite and 4:1 wt.% peat-vermiculite as shown in figure 2.16.

*[Figure 2.15]* Tritium Breakthrough Concentration.

*[Figure 2.16]* Water Purge Concentration of Vermiculite and Mixed Soil.

Since moisture content in peat is high, the isotope exchange reaction would occur quickly between supplied tritiated water and adsorbed water in peat. Immersion experiments revealed that vermiculite also has an isotope exchange capacity comparable to that in peat. However, only a small amount of tritium was captured in vermiculite in this percolation experiment. This suggests that the isotope exchange reaction rate in vermiculite was slower than that in peat because the supplied tritium undergoes the isotope exchange with the hydrogen contained in the vermiculite matrix, rather than with the adsorbed water.

*[Figure 2.17]* Schematic for Tritium Percolation in Peat Soil.

*[Figure 2.18]* Schematic for Tritium Percolation in Vermiculite.

*[Figure 2.19]* Schematic for Tritium Percolation in Peat-Vermiculite mix.

Tritium concentrations decrease in the soil could be attributed to radioactive decay and/or isotopic exchange. Considering the short percolation time ($\sim 300$ s) relative to its half-life of 12.3 years, losses due to decay was considered insignificant. The tritium mass balance in the column was analyzed as shown below.

$$
\nu\frac{dC}{dt} = q_{in}C_{in} - q_{out}C_{out} - q_{ev}C_{ev} + \nu(-k_R C_R) \tag{2.11}
$$

The input concentration $C_{in}$ (mol/m³) with corresponding flow rate $q_{in}$ (m³/s) will undergo an isotope exchange reaction in soil with a mass transfer coefficient representing tritium sorption $k_R$ (1/s) to reduce the concentration to $C_R$. The system output comprises the outflow concentration $C_{out}$ and $q_{out}$ as well as that due to evaporation $q_{ev}$, $C_{ev}$. Assuming a steady state system and the negligible evaporation rate, $C_R = C_{out}$ and $k_R$ can be solved using Eq. (2.12).

$$
k_R = \frac{q_{in}C_{in} - q_{out}C_{out}}{\nu C_{out}} \tag{2.12}
$$

$k_R$ was solved numerically for peat $k_{R,P}$ as $k_{R,P} = 1.3 \times 10^{-3}\,\mathrm{s}^{-1}$. The low values indicate tritium in tritiated water is highly mobile in peat soil and could exchange with hydrogen at further depths.

### 2.7 Summary

#### 2.7.1 Key Findings

- Isotopic exchange is a fast process. The first hour of soil immersion saw a reduction tritium concentration in the liquid phase.
- Equilibrium between solid and liquid phase was established early probably on the first day of immersion. During the immersion period, there was no significant tritium concentration reduction relative to the initial input concentration.
- Vermiculite seems to suppress the tritium retention ability of peat soil.
- The release of tritiated carbon compound in soil suggests the presence of NE-OBT. This could be a buried tritium as proposed by Baumgartner and Donhaerl [21] or due to soil microbial activity.

#### 2.7.2 Conclusions

- Isotopic exchange between tritium and hydrogen contributes to tritium concentration reduction in soils.
- Peat soil showed significant tritium incorporation and retention compared to vermiculite. Due to the high moisture content in peat, isotope exchange was expected.
- The high saturated conductivity and isotope exchange capacity of peat is influenced by its moisture. This indicates that materials with water molecules structurally bonded could undergo significant tritium exchange.
- The IEC values obtained were $4.95 \times 10^{-2}\,\mathrm{mol}\text{-}\mathrm{T}_2\mathrm{O}/\mathrm{g}$ and $3.38 \times 10^{-2}\,\mathrm{mol}\text{-}\mathrm{T}_2\mathrm{O}/\mathrm{g}$ in peat and vermiculite respectively.

### References (Chapter 2)

[1] M. Shikata et al, Plant Cell Physiol. 57(1) (2016), 11(1-10).
[2] J. Xu et al., Catena 160 (2018), 134-140.
[3] G. Mesri and M. Ajlouni, J. Geotech. Geoenviron. Eng. 133 (2007), 850-866.
[4] A. Kunarso et al., J Soil Sci Plant Nutr 22 (2022), 4063-4083.
[5] G. C. Topp and P. C. Ferre, 2002. Methods for Measurement of Soil Water Content.
[6] B.C. O'Kelly and V. Sivakumar., Dry. Technol. 32(2014) (6), 631-643.
[7] M. Nishikawa et al., J. Nucl. Materials. 277(2000), 1, 99-105.
[8] I. Bisutti and I. Hilke, TrAC Trends in Analytical Chemistry, 23 (2004),10-11, 716-726.
[9] ASTM Standard D2487, 2000.
[10] S. Brunauer et al., J. Am. Chem. Soc., 60, (1938), 309-319.
[11] C. T. Chlou' and D. W. Rutherford, 1993 Env. Sci. Technol. 1003 (1993), 27, 1587-1594.
[12] A-L Nivesse et al., Talanta, 224 (2021) 121803.
[13] O. Peron et al., Chemosphere 196 (2018), 120-128.
[14] T. Hyuga et al. Nuclear Materials and Energy 17 (2018) 62-68.
[15] Furuichi et al., Journal of Nuclear Materials 367-370 (2007) 1243-1247.
[16] Nishikawa et al., Journal of Nuclear Materials 161 (1989) 182-189.
[17] K. Furuichi et al., Fusion Engineering and Design 109-111 (2016) 1371-1375.
[18] Klute and Dirksen, 1986, SSSA Books.
[19] M. Inoue et al Geoderma 435 (2023) 116511.
[20] Y. Zhang et al., Construction and Building Materials 263 (2020) 120614.
[21] F. Baumgartner and W. Donhaerl, Anal. Bioanal. Chem., 379 (2004), 204-209.

---

## Chapter 3: Tritium in Komatsuna

Komatsuna, a leafy vegetable popularly eaten in Japan was grown in the tritium-free laboratory at the Chikushi campus of Kyushu University. Seeds were nursed using water-soaked jiffy-7 peat pellets. After germinating to about $5\,\mathrm{cm}$, plants were transferred to $70\,\mathrm{cm}^3$ pot half-filled with peat soil and vermiculite. A florescent light capable of producing 400-700 nm light was installed at the upper part, and the plants were sufficiently grown at a temperature of about $25^{\circ}\mathrm{C}$ for about 50 days. About $100\,\mathrm{ml}$ autoclaved water was supplied after soil moisture monitoring to avoid soil dryness and to suppress mold growth.

The plants were transferred to the Radioisotope (RI) center, Ito Laboratory in Kyushu University for tritium exposure experiments. As shown in Figure 3.1 plants grown in each pot A-F were placed in an airtight glove box installed in an incubator. To unify the growth conditions of the plant cultivated in each pot, all leaves were excised once at the start of the experiment. Tritiated water of $150\,\mathrm{kBq}/\mathrm{cm}^3$ was supplied at $6\,\mathrm{cm}^3$ directly to the soil in each pot.

Through evaporation from the soil and transpiration of the plants, tritium concentration in the atmosphere in the glove box was expected to increase [1, 2]. This leads to the uptake of tritium to the plants from both soil and atmosphere [3]. Because this experiment focuses on the tritium transport to plants from soil, the atmosphere inside glove box was constantly ventilated. Air was supplied at $0.8\,\mathrm{l}/\mathrm{min}$ by a pump and exhausted at $1.5\,\mathrm{l}/\mathrm{min}$ by another pump. By setting the exhaust flow rate higher than the supply flow rate, the pressure inside the glove box was kept slightly lower than the atmospheric pressure, preventing tritium from leaking to the outside. The exhausted air was passed through two series of water bubblers to collect tritiated water vapor.

Artificial illumination was done with an installed fluorescent lamp to simulate daytime settings and was programmed to supply alternating 12 hours of light and dark. These conditions were selected to simulate natural growth conditions. After pouring tritiated water to the soil, leaves and stems of Komatsuna were sampled over a period of 86 days.

A part of the soil was also collected to evaluate tritium amount in the soil. Sampling of stem, leaves and soil were done 7, 5 and 4 times respectively. At the end of the experiment after 70 to 80 days, the whole Komatsuna was collected separately into main stem, lateral stem, leaves, main root, and lateral root.

*[Figure 3.1]* Set-up for Komatsuna cultivation and Tritium Exposure at the RI Center.

### 3.1 Sample Treatment

Komatsuna leaves, stem and roots were sampled into $20\,\mathrm{ml}$ polyethylene vials. Due to transpiration from plant tissues and evaporation from the soil surface, tritium is expected to be deposited on plants and the soil medium [4,5]. As shown in Figure 3.2, sample surfaces were rinsed by submersion in $12\,\mathrm{cm}^3$ distilled water for about $1\,\mathrm{min}$. $1\,\mathrm{cm}^3$ aliquot was sampled for liquid scintillation counting.

Plant leaves and stems were later immersed in water in each polyethylene vial. The amounts of water were $22\,\mathrm{cm}^3$ for stems and $120\,\mathrm{cm}^3$ for leaves, respectively. Distilled water mixed with about $18\%$ ethanol was used as immersion water to prevent rotting of the samples. $1\,\mathrm{cm}^3$ was periodically sampled for liquid scintillation counting to monitor the TFWT concentration until it became steady.

*[Figure 3.2]* Process Flow for Sample Rinsing.

### 3.2 Drying, Isotope Exchange and Combustion

To extract slight TFWT left in the sample after water immersion, the sample was dried in vacuum [6] and released tritiated water was collected in water bubblers as shown in Fig. 3.3. After immersion in water, the sample was removed, and the water adhered on the surface of the sample was wiped off. Then, the samples were weighed and packed in a quartz tube, and both ends of the sample bed fixed with quartz wool. A valve on the upstream side of the quartz tube was closed, and a diaphragm pump was operated and vacuum drying of the sample was performed. The released tritiated water vapor was collected in double water bubblers. $1\,\mathrm{cm}^3$ of water was periodically sampled from the bubblers and the tritium concentration was measured by the LSC. Vacuum drying was terminated when the increase in tritium concentration in the bubbler water was no longer observed.

After vacuum drying, the tube containing sample was reweighed and the effective sample weight evaluated. The valve on the upstream side of the quartz tube was opened, and the diaphragm pump was operated. The air flow rate introduced in the quartz tube was adjusted with a flow controller installed upstream of the pump. In this process, E-OBT was extracted through an isotope exchange reaction with water vapor in air. A hygrometer monitored the humidity in the introduced air to be between $60\% - 70\%$. Air drying was terminated when the increase in tritium concentration in the bubbler water was no longer observed.

*[Figure 3.5]* Vacuum and Air-Drying Set-up.

After air exposure, the samples were transferred to a new quartz tube for combustion to extract NE-OBT. Experimental setup for combustion is shown in Fig. 3.4. The samples were completely combusted [7] at $800^{\circ}\mathrm{C}$ for 30 minutes by an electric furnace with flowing $40\%$ $\mathrm{O}_2/\mathrm{Ar}$ at $60\,\mathrm{cm}^3/\mathrm{min}$. This purge gas was generated by passing $1\%$ $\mathrm{H}_2/\mathrm{Ar}$ gas and $40\%$ $\mathrm{O}_2/\mathrm{Ar}$ gas through a Pt catalyst bed. The flow rate of $1\%$ $\mathrm{H}_2/\mathrm{Ar}$ gas was $80\,\mathrm{cm}^3/\mathrm{min}$ and that of $40\%$ $\mathrm{O}_2/\mathrm{Ar}$ gas was $20\,\mathrm{cm}^3/\mathrm{min}$.

The water vapor in the purge gas recovered tritium sorbed on the piping system at the downstream of the quartz tube by the isotope exchange reaction. The released tritium was collected by two series of water bubblers. A Pt catalyst bed was set between the first bubbler and the second bubbler and heated to $400^{\circ}\mathrm{C}$. HTO was collected in the first bubbler and HT and hydrocarbon such as tritiated methane $\mathrm{CH}_3\mathrm{T}$ were collected in the second bubbler. Tritium concentration in each bubbler was measured by the LSC.

*[Figure 3.4]* Set-up for Sample Combustion.

### 3.3 Results and Discussion

Lateral stems were collected after 1, 8, 34, 42, 54, 72 and 86 days, and leaves were collected after 34, 42, 54, 72 and 86 days, after pouring tritiated water directly on the soil. Figure 3.5 shows the variation of tritium concentration in lateral-stem is relatively quickly released into water by isotope exchange reaction. The release from xylem tissues and cuticular damage during the air-drying process may account for this observation.

*[Figure 3.5]* Tritium Concentration Variations in Lateral-stem Immersed Water.

Figure 3.6 shows the change of tritium concentration in immersion water for the leaves collected from Komatsuna A, B, D cultivated for 34 days, where the values are normalized by the weight of samples. After the initial first day large increase in concentration, it remained steady throughout. Like stems, TFWT retained in leaves is released into water relatively quickly through isotope exchange reactions with water.

*[Figure 3.6]* Tritium Concentration Variations in Leaf-Immersed Water.

There was no significant difference in tritium release behavior between stems and leaves during water immersion as the retention amounts were similar. After 86 days when the Komatsuna was withering, the stems and leaves of this sample were also collected and immersed in water, but no release of tritium into water was observed. This indicates that the TFWT contained in the plant is released into the atmosphere when the plant dies.

After 54 days, whole Komatsuna was sampled from the roots, and separated into stem, main root, and lateral root, and immersed in water. Figures 3.7 and 3.8 show the time variation of tritium concentration in the water immersing the stem, and the roots, respectively. In these figures, the value at time zero is the background value before the sample was immersed in water. Obvious release of tritium was observed from the stem, and it was confirmed that TFWT was present even after 54 days. On the other hand, the increase in tritium concentration in the water immersing the roots was slight. No significant tritium release was observed from the lateral roots.

*[Figure 3.7]* Tritium Concentration Variations in Stem-Immersed Water.

Although the tritium concentration in water immersing the main root increased slightly, it is possible some soil may still have been adhered to the roots. Continuous rinsing of roots to remove soil particles can be challenging as it is not entirely effective. The amounts of tritium released from roots were much less than that from the leaves and the stems. This is because, root tissues are primarily conducting tissues and tend to transmit their contents by capillary action to other parts of the plant. This implies any tritium observed is likely to be residual tritium in roots or contributions from surrounding soil particles. It was found that tritium in soil is transported to stems and leaves through roots, but tritium retention in roots is much smaller than that in stems and leaves.

*[Figure 3.8]* Tritium Concentration Variation in Root-Immersed Water.

After pouring tritiated water into the soil, the amount of tritium in the soil is expected to decrease with time due to direct evaporation from the soil, plant uptake and transpiration, and tritium decay. About 2 g of the soil was collected from each pot for Komatsuna A to F, immersed in tritium-free water for 5 hours and aliquots sampled for LSC. The samples were collected 22, 49, 70, and 134 days after the tritiated water was poured. An immediate increase in tritium concentration was observed in the liquid phase, as was the case with leaves and lateral stems. It is thought that the tritiated water retained in the soil was released into the water quickly [8], through an isotopic exchange reaction. Figure 3.9 shows the relationship between the amount of tritium released from the soil to water and the cultivation time at the time soil was sampled. It was clearly showed that the amount of tritium in each soil decreased at almost the same rate with elapsing cultivation time. Reduction in soil concentration may be due to leaching of tritium down the cultivating soil, evaporation and uptake by Komatsuna.

*[Figure 3.9]* Tritium Concentration Variation in Komatsuna-grown Soil.

Figure 3.10 shows the time variation of the amount of tritium per unit mass released from stems and soil by water immersion. It is clearly shown that the amount of tritium released from the stem decreases with elapsing cultivation time. The amount of tritium released from the leaves also tended to decrease with elapsing cultivation time. From these results, it implies the amount of TFWT in Komatsuna depends on the tritium concentration in the soil, and its concentration in stems and leaves in decreases as the tritium concentration in the soil decreases.

*[Figure 3.10]* Tritium Concentration Variation released in Stems and Soil by Water Immersion.

The amount of Tissue Free Water (TFW) in the sample can be obtained from the mass change before and after vacuum drying. By dividing the amount of TFWT by the amount of TFW, the approximate tritium concentration in TFW in the sample can be calculated. For the stems of sample B and C on day 1 after tritiated exposure, and the leaf of sample A on day 34 after, the calculations were done. The obtained tritium concentration in each TFW was $8.8\,\mathrm{kBq}/\mathrm{cm}^3$ for B, $14.3\,\mathrm{kBq}/\mathrm{cm}^3$ for C and $1.9\,\mathrm{kBq}/\mathrm{cm}^3$ for A.

The tritium concentration of water in soil can also be obtained by the same method, but vacuum drying was not performed for the soil samples in this experiment. Here, the tritium concentration in soil water was calculated assuming a water content of $70\%$. The obtained tritium concentration in each soil was $9.7\,\mathrm{kBq}/\mathrm{cm}^3$ for B, $11.1\,\mathrm{kBq}/\mathrm{cm}^3$ for C and $1.6\,\mathrm{kBq}/\mathrm{cm}^3$ for A. These values are close to the tritium concentration in TFW of each sample. These results suggest that the tritium in the root zone was at equilibrium with that in Komatsuna.

For the stem sample of Komatsuna sampled 1 day after tritiated water was poured in the soil, TFWT, E-OBT and NE-OBT were evaluated on a $0.383\,\mathrm{g}$ sample. The tritium amount and related forms released in each process was summarized in Table 3.1. The total amount of tritium retained in the sample was $8.736\,\mathrm{kBq}/\mathrm{g}$. No significant tritium release was detected in vacuum drying. This indicates that almost all TFWT was released by water immersion. A relatively large amount of tritium was extracted by air exposure after vacuum drying. It is speculated that the tissue in the stem was destroyed by vacuum drying, and that E-OBT, which could not be determined by the immersion water, could be extracted with water vapor in air, and tritium was released through an isotope exchange reaction.

**Table 3.1** Tritium Amount and Existing Forms in Komatsuna.

| Process | Tritium amount [kBq] | Ratio (Tritium Amount/Total Tritium) [%] | Retention form |
|:--------|:---------------------|:-----------------------------------------|:---------------|
| Water immersion | 2.433 | 72.7 | TFWT |
| Vacuum drying | BG Level | - | TFWT |
| Air exposure | 0.650 | 19.4 | E-OBT |
| Combustion | 0.263 | 7.9 | NE-OBT |

### 3.4 Summary

#### 3.4.1 Key Findings

The TFWT form was prominent in Komatsuna similar to general TFWT distribution in plants. However, for a herbaceous plant with broad leaves, evapotranspiration accounts for significant tritium losses. This implies a lower percentage range is expected. It is considered that the enclosed environment held significant tritium concentrations in the growing atmosphere leading to interception. It can be inferred that tritium concentrations in glovebox experiments leads to significant canopy interception hence elevated surface tritium concentration thereby impacting TFWT evaluation. 7.9% NE-OBT is significantly high compared to the $<1\%$ generally reported for low tritium concentration exposure experiments. It can be inferred that the high tritium concentration used, small growth environment and long exposure time to the tritium source may have accounted for this.

#### 3.4.2 Conclusions

Komatsuna was cultivated in peat soil contaminated with tritium with the results obtained shown above. There was no significant difference in tritium release behavior between stems and leaves during water immersion, and retention amounts were similar. Komatsuna as a herbaceous plant has no specialized plant tissue for storage of photosynthetic products hence the stem and leaves were equally involved in this process. At any time, the tritium content in both tissues were at equilibrium thereby accounting for the similar variation in tritium concentration. The amounts of tritium released from the roots were much less than that from the stems and leaves. The amount of TFWT in Komatsuna depended on the tritium concentration in the soil, and that tritium concentration in the stems and leaves in Komatsuna decreased as the tritium concentration in the soil decreased. The tritium concentration in TFW contained in the stems and leaves of Komatsuna was almost the same as the tritium concentration in water in soil. As tritium is transferred from the roots to the leaves by the stem, the concentration is expected to reduce along this gradient. An aggregation of the stem and leaf tritium content should be closer to that of the root. The ratio of the forms of tritium present in the stems of Komatsuna 1 day after tritiated water was poured into the soil was $72.7\%$ in TFWT, $19.4\%$ in E-OBT, and $7.9\%$ in NE-OBT.

### References (Chapter 3)

[1] C. Boyer et al., Environ. Exp. Bot., 67, 34 (2009).
[2] C. E. Murphy, Health Phys., 65 (1993), 683.
[3] Y. Belot, Radiat. Prot. Dosim., 16 (1986), 1-2, 101.
[4] N. Momoshima, J. Radioanal. Nucl. Chem., 239 (1999), 3, 459.
[5] D. Galeriu et al., J. Environ. Radioact., 118 (2013), 40.
[6] T. Matano, Fusion Eng. Des., 173 (2021), 112787.
[7] C. Cossonnet, Appl. Radiat. Isot., 67 (2009), 809.
[8] F. Pointurier et al., J. Environ. Radioactivity 68 (2003) 171-189.

---

## Chapter 4: Tomato Cultivation and Tritium Exposure

The cherry tomato type, Micro-Tom used in this experiment is a widely used model cultivar known to have improved phenotypic and genotypic characteristics suitable for tritium exposure experiment to evaluate radiocological and biological impact. Seeds obtained from TOMATOMA project were nursed during the summer for 3 days and transferred to planting pots $70\%$ filled with commercially available peat soil and vermiculite. After 69 days, a fully matured tomato plant weighing $0.6533\,\mathrm{kg}$ with both ripe and unripe fruits was transferred to the radioisotope center at Kyushu University, Ito campus for tritium exposure and analysis.

### 4.1 Experimental Set-up and Treatments

#### 4.1.1 Plant Placement and Tritium Supply

Fig 4.1 shows the set-up for the Microtom tritium exposure and cultivation. The sample tomato plant was set-up in a small primary glovebox of approximate dimensions L53cm × H50cm × W43cm fitted with regulators and sensors to maintain and record environmental parameters such as $\mathrm{CO}_2$, humidity, temperature, pressure and light intensity (Figure 4.2).

*[Figure 4.1]* Primary Glovebox for Tomato Cultivation and Tritium Exposure.

*[Figure 4.2]* Sample Environmental parameters Recorded During the Tritium Exposure Period (a) Relative Humidity, Temperature, Illuminance (b) $\mathrm{CO}_2$ Variation.

This glovebox was also housed in a larger secondary glovebox of approximate dimensions L100cm × H85cm × W60cm as shown in Figures 4.3 (a) (b). Two $500\,\mathrm{ml}$ and $1000\,\mathrm{ml}$ bubbles were fitted to the internal and external gloveboxes respectively to trap released tritium. A dual-purpose air/vacuum pump provided air to the plants with an input-output rate of $0.6\,\mathrm{L}/\mathrm{min} - 0.8\,\mathrm{L}/\mathrm{min}$ respectively to lower the atmospheric pressure in the internal glovebox. A florescent bulb was placed on top of the primary glovebox and automatically set to 16 hours light period and 8 hours dark according to the recommended micro-tom greenhouse growth protocol. 100 ml of $12\,\mathrm{MBq}$ HTO was supplied once to the topsoil.

*[Figure 4.3]* (a) Tomato Set-up in Larger Glovebox (b) Schematic of Tritium Exposure.

#### 4.1.2 Imaging Plate (IP) Radiography on Leaves

This technique is used for x-ray exposure detection and quantification in soil, plants [1,2] and metal surfaces [3-5]. The GE Amersham typhoon 600 imager was used to analyze the surface of leaves grown in the tritium environment. As shown in figure 4.4, two leaves—taken from middle and top part of the plant sample were mounted on 12cm by 7cm Fuji BAS-TR2025 phosphor plate. The BAS-TR type-IP was selected over the BAS-MS type-IP due to its ability to detect tritium beta radiation and has no protective surface [6]. Mounting was done in a dark room at $22^{\circ}\mathrm{C}$ and the mounted plate stored in an aluminum cassette for 17 hours shielded in a 10cm thick leaded-brick chamber against external radiation. Sample leaves were then dismounted, read and the etched image analyzed using the Image Quant™ TL software.

This technique for tritium detection and quantification is based on the principle that the photostimulated luminescence (PSL) intensity produced during the de-excitation of beta electrons to the ground state is directly proportional to the tritium concentration ($C_T$).

$$
PSL \approx C_T \tag{4.1}
$$

*[Figure 4.4]* a) Leaf from Middle [Left] and Upper [Right] Part Mounted on the BAS-TR Plate b) Corresponding PSL Image Showing Tritium [in red] Areas.

As shown in Fig 4.5, the high intensity observed between pixel positions 550-1050 corresponds to leaf sampled from the lower part of the plant. Beta radiation for leaf from the upper part of the plant showed weak intensity. Tritium evaporated from the soil remains in the glovebox atmosphere cloud with a proportion evacuated, redeposited or intercepted by the leaves and other tissues. Since the glovebox evacuation rate is constant, the tritium amount depends on the leaf position.

It is assumed that the higher the position of the leaf, the greater the tritium loss assuming an even leaf distribution on either side of the plant. Through surface evaporation and isotopic exchange with glovebox atmosphere, TWFT and e-OBT in the top-based leaf was lost. The absence of IP detected tritium on the upper leaf suggests this technique may be used for surface contamination assessment of leaves and other thin specimen.

*[Figure 4.5]* PSL Intensity Distribution Across three (3) Cross-Sections.

#### 4.1.3 Rinse, Vacuum and Air Drying

Sample rinsing was done by using 10-20ml distilled water to rinse the surfaces. Samples were excised from the main plant, held with tweezers and either immersed for about a minute or washed with rinsing water. This technique is widely used for TFWT removal as it easily incorporated plant surface tritium into the water pool.

Vacuum drying was done to remove any remaining rinse water on the surface and to also extract non-bounded tritium. Samples were weighed and packed into 3mm diameter quartz tube of 20cm length and supported with quartz wools. One end is closed, and the other end connected to a vacuum pump installed with water-filled bubblers. Suction is done for 7 hours after which vacuumed samples are reweighed for the next stage of air drying. Water from the installed bubblers were sampled for LSC.

Air drying is done to induce isotopic exchange between exchangeable tritium in the sample and hydrogen contained in air moisture. 2L/min non-tritiated atmospheric air is passed over samples for 7 hours and the liberated tritium trapped in water bubbler, after which samples were reweighed. The tritium atmosphere in the RI lab is periodically sampled by conducting blank air drying to obtain corrected backgrounds.

### 4.2 Results and Discussion

#### 4.2.1 Tritium in the Leaves

*[Figure 4.6]* Fruit and Leaf Surface Rinse Concentrations.

Leaf surface concentration was two orders more than that of fruit surface and stem as shown in Figure 4.6. MicroTom leaves have large exposure area due its broad horizontal orientation as compared to the fruit which is spherical with a smaller exposure surface. Similarly, stems are thinner with diagonal, horizontal or vertical orientations. Also, the surface of tomato fruit is smoother than leaves. This implies leaves have a higher exposure surface availability for interception and hold-up of HTO in the glovebox atmosphere.

Leaves are the site of OBT formation through photosynthesis. As shown in Fig. 4.7, TFWT is one order higher than NE-OBT. For the exposure period, there was a corresponding increase in both TFWT and NE-OBT on day 2 which implies an equilibrium tritium conversion to TFWT and simultaneous production of NE-OBT. On day 6, contrasting peaks were observed which implied a significant production of NE-OBT from TFWT. Both tritium fractions reduced significantly on the day 14 suggesting no further OBT production after day 6.

*[Figure 4.7]* TFWT and OBT Fractions in MicroTom Leaves.

#### 4.2.2 Fruits and Stem

OBT formed in leaves are transferred to tissues including the flowers, fruits and stem. Figure 4.8 showed TFWT one (1) order higher than that in juice and NE-OBT for fruits and a similar trend between TFWT and NE-OBT in stem. During the exposure period, the tritium fractions followed the same activity concentration change, initially increasing between day 2 to 5 and sharply decreasing on day 9 by a factor of 7.5 for fruits. Values for day 9 were obtained after analyzing unripe fruits. The sampled fruit juice also showed significant presence of tritium with a high concentration observed on day 5 and day 14. There was a similar sharp decrease in stem tritium concentration between day 6 and 9 as shown in Figure 4.9. Ripe fruits are known to respire at about 4 times the rate in unripe fruits [7]. Due to faster deterioration by ripe fruits, they lose a higher percentage of its content resulting in the high tritium fractions observed.

The phase of tritium concentration increase in stem seems to correspond to a decrease in leaf concentration within the same period. Translocation of OBT from leaf to edible parts such as fruits and stem are defined by the translocation index [8]. Leaves are the main photosynthetic organs of the plants and the site for OBT production. Through transport tissues such as phloem, OBT is translocated to fruits and stem.

*[Figure 4.8]* Variation of Tritium Fraction Concentrations in Fruit.

*[Figure 4.9]* Variation of Tritium Fraction Concentrations in Stem.

Figure 4.10 compares the TFWT and NE-OBT for days 2 and 14 representing 48 hours after initial HTO exposure and the last day of sampling respectively. Some terrestrial organisms directly feed on the edible portions of tomato hence the impact of TFWT as a source of tritium exposure cannot be underestimated. Rinse concentrations analyzed between a 12-day interval showed marked decreases of about $83\%$ in leaves to $95\%$ in stems. However, that in fruit increased by $95\%$ in the same period. TFWT values however tend to depend on the interception rate, plant canopy distribution and evapotranspiration dynamics in the glovebox. The significant decrease in stem and root NE-OBT could be due to growth dilution. The stem and roots are known to undergo indeterminate growth [9] where this tissue types continue to grow during the plant's life cycle. This contrasts with that determinate growth of leaves and fruit which terminates at stage in the plant life cycle.

#### 4.2.3 Tritium in Roots

The roots were sampled on the last day (day 14) of harvest because it was the main support for the entire plant and assessing it in the early days will cause plant mortality. The primary and lateral roots were isolated after several rinsing with distilled water to remove adhered soil on the surface.

*[Figure 4.11]* Pictures of Root sampling a) soil core with roots, b) 1st rinse to dislodge soil, c) 2nd Rinse d), 3rd rinse with visible lateral roots, e) main root, f) weighing lateral roots, g) sample lateral root.

Rinsing, vacuum and air drying as well as combustion were done on the isolated samples to determine the tritium fractions present. From Figure 4.12, the rinse fractions representing TFWT was naturally and 2 orders larger than its constituent OBT. This was expected due to the large amount of contaminated soil adhered to this part of the plant and the difficulty of displacing it entirely. The lateral roots maintained a high amount of tritium fractions except for its NE-OBT concentration which was 2 orders less. The NE-OBT component in the primary root was about $90\,\mathrm{Bq}/\mathrm{g}$, which was significantly less than its TFWT and E-OBT.

The value of E-OBT recovered during the vacuum drying process may be because of water molecules remaining after the rinsing process. The high tritium concentration in the lateral roots as compared to the primary root could be explained by referring to the lateral roots as the primary contact to soil tritium. As a conducting tissue, it is responsible for transporting soil solutes by absorption and capillary action to the primary roots. Therefore, it is possible to have residual tritium at any time during its growth phase.

*[Figure 4.12]* Tritium Forms and Distribution in Primary and Lateral Roots of MicroTom.

#### 4.2.4 Translocation Index (TLI)

This index defines the ratio of OBT in a tissue of interest to the TFWT of leaves at the time of harvest, and which is dependent on the growth stage of the plant. Diabate and Strack [8], argued this as a good measure to assess tritium tissue-to-tissue transfer and infer a spatio-temporal characteristic. In Fig. 4.13, TLI for leaf-fruit is one 4x higher than for leaf-stem and seem to decrease exponentially by an inverse square root. This was expected as fruits serves as major sinks for photosynthates. Additionally, it is now known that stems and fruits are also involved in photosynthesis [10] though in limited proportions with the order being leaves > stem > fruits.

The high leaf-fruit TLI suggests a significant transfer of OBT to fruits which are the most economically important parts of the plant. Translocation was high in the first 5 days in fruits and slowed considerably after that which suggests some resistance to OBT formation after a saturation point.

*[Figure 4.13]* Leaf-Fruit (Stem) TLI for a matured MicroTom.

Generally, TLI depends on the plant growth stage and period of sampling. The values tend to be low in the early stages of plant growth and significant during anthesis and fruit development. Also, Ichimasa et al [11] reported significant TLI during the day than at night for soyabeans. On an average, it tends to decrease as more fruits are formed. Compared to a similar TLI experiment in cherry tomato, the TLI value for MicroTom using the highest value seems to significantly higher to the result for the average night and day values as shown in Figure 4.14. In this study, the value was considered an aggregate for both day and night conditions. It is important to note that, tritiated water vapor was used in the cherry tomato experiment for acute periods (1 hour) as compared to the 48 hours continuous exposure with a highly concentrated tritium amount. A similar TLI comparison was done with other food crop experiments (Appendix C).

*[Figure 4.14]* Comparing TLI in Microtom to that for Cherry Tomato [12].

#### 4.2.5 Evapotranspiration

It is considered that the concentration measured in the bubbles was due to evaporation from the soil and evapotranspiration from the plants. Figure 4.15 shows emission concentration during evacuation of the primary and secondary gloveboxes during the tritium exposure period. With an average evaporation rate $2.6\,\mathrm{kBq}/\mathrm{Day}$, the tritium concentration in the primary glovebox was three times higher, increasing by a factor of 7 in the following 11 days. The high concentration in the immediate environment is explained by considering the contaminated soil as a point source. Further out the smaller glovebox, bubbler-trapping and dilution effects reduce the concentration hence smaller values observed in the secondary glovebox. Generally, the analyzed evapotranspiration of $\mathrm{Day}^{0.67}$ is $17\%$ higher than a theoretical wet bare surface evaporation rate of $\mathrm{Day}^{0.5}$ [13]. This confirms the contribution of plant transpiration to the total tritium released into the environment.

Soil layer analysis as shown in Figure 4.16 indicated a consistent increase in soil surface concentration over the period of exposure. Generally, the sub-surface layer (about $5\,\mathrm{cm}$ deep) showed the highest concentration, consistent with a similar $25\,\mathrm{cm}$ soil core analysis for OBT [14]. There was a decrease in the sub-soil and root zone tritium concentrations in contrast to a general increase in the surface concentration. It is considered that continuous extraction of soil moisture containing HTO through evaporation, plant transpiration and redeposition due to localized precipitation accounted for this.

*[Figure 4.15]* Tritium Concentration in the Atmosphere of the Gloveboxes.

*[Figure 4.16]* Tritium Concentration in sampled layers of the soil.

Analysis of the tritium forms in the leaves, stem and fruit for MicroTom over the 14-day exposure period is summarized in Table 4.1. These values were calculated against the input concentration of $0.12\,\mathrm{MBq}/\mathrm{cc}$. Since E-OBT exists in equilibrium with TFWT, they were unified in the table as TFWT. The combustion parameter representing NE-OBT was presented in the table as OBT. The TFWT and OBT in leaves reduced gradually over the period. As site for OBT production, leaves first convert HTO to OBT before translocating to other tissues. Only a small proportion of HTO is converted as shown.

Tritium fraction analysis in stem showed a similar gradual reduction in OBT but varies for TFWT distribution. Stems grow more rapidly causing a growth dilution of incorporated tritium. Further, OBT storage is not uniform across the stem, and this may account for the variance.

For fruits, except for the unripe fruit on day 9, the TFWT increase over the period while the OBT concentration initially increase and then decreased sharply. Due to ripening, respiration is high and tomato cover begins to lose its strength thereby releasing its content gradually. This and other biological processes release any TFWT or E-OBT.

**Table 4.1** TFWT and OBT variation in MicroTom Tissues over the Exposure Period.

| Plant Tissue | Tritium Form | Ratio of Tritium form at Harvest [%] (Day 2) | Ratio of Tritium form at Harvest [%] (Day 6) | Ratio of Tritium form at Harvest [%] (Day 9) | Ratio of Tritium form at Harvest [%] (Day 14) |
|:-------------|:-------------|:--------------------------------------------:|:--------------------------------------------:|:--------------------------------------------:|:---------------------------------------------:|
| Leaves | TFWT | 12.9 | 9.08 | - | 5.24 |
| Leaves | OBT | 0.52 | 0.84 | - | 0.09 |
| Stem | TFWT | 13.74 | 9.55 | - | 15.34 |
| Stem | OBT | 1.38 | 0.13 | - | 0.07 |
| Fruit | TFWT | 5.26 | 6.53 | 1.39 | 9.17 |
| Fruit | OBT | 0.63 | 0.83 | 0.13 | 0.25 |

The tritium balance was evaluated to assess the amount taken up by the plant and related environmental compartments. As shown in Table 4.2, about $6.5\%$ of the input tritium was taken up by the plant with a significant amount ($62.3\%$) removed by evaporation and transpiration. About $30\%$ remained at the bottom of the container due to percolation and also on the walls of the glovebox. Only a small proportion ($1\%$) remained near the root zone of the plant.

**Table 4.2** Tritium Balance at the End of the Exposure Period.

| Item | Concentration (MBq) | Ratio (%) = (Tritium amount / Input Tritium) |
|:-----|:--------------------|:---------------------------------------------|
| Tritium Input | 12.45 | 100.0 |
| Total tritium in Tomato | 0.81 | 6.5 |
| Total tritium trapped in bubbles | 7.76 | 62.3 |
| Tritium in soil root zone | 0.13 | 1.0 |
| Tritium at the base of cultivation container | 3.70 | 29.7 |
| Unaccounted | 0.05 | 0.4 |

### 4.3 Summary

#### 4.3.1 Key Findings

OBT is formed relatively early (within 2 days) of exposure and decreases in concentration with time due to physicochemical and biological processes including growth dilution. TFWT distribution remains significantly high but reduces in the plant tissues with time except for fruits. Leaf interception of tritiated water on its surfaces is not uniform. It varies by leaf position, canopy density and local weather conditions. NEOBT is present in all tissue parts even after 14 days which confirms OBT persistence. The stem for tomato seems to hold-up significant amounts of NEOBT but the concentration is severely impacted by growth dilution.

#### 4.3.2 Conclusion

MicroTom was exposed to high concentrated tritiated water via the soil and the plant parts were sampled over a 14-day period. Only $6.5\%$ of total tritium was transferred to the plant. The IEC determined for peat and vermiculite in the immersion experiment implies a longer contact time between solid soil and liquid HTO phase is required for significant tritium retention hence a quick loss of soil HTO by evaporation. The local conditions in the glovebox intended to maintain optimal growth conditions further induced soil evaporation hence a significant tritium-in-air concentration. By translocation, OBT is distributed to other parts of the plant with a diminishing concentration over the period. The use of imaging plate technique for surface concentration detection may be optimized to serve as a first step elimination method and enhance robust tritium balance calculations.

### References (Chapter 4)

[1] M. Koch et al., Analytical and Bioanalytical Chemistry, 411 (2019), 1253-1260.
[2] N. Suzuki et al. Quantum Beam Sci. 3 (2019), 18.
[3] Y. Ohuchi et al., Proc. Radiochim. Acta 1, 49-53 (2011).
[4] T. Isobe et al., Health Physics 104 (2013) (4), 362-365.
[5] Hashizume and Oki, Fusion Science and Technology, 71 (2017), 344-350.
[6] H. Ohuchi-Yoshida et al., Fusion Engineering and Design 87 (2012) 423-426.
[7] Factors Affecting for Fruit Ripening in Banana.
[8] S. Diabate and S. Strack, J. Environ. Radioact. 36 (1997), 157-175.
[9] T. Michaels et al, The Science of Plants (2022).
[10] R.J. Henry et al., Biology 2020, 9, 438.
[11] M. Ichimasa et al., FST (2002), 41:3P2, 393-398.
[12] S.B. Kim 2010.
[13] W. A. Jury and R. Horton, 2004. Soil Physics, 6th ed., 127:156-157.
[14] S.B. Kim et al., Journal of Environmental Radioactivity 104 (2012) 94-100.

---

## Chapter 5: Soil Decontamination

Tritium removal from contaminated matrices has remained a challenge thereby calling for separation or reducing strategies and technologies [1,2]. Due to its mobility and integration into water molecules, tritium poses a unique challenge for remediation efforts [3]. Techniques for tritium removal from soil include physical separation, chemical treatments, and biological approaches. Each method has its advantages and limitations, highlighting the need for integrated and site-specific strategies. No single method provides a comprehensive solution for soil tritium removal. The choice of technique depends on site-specific factors, including the extent of contamination, soil characteristics, and available resources.

### 5.1 Tritium Removal from Soil

#### 5.1.1 Physical Methods

This can be done by excavating the contaminated site and replacing with clean soil. It is usually deployed for large and heavily contaminated site. However, this a disruptive process which is expensive with associated secondary waste issues [4]. Another method involves soil washing with chemical or water-based solutions to remove loosely bound tritium. This method is limited in accessing tightly bound tritium integrated in the soil matrix [5]. Further, thermal treatment of contaminated soil has been proposed. This technique was used for a large amount of soil confined in large built concrete confinements [6].

#### 5.1.2 Chemical Methods

Sakharovskii et al [7] proposed the use of Isotopic Exchange technique by using hydrogen-containing compounds to access and exchange for tritium in contaminated soil. Since IE is known to occur very fast and equilibrates with the environment, it is important to control the reaction conditions. Others also proposed the use of chemical agents to reduce tritium mobility in soil. However, this depends on the physicochemical characteristics of the soil and the tritium concentration [8].

#### 5.1.3 Biological Methods

Tritium removal by bioremediation using microorganisms to metabolize tritiated compounds and transforming into less toxic forms has been proposed. The use of plants in phytoremediation is relatively ineffective and under investigation [9].

After harvesting the Microtom, an attempt was made to remediate the soil before discarding. A simple experiment was devised to remove by evaporation [10,11] or drying based on argon purge coupled with isotopic exchange reaction under varying conditions to access the best removal approach. The basic principle is to remove as much tritium as possible at a low cost. Figure 5.1 shows the set-up for tritium removal from a column of soil.

### 5.2 Decontamination Set-up and Soil Treatment

After harvesting, the soil in the cultivation pot was transferred to a large tray in the glovebox and thoroughly mixed. Figure 5.1 shows the proposed set-up for soil decontamination. A quartz tube of length $20\,\mathrm{cm}$, $3\,\mathrm{cm}$ diameter and $3\,\mathrm{mm}$ thickness was partially filled with contaminated peat/vermiculite soil to a height of $5\,\mathrm{cm}$. It was loaded and hermetically sealed under vacuum in a glovebox. Purge gases were connected to the upstream side and two bubblers filled with $100\,\mathrm{cm}^3$ distilled water were installed to collect the evacuated tritium. A Dew Point (DP) sensor coupled to a Graphtec mini GL240 digital recorder was installed between the tube and the bubblers to measure the vapor pressure.

*[Figure 5.1]* Set-up for Spent Soil Decontamination.

The sample was subjected to three different treatments to determine the best removal method. Below is a summary table of the treatments:

**Table 5.1** Soil Contamination Treatments Performed.

| Stage | Purge Details |
|:------|:--------------|
| Treatment 1 (i) | Ar purge only at 100 cc/min |
| Treatment 1 (ii) | Ar purge only at 150 cc/min |
| Treatment 1 (iii) | Ar purge only at 200 cc/min |
| Treatment 2 (i) | 40% O₂/Ar at 20 cc/min + 1% H₂/Ar at 80 cc/min |
| Treatment 3 (ii) | 40% O₂/Ar at 20 cc/min + 1% H₂/Ar at 80 cc/min + Heating at 100°C |

Decontamination treatment was done for approximately 8 hours with the tritium trap replaced every 30 mins and sampled for liquid scintillation counting at a count rate of 3 min/sample.

### 5.3 Results and Discussion

#### 5.3.1 Calibrating the Dew Point Meter

The DP meter was calibrated against its output voltage for a pure argon gas with no soil. Under dry conditions, the DP meter measured dew point value should be proportional to the signal voltage. Figure 5.2 shows the relationship between dew point and the detected voltage signal using a blank set-up.

*[Figure 5.2]* Response Curve of the Dew Point Meter.

From Figure 5.2, the corresponding DP can be deduced from the Voltage (V) using the following equation,

$$
DP = 29.99759V - 129.9336 \tag{5.1}
$$

The dew point is the temperature at which the water vapor in a sample of air at constant atmospheric pressure condenses into liquid water at the same rate at which it evaporates. It is related to the temperature at which the layer of air above the soil sample in the column becomes saturated with moisture vapor due to evaporation of tritiated water therefore it's a good measure of moisture removed from the soil. Empirical data (appendix) for DP at different partial vapor pressures was extrapolated from the psychrometric chart of water at low temperatures. By constructing the relationship, the partial vapor pressure exerted by the evaporated tritiated water could be inferred.

*[Figure 5.3]* Graph Showing Saturated Vapor Pressure and Related Dew Point at Low Temperatures.

It can be seen from figure 5.4 that the mass activity decreases exponentially with time except for rare spikes which occurred during a period when the experiment was stopped for the following day. These points indicated the water vapor build-up in the column due to continuous evaporation of soil and which was instantly evacuated by argon purge on resumption of the experiment. For Ar purge, all three flow conditions gave similar trend where the initial evacuated temperature was high and seemed to flatten after 5 hours.

*[Figure 5.4]* Mass activity-Time Relationship Under Different Ar Flow Regimes.

In evaluating the best removal method, it is important to estimate the tritium concentrations in the solid and gas phases. The soil solid phase tritium concentration was determined prior to drying by immersing sample soil in distilled water and immersion water analyzed for tritium concentration using LSC.

#### 5.3.2 Argon Purge at 100 cc/min

Plotted data points illustrate the variation in mass activity over time. This curve reveals how the radioactivity of the sample changes in response to the Argon purge.

*[Figure 5.5]* Mass Activity-Vapor Pressure Relationship for Ar Purge at 100 cc/min.

Drying by Argon purge was initially done under 3 different flow rate conditions at 100, 150 and $200\,\mathrm{cc}/\mathrm{min}$ to determine the optimal tritium removal condition. Figure 5.5 shows the Argon purging at $100\,\mathrm{cc}/\mathrm{min}$ with the tritium removed quantified in Becquerel per gram of soil. The saturated vapor pressure represents the equilibrium pressure exerted by the contaminated soil water vapor in the closed system at a given temperature. This parameter is important for maintaining constant environmental conditions throughout the experiment. The vapor pressure remains relatively stable, with minor variations around 42.07 Pa, suggesting that the temperature and humidity are kept consistent throughout the experiment. This stability implies that the observed changes in mass activity are attributable to the Argon purge rather than external environmental factors.

Generally, the mass activity loss over time follows an exponential trend showing a gradual decrease in the evacuated vapor from 43 Bq/g to 12 Bq/g (removal factor of 3.5) with a corresponding soil moisture reduction of 5g. This is expected for a pure argon purge.

#### 5.3.3 Argon Purge at $150\,\mathrm{cm}^3/\mathrm{min}$ and $200\,\mathrm{cm}^3/\mathrm{min}$

Figures 5.6 and 5.7 shows the mass activity for contaminated soil evacuated with pure Ar at $150$ and $200\,\mathrm{cm}^3/\mathrm{min}$.

*[Figure 5.6]* Mass Activity-Vapor Pressure Relationship for Ar Purge at $150\,\mathrm{cm}^3/\mathrm{min}$.

Tritium evacuation at $150\,\mathrm{cc}/\mathrm{min}$ showed a similar trend as that at $100\,\mathrm{cc}/\mathrm{min}$ with a similar removal factor of 3.2. The saturated vapor pressure was also held constant except for the peak attributed to vapor build-up during the shutdown phase. The sample weight after drying indicated a $5\,\mathrm{g}$ loss in moisture like that in the argon purge at $100\,\mathrm{cc}/\mathrm{min}$.

*[Figure 5.7]* Mass Activity-Vapor Pressure Relationship for Ar Purge at $200\,\mathrm{cm}^3/\mathrm{min}$.

As shown in Figure 5.7, tritium removal at a high flow rate of $200\,\mathrm{cm}^3/\mathrm{min}$ tend to flatten after the initial evacuation. However, the high removal ratio of about 6 did not correlate with the final activity concentration remaining in the soil. This implies, the high flow rate initially evacuated the tritium from the soil into the void space in the tube subsequently reduced by purging.

#### 5.3.4 Purging by Isotopic Exchange with $\mathrm{H}_2/\mathrm{Ar}$ and $\mathrm{O}_2/\mathrm{Ar}$

*[Figure 5.8]* Mass Activity-Vapor Pressure Relationship for $\mathrm{H}_2/\mathrm{Ar} + \mathrm{O}_2/\mathrm{Ar}$ Purge at $100\,\mathrm{cm}^3/\mathrm{min}$.

By introducing water vapor, it is expected that free hydrogen will be exchanged with tritium in the soil. Figure 5.8 shows tritium removal using wet gas comprising $40\%$ $\mathrm{O}_2/\mathrm{Ar}$ and $1\%$ $\mathrm{H}_2/\mathrm{Ar}$ at $20\,\mathrm{cm}^3/\mathrm{min}$ and $80\,\mathrm{cm}^3/\mathrm{min}$ respectively. The removal ratio was about 7 with a corresponding 3-fold reduction in the soil mass activity from 3111.41 Bq/g to 1111.5 Bq/g.

Since heating is known to induce faster evaporation, a heating jacket was installed around the soil tube and the soil heated to and maintained at $100^{\circ}\mathrm{C}$ for the entire period of sampling. It is assumed this temperature is adequate to remove the moisture trapped in the soil column.

*[Figure 5.9]* Mass Activity-Vapor Pressure Relationship for $\mathrm{H}_2/\mathrm{Ar} + \mathrm{O}_2/\mathrm{Ar} + \mathrm{Heat}$ Purge at $100\,\mathrm{cm}^3/\mathrm{min}$.

As shown in Figure 5.9, the impact of condensation caused by heating can be seen in the sudden rise of the vapor pressure. As at about $480\,\mathrm{min}$, the removal ratio was 3.5 similar to the pure argon purge with visible moisture column seen midway to bottom of the tube. This suggests the soil tritiated moisture is gradually evacuated from the top towards the bottom.

#### 5.3.5 Estimating gas released from soil to the gaseous phase

Using mass balance [12][13] equations, the amount of tritium released from the solid to the gas phase can be estimated. From the principle of mass-balance the rate (t/s) of change in tritium concentration ($C/\mathrm{Bq}\,\mathrm{m}^{-3}$) in a volume of gas ($V_g$) is dependent on the input and output concentration taking into the account the volume of soil ($V_s$), the tritium mass transfer coefficient ($k/\mathrm{s}^{-1}$),

$$
V_g\frac{dc}{dt} = Q C_{in} - Q C + V_g k q \tag{5.2}
$$

where

- $C$: Tritium concentration in the gas phase of the quartz tube $[\mathrm{Bq}/\mathrm{m}^3]$
- $C_{in}$: Tritium concentration in the input gas to the quartz tube $[\mathrm{Bq}/\mathrm{m}^3]$. In this experiment, $C_{in} = 0$.
- $V_g$: The volume of the gas phase of the quartz tube $[\mathrm{m}^3]$
- $t$: Time [s]
- $Q$: Volumetric flow rate of argon gas $[\mathrm{m}^3/\mathrm{s}]$
- $V_s$: The volume of soil $[\mathrm{m}^3]$
- $k$: Tritium mass transfer coefficient from soil to gas phase $[1/\mathrm{s}]$
- $q$: Tritium concentration in soil $[\mathrm{Bq}/\mathrm{m}^3]$

When $t = 0$, $C = C_0$ and when $t = T$, $C = C_T$

$$
\ln\left(\frac{C_T - \frac{V_s k q}{Q}}{C_0 - \frac{V_s k q}{Q}}\right) = -\frac{Q}{V_g} T \tag{5.3}
$$

$C_T$ is now expressed as

$$
C_T = \frac{V_s k q}{Q} + \left(C_0 - \frac{V_s k q}{Q}\right)\exp\left(-\frac{Q}{V_g} T\right) \tag{5.4}
$$

From equation 5.4, fitted curves are shown in figure 5.10. The proposed mass balance model was able to reproduce the experimental results as shown in Figure 5.10.

*[Figure 5.10]* Curve Fitting Based on Mass Balance Equation.

Analysis of the different treatments indicated of significant reduction of soil initial activity by more than $70\%$. It is clear from Figure 5.11, that tritium removed by argon purge is not dependent on the gas flow rate. It can be inferred that, soil characteristics and boundary conditions in the tube affects tritium diffusivity. Isothermal removal and isotopic exchange with gaseous water didn't show any significant difference in the percentage of tritium removed.

*[Figure 5.11]* Soil Decontamination by Gas Purge and Thermal Drying.

### 5.4 Summary

#### 5.4.1 Key Findings

- Drying induced by Argon purging is more efficient than isotopic exchange with gaseous water and isothermal heating.
- Thermal treatment in addition to isotopic exchange with gaseous water induces condensation in the closed system thereby increasing the drying time.
- The choice of decontamination method depends on the size of the contaminated sample and the resources available.

#### 5.4.2 Conclusion

- All the treatment types used resulted in over $70\%$ reduction of tritium activity with Ar purge at $200\,\mathrm{cm}^3/\mathrm{min}$ giving the highest percentage.
- Isothermal heating slightly enhances the isotopic exchange capacity because it induces evaporation making tritiated water readily accessible for exchange.
- The tritium concentration in the gas phase of the closed system is a function of initial concentration, soil volume and the mass transfer coefficient.
- For the small cultivation contaminated soil sample, Argon purge will be used for decontamination.

### References (Chapter 5)

[1] P.E. Warwick et al., Analytica Chimica Acta 676 (2010) 93-102.
[2] Bonnett et al., FST, 54 (2008), 1, 209-214.
[3] C.E. Murphy Health Physics, 82 (2002), 615-625.
[4] T. Katsumi, Soil Science and Plant Nutrition (2015), 61, 22-29.
[5] F. Gu et al, Bull Environ. Contam. Toxicol. 109, 651-658 (2022).
[6] Jackson et al, 2013.
[7] Sakharovskii et al., At. Energy 85, 462-467 (1998).
[8] A. Taguchi et al., FST, 60 (2011), 1395-1398.
[9] D. Prakash et al., Micro. Biol. 6(4) (2013), 349-360.
[10] de Amesti et al., Water Resources Research, 56 (2020).
[11] Kondo et al., Journal of Applied Meteorology, 31 (1992), 3, 304-312.
[12] T.L. Bergman, A.S. Lavine, F.P. Incropera, D.P. DeWitt, Fundamentals of Heat and Mass Transfer, 7th Edition, Wiley, 2011.
[13] F. Kreith, J.F. Kreider, Principles of Heat Transfer, 6th Edition, Brooks/Cole Publishing, 2001.

---

## Chapter 6: General Summary

### 6.1 Highlights

In **chapter 2**, the IEC parameter was evaluated for peat and vermiculite. This parameter enhances the understanding of the rate of tritium uptake and release from this soil at high concentrations. By measuring and estimating some soil properties, the tritium behavior could be predicted.

In **chapter 3**, the dominant TFWT form of tritium in Komatsuna was expected but could be of radiological importance due to mode of its consumption. Largely eaten in its raw state, nonhuman biota has a larger risk to tritium exposure due to the lack of food treatment prior to consumption. The high NE-OBT observed was unusual and needs further investigation.

**Chapter 4** highlighted the difficulty of tritium exposure experiments in closed spaces as against real field conditions. However, it gives a good approximation to understanding tritium uptake in food crops. Though OBT concentrations followed general literature patterns, TFWT in tomato fruits differed. A significant amount of tritium is lost due to evaporation and about $6.5\%$ is taken up by the plant.

**Chapter 5** described simple and readily available logistics for decontaminating a laboratory scale spent soil. Gas purging at high flow rate with or without isotope exchange with tritium-free water and heating removes a substantial amount of tritium in a relatively short time.

### 6.2 Conclusion

The forms of tritium that exist in plants grown in tritium contaminated peat soil was evaluated. Initially, soil characterization enhanced the physicochemical behavior understanding of this highly mobile solute in the solid phase. The determined isotope exchange capacity was generally low as compared to other materials even after 29-days intrusiveness. This indicated peat and vermiculite as material has a low affinity for tritium. Local weather conditions could be a major determinant of tritium retention but was not evaluated extensively in this work.

*[Figure 6.1]* A simple box model showing tritium uptake predominantly via the atmosphere rather than the soil.

**In conclusion:**

- Tritium behavior in soil is dependent on soil physical parameters such as moisture, surface area and size distribution.
- The IEC is independent of the physically adsorbed water. Structural and chemically adsorbed water determine the IEC of peat and soil.
- Tritium Isotopic Exchange occurs faster in peat soil than vermiculite.
- OBT was formed in peat soil during immersion. Though very small, the photosynthetic theory of OBT formation could not be the only route.
- TFWT still remains the dominant fraction in plants.

### 6.3 Future work

The proportion of NE-OBT in Komatsuna is so high compared to general trends. However, most of the related experiments used environment-level low tritium concentrations and mostly under acute exposure conditions. The high concentration fusion reactor conditions need further investigations. There is the need to re-evaluate NE-OBT levels in Komatsuna at high tritium concentrations to validate the experiment.

The use of Imaging plate technique to detect and quantify surface tritium concentrations in leaves could be valuable. Since TFWT is generally of less interest to radioecologists, the need to measure surface tritium distributions rapidly and accurately will contribute to robust mass balance calculations.

The role of soil microorganisms in soil OBT formation needs investigation. The hypothesis to validate that OBT is not only formed during photosynthesis will open interesting OBT dynamics in non-photosynthetic plants.

---

## Appendix

### A) Derivation of the Hydraulic conductivity ($K_s$) equation

The gradient of solute flow is given as

$$
G = \frac{H_1 - H_2}{z_2 - z_1} \tag{A.1}
$$

From Darcy's law, the flux ($J_w$) is proportional to the rate of falling head ($b$)

$$
J_w = \frac{db}{dt} \tag{A.2}
$$

In head terms, this is dependent on the hydrostatic pressure ($b + L$) exerted by the head

$$
J_w = -\frac{K_s}{L}(b + L) \tag{A.3}
$$

$$
\frac{db}{b + L} = -\frac{K_s}{L} dt \tag{A.4}
$$

By integrating both sides and resolving

$$
\int_{b_0}^{b_1}\frac{db}{b + L} = \ln(b + L)\Big|_{b_0}^{b_1} = \ln\frac{b_1 + L}{b_0 + L} \tag{A.5}
$$

$$
-\int_0^{t_1}\frac{K_s}{L}dt = -\frac{K_s}{L}\int_0^{t_1}dt = -\frac{K_s t_1}{L} \tag{A.6}
$$

$$
K_s = \frac{L}{t_1}\ln\frac{b_0 + L}{b_1 + L} \tag{A.7}