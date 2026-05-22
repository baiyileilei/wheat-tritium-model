# Development and validation of a dynamical atmosphere–vegetation–soil HTO transport and OBT formation model

**Masakazu Ota\*, Haruyasu Nagai**

*Research Group for Environmental Science, Division of Environment and Radiation, Nuclear Science and Engineering Directorate, Japan Atomic Energy Agency, Japan*

## ARTICLE INFO

**Article history:** Received 25 August 2010; Received in revised form 13 April 2011; Accepted 21 May 2011; Available online 12 June 2011

**Keywords:** HTO; TFWT; OBT; Transpiration; Photosynthesis; Translocation

## ABSTRACT

A numerical model simulating transport of tritiated water (HTO) in atmosphere-soil-vegetation system, and, accumulation of organically bound tritium (OBT) in vegetative leaves was developed. Characteristic of the model is, for calculating tritium transport, it incorporates a dynamical atmosphere-soil-vegetation model (SOLVEG-II) that calculates transport of heat and water, and, exchange of $\mathrm{CO}_2$. The processes included for calculating tissue free water tritium (TFWT) in leaves are HTO exchange between canopy air and leaf cellular water, root uptake of aqueous HTO in soil, photosynthetic assimilation of TFWT into OBT, and, TFWT formation from OBT through respiration. Tritium fluxes at the last two processes are input to a carbohydrate compartment model in leaves that calculates OBT translocation from leaves and allocation in them, by using photosynthesis and respiration rate in leaves. The developed model was then validated through a simulation of an existing experiment of acute exposure of grape plants to atmospheric HTO. Calculated TFWT concentration in leaves increased soon after the start of HTO exposure, reaching to equilibrium with the atmospheric HTO within a few hours, and then rapidly decreased after the end of the exposure. Calculated non-exchangeable OBT amount in leaves linearly increased during the exposure, and after the exposure, rapidly decreased in daytime, and, moderately nighttime. These variations in the calculated TFWT concentrations and OBT amounts, each mainly controlled by HTO exchange between canopy air and leaf cellular water and by carbohydrates translocation from leaves, fairly agreed with the observations within average errors of a factor of two.

© 2011 Elsevier Ltd. All rights reserved.

## 1. Introduction

Among the collective doses from the radioactivity released from nuclear facilities to the environment, dose from tritium is estimated to be the second largest, next to that from radiocarbon (UNSCEAR, 2000). Tritium inventory in a future nuclear fusion plant accounts for as much as $1\,\mathrm{kg}$, comparable to the present tritium inventory in the globe (Boyer et al., 2009; ITER Joint Central Team et al., 1998). Release of tritium from a fusion plant under a normal operation is estimated to be $1\,\mathrm{g}\,\mathrm{y}^{-1}$, which is more than thousand times that from a nuclear fission power plant of 1000 MW level, a major power plant in the present (Okada and Momoshima, 1993). As a result, collective dose from tritium can increase significantly in the future, and therefore precise safe assessment for tritium release has been required (Barry et al., 1999; Bartels, 1991; Murphy, 1991; Raskob and Barry, 1997).

Main chemical forms of tritium released from nuclear facilities are tritiated hydrogen (HT) and tritiated water (HTO) for nuclear fission and fuel reprocessing plants, and HT for a fusion plant (Okada and Momoshima, 1993). After release into the natural environment, HTO can be organically bound (OBT) through photosynthetic hydrogen assimilation in plant. HTO and OBT can contribute to doses mainly through ingestion pathway (Boyer et al., 2009; Diabaté and Strack, 1993; Galeriu et al., 2007). Since HTO and OBT easily assimilates in human tissues, dose conversion coefficient for HTO is four-order of magnitude larger than that for HT, and, dose conversion coefficient for OBT is further two times larger than that of HTO (ICRP, 1995). Contribution of OBT can, therefore, dominate the doses from tritium (Barry et al., 1999; Diabaté and Strack, 1993; Gulden and Raskob, 1992; Raskob and Barry, 1997).

*[Figure 1]* Schematic of tritium transfer in the natural environment, and, the fate of tritium in vegetations.

Fig. 1 shows a schematic of tritium transfer in the environment after HT and HTO release into the atmosphere. Both HT and HTO disperse in the atmosphere, and after that, the latter directly enters into plants via stomata (transpiration), or, to soil through dry or wet deposition (Boyer et al., 2009; Brudenell et al., 1997; Taschner et al., 1997). Although HT is much less toxic than HTO, HT can contribute to doses through the ingestion of HTO and OBT since HT diffused into soil is rapidly oxidized to HTO by soil microorganisms ubiquitously contained in surface soils (Komuro et al., 2002; Noguchi et al., 1995; Ota et al., 2007; Taschner et al., 1988; Velarde and Perlado, 2003). These HTO in soils evaporate into the atmosphere (re-emission), or, moves in soil through diffusion and advection (Barry et al., 1999; Brudenell et al., 1997; Taschner et al., 1997; Yamazawa, 2001). Aqueous HTO near surface is taken up by plants root, and then transpired into the atmosphere, or assimilate as OBT in leaves (Barry et al., 1999; Diabaté and Strack, 1993; Okada and Momoshima, 1993).

The importance and status of modeling of these tritium transfer processes for safe assessments have been summarized by Murphy (1991) and by Raskob and Barry (1997). They rank uptake of HTO and successive OBT formation in vegetation as very important processes to be modeled precisely, nevertheless the status of modeling of these processes is still low (Boyer et al., 2009; Strack et al., 1995).

Recently, knowledge on tissue free water tritium (TFWT) variation and OBT formation after an exposure of vegetations to atmospheric HTO has been progressed for several foodstuffs (Atarashi et al., 1998; Belot et al., 1979; Brudenell et al., 1997; Choi et al., 2002, 2005, 2007; Diabaté and Strack, 1997; Guenot and Belot, 1984; McFarlane, 1976, 1978; Sweet et al., 1983). Direct exchange of HTO through stomata is rapid, and TFWT concentration in leaves changes with retention times of 1 h or less, affected by stomata resistance (Atarashi et al., 1998; Belot et al., 1979; Boyer et al., 2009; Kline and Stewart, 1974). Change in TFWT concentration is therefore more rapid in daytime than in nighttime (Brudenell et al., 1997; Couchat et al., 1983; Diabaté and Strack, 1997).

TFWT in leaves becomes OBT through photosynthesis that synthesizes glucose from leaf cellular water and $\mathrm{CO}_2$. Hence, OBT formation rate in a leaf is affected by both TFWT concentration and photosynthetic $\mathrm{CO}_2$ assimilation rate (Boyer et al., 2009; Diabaté and Strack, 1993; Guenot and Belot, 1984). After formed as carbohydrates through photosynthesis, some OBT is stored in leaves and some is translocated to the other parts of the plants (Fig. 1). The rate of OBT translocation depends on the growing stages of the plant, age of the leaves, etc. Mature leaves act as a source organism exporting photosynthesized carbohydrates to sink parts (Fondy and Geiger, 1982; Servaites and Geiger, 1974; Taiz and Zeiger, 2002). On the other hand, newly formed leaves spend synthesized carbohydrates for their own growths, and also import carbohydrates from the source leaves. Demands for photosynthesis from sink parts, such as roots, ears, as well as young leaves, are high when they are actively growing (Choi et al., 2002, 2005, 2007; Taiz and Zeiger, 2002).

Organically bound tritium is also formed through hydrogen exchange reaction between $^{1}\mathrm{H}$ or $^{3}\mathrm{H}$ atoms in tissue free water and carbohydrates (Diabaté and Strack, 1993; Guenot and Belot, 1984). Hydrogen in N–H, O–H, and S–H bonds in organic compounds are unstable, and hence easily dissociates, replaced by H atoms in cellular water (Boyer et al., 2009; Diabaté and Strack, 1993). Hydrogen bonded to carbon as C–H, on the other hand, is stable, and is non-exchangeable. These exchange reaction is rapid, having a timescale of within a few seconds (Diabaté and Strack, 1993). Therefore exchangeable OBT is removed from organic compounds while organic compounds are transported within vegetations through phloem translocation, or removed through food chains and cooking process (Boyer et al., 2009; Diabaté and Strack, 1993; Guenot and Belot, 1984). Dose assessment concerning OBT is, therefore, generally done only for non-exchangeable OBT, and hence tritium transfer models for safe assessments should precisely assess non-exchangeable OBT in plants.

In the natural environment these TFWT retention and OBT formation rate dynamically changes, affected by many environmental factors. A simple steady-state compartment model, therefore, is not adequate to precisely assess OBT amount in vegetations (Boyer et al., 2009; Raskob, 2002; Strack et al., 1995). However, such a dynamical tritium transfer model that includes both the above-addressed HTO transport and OBT formation is rare. The objective of the present study is, therefore, to develop a dynamical OBT formation model by cooperating physical HTO transfer in the atmosphere and soil, and, physiological OBT formation in vegetations. For this objective, we modeled HTO exchange between canopy air and leaf cellular water, root uptake of HTO due to transpiration of water, photosynthetic TFWT assimilation into OBT, and, TFWT production from OBT through respiration. Furthermore, a carbohydrate allocation model in a leaf is developed, calculating translocation of photosynthesized OBT in carbohydrates in leaves. To dynamically evaluate processes related these tritium transfers and exchanges within atmosphere, vegetation and soil, these models are incorporated with SOLVEG-II, an atmosphere-soil-vegetation heat and water transport, and $\mathrm{CO}_2$ exchange model (Nagai, 2005; Yamazawa, 2001; Yamazawa and Nagai, 1997). The developed model was then validated with observations of TFWT concentration and non-exchangeable OBT amount in leaves during and after an acute exposure of grape plants to atmospheric HTO vapor (Guenot, 1984; Guenot and Belot, 1984).

## 2. Model description

### 2.1. Atmospheric model

The atmospheric HTO vapor transport is expressed by a diffusion equation, similar to the atmospheric $\mathrm{CO}_2$ transport in SOLVEG-II (Nagai, 2005), as:

$$
\frac{\partial\chi_a}{\partial t} = \frac{\partial}{\partial z} K\frac{\partial\chi_a}{\partial z} + aE_{\mathrm{stom}} \tag{1}
$$

where the vertical turbulent diffusivity $K$ is calculated by a turbulent closure model (Yamada, 1981), and, the last term $aE_{\mathrm{stom}}$ expresses HTO exchange between canopy air and leaf, termed as a volumetric sink or source of HTO.

### 2.2. Soil model

Original soil HTO sub-model of SOLVEG-II includes diffusion, advection, and evaporation/condensation for aqueous and gaseous HTO in soil (Yamazawa, 2001). For this model, root uptake $\hat{e}_r$ of aqueous HTO due to transpiration is newly added in the present study. Hence equation for aqueous HTO is expressed as:

$$
\frac{\partial\eta_s\chi_{sw}}{\partial t} = -\frac{1}{\rho_w}\frac{\partial E_w\chi_{sw}}{\partial z} +\frac{\partial}{\partial z}\bigg(D_{sw}\frac{\partial\chi_{sw}}{\partial z}\bigg) - \hat{e}_b - \hat{e}_r \tag{2}
$$

where the first and second terms in the right-hand side expresses advection and diffusion of HTO, and the last two terms express evaporation/condensation and root uptake as volume sinks or sources. Soil water content $\eta_s$ and vertical water flux $E_w$ are calculated in the soil sub-model of SOLVEG-II, for which the equation for liquid water transport is a classical Richard's type (Yamazawa and Nagai, 1997). The evaporation/condensation in Eq. (2) is expressed as:

$$
\hat{e}_b = \frac{1}{r_b}\bigg\{\chi_{sw}q_{\mathrm{sat}}(T_s)\frac{\rho}{\rho_w} - \chi_{sa}\bigg\} \tag{3}
$$

where the evaporation resistance $r_b$ is an empirically-determined function of $\eta_s$ (Kondo and Saigusa, 1994). Root uptake is expressed by:

$$
\hat{e}_r = \frac{\chi_{sw}}{\rho_w} R_r\int_{z_0}^{z_{st}}E_{\mathrm{tra}}(z)dz \tag{4}
$$

where the transpired water flux $E_{\mathrm{tra}}$ is calculated in the vegetation $\mathrm{CO}_2$ sub-model, and will be discussed in Section 2.3.1.

Transfer of HTO vapor in soil is expressed by a diffusion equation, and is linked with the above aqueous HTO transfer through $\hat{e}_b$ as:

$$
\frac{\partial\{(\eta_{\mathrm{sat}} - \eta_s)\chi_{sa}\}}{\partial t} = \frac{\partial}{\partial z}\bigg(D_{sa}\frac{\partial\chi_{sa}}{\partial z}\bigg) + \hat{e}_b \tag{5}
$$

where the effective diffusivity $D_{sa}$ for HTO vapor is calculated with $\eta_s$ and $\eta_{\mathrm{sat}}$ (Yamazawa, 2001).

### 2.3. Vegetation model

#### 2.3.1. Transpiration of water and exchange of $\mathrm{CO}_2$

In this study, leaf-atmosphere HTO exchange and formation of OBT were modeled with conductance for transpiration and photosynthetic $\mathrm{CO}_2$ assimilation rate in leaves etc., variables calculated in the $\mathrm{CO}_2$ sub-model of SOLVEG-II as follows (Nagai, 2005). Using formulations proposed by Farquhar et al. (1980), net $\mathrm{CO}_2$ assimilation rate $A_n$ in a leaf is calculated as:

$$
A_n = \min(w_{\mathrm{PAR}}, w_{\mathrm{RUB}}, w_{\mathrm{EXP}}) - R_d \tag{6}
$$

which means $A_n$ is determined as the minimum of three limiting rate: the limitation resulting from the absorbed photosynthetic active radiation, from the efficiency of the photosynthetic enzyme Rubisco, and, from the capacity of the photosynthetic products export. These limiting rates $w_{\mathrm{PAR}}, w_{\mathrm{RUB}}, w_{\mathrm{EXP}}$ are calculated from the light intensity, leaf temperature $T_c$ etc. (Farquhar et al., 1980). Leaf respiration rate $R_d$ in Eq. (6) is calculated by:

$$
R_d = f_d V_m \tag{7}
$$

where the factor $f_d = 0.015$ for C3 plants and $f_d = 0.025$ for C4 plants, and $V_m$ is the maximum catalytic capacity of Rubisco primarily determined by $T_c$ (Nagai, 2005).

The above determined $A_n$ is used to calculate the stomata resistance, by using a relationship proposed by Leuning (1995):

$$
\frac{1}{r_s} = m\frac{A_n}{c_c}\frac{e_c}{e_{\mathrm{sat}}(T_c)}p_a + g_{s,\mathrm{min}} \tag{8}
$$

Then $r_s^*$ obtained is converted to the stomata resistance $r_s$ as,

$$
r_s = \left(\frac{p_a}{RT_c}\right)r_s^* \tag{9}
$$

The transpiration flux $E_{\mathrm{tra}}$ appearing in Eq. (4), for water is calculated from $r_s$ and vapor pressure deficit between the atmosphere and leaf interior, as:

$$
E_{\mathrm{tra}} = \rho\frac{1}{r_a + r_s}(q_{\mathrm{sat}}(T_c) - q_a) \tag{10}
$$

where $r_a$ is the leaf-surface boundary layer resistance calculated from horizontal and vertical wind component $(u, v)$, and aerodynamic characteristics of the leaf as:

$$
r_a = \left(C_d\sqrt{u^2 + v^2}\right)^{-1} \tag{11}
$$

#### 2.3.2. Tritiated water budget in leaves

Change in TFWT concentration $\chi_v$ in a unit leaf area is expressed as:

$$
\frac{\partial\eta_v\chi_v}{\partial t} = E_{\mathrm{stom}} + E_{\mathrm{root}} + E_{\mathrm{phot}} + E_{\mathrm{res}} \tag{12}
$$

where terms in the right-hand side respectively expresses HTO flux in a unit leaf area for HTO exchange between canopy air and leaf cellular water, root uptake of HTO due to transpiration of water, TFWT assimilation to OBT through photosynthesis, and, TFWT production by respiration. Each flux is defined to be positive when it increases $\chi_v$. Hydrogen exchange process is not included in Eq. (12), since flux from exchange reaction should be much smaller than the fluxes in the right-hand side of Eq. (12). This estimation is deduced from the results that $E_{\mathrm{phot}}$ is two to three orders of magnitudes smaller than $E_{\mathrm{stom}}$ throughout the calculation in this study. This confirms that HTO flux from the exchange reaction does not affect TFWT concentration in leaves, even if all of the tritium fixed to the organic compounds is again released to tissue free water through the exchange reaction. This estimation is conservative because only a small fraction of the total hydrogen in carbohydrates is exchangeable, which will be discussed in section 2.4.

Exchange of HTO is expressed by:

$$
E_{\mathrm{stom}} = \rho\frac{1}{r_a + r_s}\left\{\frac{\chi_a}{\rho} - q_{\mathrm{sat}}(T_c)\frac{\chi_v}{\rho_w}\right\} \tag{13}
$$

where $r_a$ and $r_s$ are calculated in the vegetation $\mathrm{CO}_2$ sub-model. This $E_{\mathrm{stom}}$ is introduced into the atmospheric HTO transport in Eq. (1). $E_{\mathrm{root}}$ is expressed by:

$$
E_{\mathrm{root}} = \int_{z_{rb}}^{z_{rt}}\hat{e}_r R_{er}(z_s, z)\mathrm{d}z_s \tag{14}
$$

where $\hat{e}_r$ is determined with Eq. (4).

Photosynthetic TFWT assimilation flux $E_{\mathrm{phot}}$ is calculated with $\chi_v$ and $A_n$. A photosynthesis reaction is expressed as $6\mathrm{CO}_2 + 6\mathrm{H}_2\mathrm{O} \rightarrow \mathrm{C}_6\mathrm{H}_{12}\mathrm{O}_6 + 6\mathrm{O}_2$, in which 1-mol of $\mathrm{CO}_2$ reacts with 1-mol of $\mathrm{H}_2\mathrm{O}$. Therefore, $E_{\mathrm{phot}}$ can be expressed as:

$$
E_{\mathrm{phot}} = -\frac{\chi_v}{\rho_w} m_w f_{An} A_n \tag{15}
$$

where $f_{An} = 0.78$ is an isotopic discrimination factor for $^{3}\mathrm{H}$ at photosynthesis reaction due to a cleavage of more stable $^{3}\mathrm{H–O}$ bond in tritiated water than $^{1}\mathrm{H–O}$ bond (Guenot and Belot, 1984; Diabaté and Strack, 1993; McFarlane, 1976).

Production of TFWT from photosynthates through respiration is calculated with $R_d$. A respiration reaction is expressed as $\mathrm{C}_6\mathrm{H}_{12}\mathrm{O}_6 + 6\mathrm{O}_2 \rightarrow 6\mathrm{CO}_2 + 6\mathrm{H}_2\mathrm{O}$, where the production of 1-mol $\mathrm{CO}_2$ accompanies with that of 1-mol $\mathrm{H}_2\mathrm{O}$, and decomposition of $1/6$-mol of glucose. Hence, $E_{\mathrm{res}}$ is expressed as:

$$
E_{\mathrm{res}} = S_{\mathrm{int}}\frac{1}{6}m_g R_d \tag{16}
$$

where $S_{\mathrm{int}}$ is the OBT amount in an intermediate carbohydrate pool, described in Section 2.4.

### 2.4. Carbohydrate translocation model

The carbohydrate translocation model is based on an observation of carbohydrate allocation and translocation for a source leaf of sugar beet, reported by Fondy and Geiger (1982). They observed that during daytime photosynthates firstly enter to an intermediate pool, and allocated into sucrose, starch, or structural compounds, among which sucrose is translocated to the other sink parts via phloem transport. During nighttime, intermediates are either decomposed into $\mathrm{CO}_2$ and $\mathrm{H}_2\mathrm{O}$ through respiration, or allocated to sucrose pool. To compensate nighttime sucrose translocation, starch accumulated daytime is decomposed to intermediates. Servaites and Geiger (1974) also reported a linear relationship between translocation rate of sucrose and photosynthetic $\mathrm{CO}_2$ assimilation rate.

Based upon these observations we developed a carbohydrate allocation model in a leaf, shown in Fig. 2. The model has four carbohydrate pools, and carbohydrate fluxes between these pools are calculated as a proportional function of $A_n$ for daytime, and that of $R_d$ for nighttime, where the proportional coefficients are determined from the observations by Fondy and Geiger (1982).

*[Figure 2]* A carbohydrate allocation and translocation model developed in the present study. Coefficients multiplied to carbohydrate fluxes, $E_{An}$ and $E_{Rd}$ are determined from the observations by Fondo and Geiger (1982).

This compartment model is connected to the $\mathrm{CO}_2$ and OBT assimilation in leaves, through carbohydrate and OBT fluxes into or out of the intermediate pool (Fig. 2). Assuming that the carbohydrate fully consists of $\mathrm{C}_6\mathrm{H}_{12}\mathrm{O}_6$ molecules, in- and output carbohydrate fluxes for the intermediate pool are calculated from $A_n$ or $R_d$ as:

$$
E_{An} = \frac{1}{6}m_g A_n \quad (\mathrm{kg}\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}), \text{ for daytime carbohydrate input} \tag{17}
$$

and

$$
E_{Rd} = \frac{1}{6}m_g R_d \quad (\mathrm{kg}\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}), \text{ for nighttime carbohydrate output} \tag{18}
$$

where the factor $1/6$ is the molar ratio between $\mathrm{CO}_2$ and $\mathrm{C}_6\mathrm{H}_{12}\mathrm{O}_6$ in photosynthesis and respiration reaction. For tritium, in- and output OBT fluxes are respectively expressed by Eq. (15) and Eq. (16). Then the OBT fluxes $(\mathrm{Bq}\,\mathrm{m}^{-2}\,\mathrm{s}^{-1})$ between the pools are calculated as a product of the carbohydrate flux $(\mathrm{kg}\,\mathrm{m}^{-2}\,\mathrm{s}^{-1})$ and OBT amount $(\mathrm{Bq}\,\mathrm{kg}^{-1})$. For example, daytime OBT flux from intermediate to sucrose pool is expressed as: $S_{\mathrm{int}} \times 0.48 \times E_{An}$.

Amount of OBT $Q_{OBT}$ $(\mathrm{Bq}\,\mathrm{kg}^{-1})$ by carbohydrate weight in a leaf is calculated as follow. Assuming that a leaf consists of free water and dry matter, and dry matter is entirely made up with $\mathrm{C}_6\mathrm{H}_{12}\mathrm{O}_6$, then the weight of carbohydrates $(W_{\mathrm{int}}, W_{\mathrm{suc}}, W_{\mathrm{sta}}, W_{\mathrm{str}})$ in each pool can be calculated by integrating net carbohydrate flux in each pool. $Q_{OBT}$ is then calculated by summarizing OBT and carbohydrate amount as:

$$
Q_{OBT} = \frac{\sum S_i W_i}{\sum W_i} = \frac{S_{\mathrm{int}}W_{\mathrm{int}} + S_{\mathrm{suc}}W_{\mathrm{suc}} + S_{\mathrm{sta}}W_{\mathrm{sta}} + S_{\mathrm{str}}W_{\mathrm{str}}}{W_{\mathrm{int}} + W_{\mathrm{suc}} + W_{\mathrm{sta}} + W_{\mathrm{str}}} \tag{19}
$$

Non-exchangeable OBT amount is calculated from $Q_{OBT}$ and fraction of non-exchangeable hydrogen in organic compounds. Theoretical values of the fraction of the non-exchangeable hydrogen to the total hydrogen (sum of non-exchangeable and exchangeable hydrogen) in each carbohydrate are given by Diabaté and Strack (1993) as: 0.62 for intermediate (glucose), 0.64 for sucrose, 0.72 for starch, and 0.70 for structural (cellulose). Guenot (1984) and Guenot and Belot (1984) observed the non-exchangeable fraction $f_{\mathrm{nex}} = 0.79$ for leaves of grape plants and potato plants. We adopted the latter as a first trial for the calculation. Then the non-exchangeable OBT amount $Q_{OBT-N}$ by carbohydrate weight is calculated as:

$$
Q_{OBT-N} = f_{\mathrm{nex}} Q_{OBT} \tag{20}
$$

## 3. Model validation

### 3.1. HTO exposure experiment

To validate the model, calculation simulating a field experiment on a short term grape plants exposure to HTO vapor (Guenot, 1984; Guenot and Belot, 1984), was performed. The exposures were carried out in 9:00–13:00 June 30 and July 1 in 1982 at a grape plants field in Cadarache in south France ($43^{\circ}36^{\prime}43^{\prime \prime}\mathrm{N}, 05^{\circ}53^{\prime}19^{\prime \prime}\mathrm{E}$, c.a. $300\,\mathrm{m}$ above the sea level). Three wine grape plants (vitis vinifera) at flowering stage were exposed to HTO vapor containing air over the $4\,\mathrm{h}$ in a field-exposure chamber, as schematically drawn in Fig. 3.

The chamber was a tunnel of $2\text{-}\mathrm{m}$ long and $1\text{-}\mathrm{m}$ diameter, and covered with a vinyl film. An HTO generator that continuously evaporates tritiated water, and, an air blower were connected to the chamber. Generated HTO vapor was diluted in an air stream of $1500\,\mathrm{m}^3\,\mathrm{h}^{-1}$, entering the chamber at the one end, and escaping at the other end. This air stream exchanged air in the chamber with a time constant of $4\,\mathrm{s}$, and ensured a sufficient air-mixing inside the chamber. During the exposure, therefore, specific activity of HTO in the water vapor surrounding the leaves in the chamber was spatially uniform at a constant value of $9.93 \times 10^3\,\mathrm{Bq}\,\mathrm{g}^{-1}$. To prevent the HTO exchange between the air in the chamber and the air in the underlying soil, the soil surface was covered with a vinyl film during the exposure.

At the end of the exposure, vinyl-films covering the chamber and the soil surface were removed, allowing free circulation of the ambient air. The grape plants were thereafter grown under the ambient condition. During and after the exposure leaves were cropped, and TFWT concentration $\chi_v$ and non-exchangeable OBT amount $Q_{OBT-N}$ were measured.

### 3.2. Calculation conditions simulating the experiments

#### 3.2.1. Grid definitions

Fig. 3 also shows grid definitions in the calculation. Atmospheric layer of $12\,\mathrm{m}$ height above the ground has a C3-crop canopy with a crown existing over $0.3 - 1.0\,\mathrm{m}$ height with a leaf area density of $4.0\,\mathrm{m}^2\,\mathrm{m}^{-3}$. Loamy sand soil underlies in $0 - 2.0\,\mathrm{m}$ depth. The atmosphere including canopy, and the soil were respectively divided into ten and seven layers.

*[Figure 3]* Schematics of the field experiment (Guenot, 1984; Guenot and Belot, 1984), and, grid definition in the model.

#### 3.2.2. Conditions simulating the chamber and the vinyl-film covering

During the exposure, trees inside the chamber were HTO contaminated, while trees outside the chamber were not. Hence, soon after the exposure, HTO vapor in the air surrounding the HTO-exposed trees should have been blown out in the ambient air stream, resulting in a sudden decrease of the HTO concentration in the air surrounding the leaves. To simulate this phenomenon in the calculation, specific activity of the HTO in the atmosphere, including canopy, were set to be temporally rectangle; at a constant background level before and after the exposure, and, at a constant value of $9.93 \times 10^3\,\mathrm{Bq}\,\mathrm{g}^{-1}$ during the 4-h exposure.

To simulate the vinyl-film covering of the soil surface, aqueous and gaseous HTO concentration in soil was set to be at a background HTO level throughout the calculation.

To assume the above calculation conditions, background HTO concentration in the atmosphere, a missing datum, was needed. We estimated it from the TFWT observation results. TFWT concentration $\chi_v$ changes rapidly with a retention time of 1 h or less in daytime (Atarashi et al., 1998; Belot et al., 1979; Brudenell et al., 1997; Couchat et al., 1983; Diabaté and Strack, 1997; Kline and Stewart, 1974). We then assumed $\chi_v$ measured at three days after the exposure were in an equilibrium with the background HTO concentration in the atmosphere. Then the background specific HTO activity in the atmosphere and vegetation were determined to be $6.7 \times 10^{-1}\,\mathrm{Bq}\,\mathrm{g}^{-1}$, an average $\chi_v$ measured over 80–116 h (see Fig. 6(a)).

#### 3.2.3. Initial conditions

Above determined background HTO level of $6.7 \times 10^{-1}\,\mathrm{Bq}\,\mathrm{g}^{-1}$ was also used as the initial values of atmosphere, vegetation and soil HTO concentrations.

Initial values of the carbohydrate amount $W_i$ in each carbohydrate pool were determined from leaf water volume $\eta_v = 1.54 \times 10^{-4}\,\mathrm{m}^3\,\mathrm{m}^{-2}$, a value measured for the experimental grape plant (Guenot, 1984). Assuming that a leaf consists of free water and dry matter, and, dry matter fully consists of carbohydrates, then the initial value of the total carbohydrate weight $\sum W_i$ in Eq. (19) was calculated as:

$$
\sum W_i = \frac{1 - \theta_v}{\theta_v}\rho_w\eta_v = 0.963\,\mathrm{kg}\,\mathrm{m}^{-2} \tag{21}
$$

where leaf water content $\theta_v$ by weight was also estimated to be $60\%$ from the observation on the water content in pear leaves, including an error of $\pm 8\%$ derived from seasonal and daily variations in it (Ackley, 1954). Having obtained the initial $\sum W_i$, initial carbohydrate amount in the structural carbon pool was calculated by $W_{\mathrm{str}} = 0.95 \times \sum W_i$, where the factor 0.95 is the relative amount of the structural carbon to the total carbon in a leaf (Fondy and Geiger, 1982). Then the residual carbohydrates, $0.05 \times \sum W_i$, calculates the initial value of the carbohydrate in the intermediate pool of $0.03 \times \sum W_i$, starch pool of $0.0175 \times \sum W_i$, and, sucrose pool of $0.0025 \times \sum W_i$. Factors multiplied to $\sum W_i$ were determined so that changes in $W_i$ in each pool were almost equal at a twofold increase after the five-day calculation in the present study.

#### 3.2.4. Input meteorological data

One-hour interval meteorological data, observed at the nearest meteorological observatory (Aix Les Milles FAFB, $43^{\circ}50^{\prime}00^{\prime \prime}\mathrm{N}$, $05^{\circ}36^{\prime}70^{\prime \prime}\mathrm{E}$, 111 m above sea level, and $40\,\mathrm{km}$ apart from the experimental site) was used as input data at the 8–12 m height atmosphere (Fig. 3). No observations on solar and long-wave radiations were available, hence they were estimated by using empirical formulas reported by Kondo and Miura (1985) from the observations on dew point and air temperature at Aix Les Milles FAFB.

In the experiment, during the exposure air flow in the chamber was maintained at a constant value of c.a. $0.5\,\mathrm{m}\,\mathrm{s}^{-1}$, calculated as $1500\,\mathrm{m}^3\,\mathrm{h}^{-1} / 0.7\,\mathrm{m}^2 = 0.5\,\mathrm{m}\,\mathrm{s}^{-1}$, where $1500\,\mathrm{m}^3\,\mathrm{h}^{-1}$ is the air blow inside the chamber and $0.7\,\mathrm{m}^2$ is the sectional area of the chamber. To simulate this constant air flow in the chamber, wind velocity of $3.0 - 3.5\,\mathrm{m}\,\mathrm{s}^{-1}$ was assumed for the input data during the 4-h exposure period, calculating wind velocity of c.a. $0.5\,\mathrm{m}\,\mathrm{s}^{-1}$ in the canopy crown.

While the experiment was duplicated at June 30 and July 1, difference in the observation results between the two experiments was small. Test calculations using the above meteorological data set also showed that difference in the calculation results was small, between the calculation assumed an exposure over $9{:}00 - 13{:}00$ in June 30 and that over $9{:}00 - 13{:}00$ in July 1. Hereafter, therefore, calculation assumes an exposure over $9{:}00 - 13{:}00$ in July 1, and, the observation results of the duplicated experiments are evaluated together.

#### 3.2.5. Uncertainties in the calculation results

These estimated $\theta_v$, solar and long-wave radiations respectively contains uncertainty of $8\%$ by weight and $20\,\mathrm{W}\,\mathrm{m}^{-2}$ (Ackley, 1954; Kondo and Miura, 1985). Furthermore, during the exposure, radiations inside the chamber can have differed from the radiations outside, affected by the vinyl-film covering of the chamber. Some experimental results have shown that radiation inside greenhouses can halves compared to that outside the greenhouses (Al-Riahi et al., 1989; Kimball, 1973). To check the uncertainties in the calculation results derived from these uncertainties in the input data, we carried out sensitivity analyses.

The sensitivities of the calculation to these variables are summarized in Table 1. For both $\chi_v$ and $Q_{OBT-N}$, largest uncertainty of a factor of 1.5 derives from the uncertainty in the radiations during the 4-h exposure period. For $Q_{OBT-N}$, errors derived from uncertainty in $\theta_v$ are also large, being at a factor of 1.3.

There also exist uncertainties derived from errors in the developed models. For the $\mathrm{CO}_2$ exchange model (section 2.3.1), parameters ($m$, $V_m$, $g_{s,\mathrm{min}}$, etc.), which used in Eqs. (6)–(8), have different values by plant type (Nagai, 2004, 2005). Although parameters for generic C3-crop plant were adopted in the present study, these can differ from the ones for the experimental grape plant. Also, developed leaf carbohydrate compartment model (section 2.4) was based upon an observation on a single cultivar (sugar beet) and a single source leaf, while carbohydrate allocation and translocation in a leaf can depend on cultivar type and can have various diurnal patterns (Mullen and Koller, 1988; Taiz and Zeiger, 2002). For these reasons, calculated $A_n$, $r_s$ and $Q_{OBT-N}$ can have discrepancies from the actual ones for the experimental grape plant. Due to a limited data set of such physiological parameters for the experimental grape plant, sensitivity analysis has not done and remains as a future work.

**Table 1** Sensitivities of the calculated TFWT concentration $\chi_v$ and non-exchangeable OBT amount $Q_{OBT-N}$ to the input data and parameters having uncertainties. Values listed are the geometrical mean $G_m$ defined as the ratio of the calculation results using tuned variable to the ones using original variable.

| Variables | $\theta_v$ (Uncertainty of 8wt.%) | Solar radiation (Uncertainty $\pm 20\,\mathrm{W}\,\mathrm{m}^{-2}$) | Long-wave radiation (Uncertainty $\pm 20\,\mathrm{W}\,\mathrm{m}^{-2}$) | Solar and long-wave radiation (Halved inside greenhouse) |
|:----------|:---------------------------------:|:------------------------------------------:|:--------------------------------------------:|:-------------------------------------------------------:|
| **Uncertainties** | +8% | –8% | +20 W m⁻² | –20 W m⁻² | +20 W m⁻² | –20 W m⁻² | Halved |
| $G_m$ for $\chi_v$ | 1.00 | 1.00 | 0.98 | 1.02 | 0.98 | 1.02 | 1.54 |
| $G_m$ for $Q_{OBT-N}$ | 1.30 | 0.78 | 0.97 | 1.03 | 0.97 | 1.03 | 1.49 |

- Uncertainty of $8\mathrm{wt.}\%$ derives from the seasonal and diurnal change in $\theta_v$ for pear leaves (Ackley, 1954). $G_m$ is an average value for the whole five-day period.
- Uncertainties of the empirical formulas calculating radiations (Kondo and Miura, 1985). $G_m$ is an average value for the whole five-day period.
- Uncertainties derived from decrease in the radiations inside greenhouses (Al-Riahi et al., 1989; Kimball, 1973). $G_m$ is an average value for the 4-h exposure period.

## 4. Results and discussion

### 4.1. Tissue free water tritium in leaves

#### 4.1.1. Total conductance for transpiration during and soon after the exposure

Throughout five-day observation, no rainfall was observed and the specific humidity in ambient air was almost constant at $10\,\mathrm{g}\,\mathrm{kg}^{-1}$. Fig. 4 (a) and (b) show the time series of the wind velocity at $z = 10\,\mathrm{m}$ (input wind data), and calculated wind velocity in the crown, during the first day of the observation. In daytime, wind velocity at $z = 10\,\mathrm{m}$ was around several-meter per second, whereas wind velocities in the crown were considerably lower than that at $z = 10\,\mathrm{m}$ and is weakened with decreasing the height. This smaller wind velocity in the lower crown is caused by momentum exchange between turbulent in the air and leaves, and, also by friction with ground surface.

Fig. 4 (c) shows calculated total conductance for HTO exchange, $g_{\mathrm{total}} \equiv (r_a + r_s)^{-1}$ in Eq. (13), for leaves at different height. Leaves at lower crown have smaller $g_{\mathrm{total}}$ mainly affected by difference in leaf surface layer resistance $r_a$ across height. Although data not shown, difference in the calculated stomata resistance $r_s$ across height is small, compared to that in $r_a$. This is due to the vertically uniform calculated leaf temperature and specific humidity over the crown, variables that largely affects on $r_s$. On the other hand, smaller wind velocities at the lower crown causes larger resistance $r_a$ resulted in a smaller $g_{\mathrm{total}}$ for leaves at the lower position. During nighttime, $g_{\mathrm{total}}$ becomes an order of magnitudes smaller than $g_{\mathrm{total}}$ in daytime, because after sunset stomata closes and $r_s$ becomes much larger.

*[Figure 4]* Time series of the input wind velocity at $z = 10\,\mathrm{m}$ (a), calculated wind velocity at difference height in the crown (b), and, calculated total conductance for exchange $g_{\mathrm{total}}$ (c), for the first day of the observation period. Elapsed time $0\,\mathrm{h}$ is defined as 0:00 July 1.

#### 4.1.2. Tissue free water tritium during and soon after the exposure

Figure 5 (a) and (b) respectively show input HTO concentrations in the canopy air and HTO exchange fluxes $E_{\mathrm{stom}}$ in leaves during the first day. During this period, the other HTO fluxes in leaves, $E_{\mathrm{root}}$, $E_{\mathrm{phot}}$ and $E_{\mathrm{res}}$ are much smaller than $E_{\mathrm{stom}}$ and hence they are not shown in the figure. At the start of the exposure ($9\,\mathrm{h} \equiv 9{:}00$ July 1) $E_{\mathrm{stom}}$ shows its maximum, and then rapidly decreases, reaching three orders of magnitudes smaller than the maximum value by $12\,\mathrm{h}$. When the leaves are exposed to the ambient air at $13\,\mathrm{h}$, $E_{\mathrm{stom}}$ is minimum and then rapidly attenuated to near zero. Since changes in $g_{\mathrm{total}}$ over the daytime $9-18\,\mathrm{h}$ are small (see Fig. 4 (c)), these changes in $E_{\mathrm{stom}}$ during and soon after the exposure are caused by changes in the HTO vapor pressure deficit, expressed by terms in the parentheses in Eq. (13), between the canopy air and the leaf interior.

*[Figure 5]* Time series of the input HTO concentrations $\chi_a$ in the air in the canopy (a), calculated HTO exchange fluxes $E_{\mathrm{stom}}$ (b), and, observed and calculated TFWT concentrations $\chi_v$ (c), for the first day of the observation period. Exposure was performed over the time $9-13\,\mathrm{h}$ (shaded area).

After the start of the exposure, calculated $\chi_v$ rapidly increased, and reached to an equilibrium concentration of $3.8 \times 10^9\,\mathrm{Bq}\,\mathrm{m}^{-3}$ by $12\,\mathrm{h}$ (Fig. 5 (c)) with almost zero $E_{\mathrm{stom}}$. After the end of the exposure at $13\,\mathrm{h}$, $\chi_v$ decreased rapidly by several factors of the magnitude by the time $19\,\mathrm{h}$. These increases and decreases in $\chi_v$ during and after the exposure are faster at the leaves in the higher positions. Larger $g_{\mathrm{total}}$ in leaves at a higher position, discussed in Section 4.1.1, gave larger $E_{\mathrm{stom}}$, resulting in these faster changes in $\chi_v$. Time constant for these increase and decrease in $\chi_v$ during and after the exposure is about $0.75\,\mathrm{h}$, being comparable to, or, at the same order of the time constants measured for cabbages ($0.9\,\mathrm{h}$), grasses ($1.6\,\mathrm{h}$), or radishes ($0.4-1.3\,\mathrm{h}$) (Atarashi et al., 1998; Brudenell et al., 1997; Kline and Stewart, 1974).

Calculated $\chi_v$ fairly agreed with the observed one during the exposure, with errors between the calculation and the observation of a factor of 1.3 (Table 2). Concerning this overestimation, increase in the calculated $\chi_v$ soon after the start of the exposure seems to be slightly faster than that of the observation (time $9-11\,\mathrm{h}$). This discrepancy between the calculation and observation during the exposure is possibly attributable to variation in the leaf water volume $\eta_v$ in the cropped leaves. While the present calculation was done for leaves having a value of $\eta_v$, leaf water content can vary as much as twice even for leaves within a plant (Ackley, 1954; Aggarwal and Shinha, 1984).

#### 4.1.3. Tissue free water tritium throughout the observation period

Fig. 6 (a) compares the calculated and the observed $\chi_v$ over the five days. After the exposure, calculated $\chi_v$ decreased down to an order of $10^6\,\mathrm{Bq}\,\mathrm{m}^{-3}$, an equilibrium TFWT level with the background atmospheric concentration, by $19\,\mathrm{h}$ for the leaves at $z = 0.85\,\mathrm{m}$ and by $35\,\mathrm{h}$ for the leaves at $z = 0.4$ and $0.6\,\mathrm{m}$. This faster decrease in $\chi_v$ for the leaves at $z = 0.85\,\mathrm{m}$ is attributable to the larger $g_{\mathrm{total}}$ discussed in Section 4.1.2. After reaching the equilibrium concentration, $\chi_v$ remained on the order of the equilibrium level until the end of observation.

During nighttime $19-29\,\mathrm{h}$, change in $\chi_v$ differed between the leaves at $z = 0.85\,\mathrm{m}$ and the leaves at $z = 0.4$ or $0.6\,\mathrm{m}$ as described below. At the time $19\,\mathrm{h}$, calculated $\chi_v$ in leaves at $z = 0.4$ and $0.6\,\mathrm{m}$ are still one–two orders of magnitude larger than the equilibrium level. As a result, for these leaves, although the total conductance $g_{\mathrm{total}}$ during nighttime ($\approx 0.04\,\mathrm{cm}\,\mathrm{s}^{-1}$, see Fig. 4 (c)) is about an order of magnitude smaller than $g_{\mathrm{total}}$ in daytime ($\approx 0.5\,\mathrm{cm}\,\mathrm{s}^{-1}$), exchange flux $E_{\mathrm{stom}}$ during $19-29\,\mathrm{h}$ is larger than the other HTO fluxes. On the other hand, for leaves at $z = 0.85\,\mathrm{m}$, $E_{\mathrm{stom}}$ is smaller than the other fluxes during $19-29\,\mathrm{h}$, and flux $E_{\mathrm{res}}$ through respiration exceeded $E_{\mathrm{stom}}$, as can be seen in comparison of the fluxes in Fig. 6 (b). This large $E_{\mathrm{res}}$ is due to a larger OBT amount $S_{\mathrm{int}}$ in intermediate pool in this period, shown in Fig. 8 (a) and discussed in Section 4.2.1. Consequently, $\chi_v$ in the leaves at $z = 0.85\,\mathrm{m}$ increased during $19-29\,\mathrm{h}$, while those in the leaves at $z = 0.4$ and $0.6\,\mathrm{m}$ decreased.

After reached to the equilibrium level by $35\,\mathrm{h}$, $\chi_v$ in the leaves at $z = 0.85\,\mathrm{m}$ changed similarly with that at $z = 0.4$ and $0.6\,\mathrm{m}$. By the time $35\,\mathrm{h}$, $S_{\mathrm{int}}$ has declined near zero (Fig. 8 (a)), and thereafter $E_{\mathrm{res}}$ does not largely affect on $\chi_v$. Hence daytime HTO flux $E_{\mathrm{root}}$ by root uptake thereafter dominated HTO inputs into leaves (Fig. 6 (b)). These TFWT supplied are soon transpired, as can be seen in $E_{\mathrm{stom}}$ being comparable to $E_{\mathrm{root}}$, and thus changes in $\chi_v$ are small after the time $35\,\mathrm{h}$.

Spatial mean of the calculated $\chi_v$ fairly agreed with the observation within the errors of a factor of 2 during the period after the exposure (Table 2). However, noticeable underestimation in the calculated $\chi_v$ during $30-36\,\mathrm{h}$ exists. Possible reasons for this underestimation are the errors in the input meteorological data, or, existence of HTO transport from contaminated vascular, or both. Wind velocity, a variable largely affects $g_{\mathrm{total}}$, can have large spatial and temporal variations. Hence wind velocity at the experimental site may have differed from the input one observed at Aix Les Milles FAFB. For the second issues, several studies have reported HTO transport to the leaf cellular water from the tritium-contaminated vascular, a process not considered in the model, can occur after the exposure of vegetation to HTO (Biddulph and Cory, 1957; Couchat et al., 1983; Kline and Stewart, 1974). During nighttime $19-29\,\mathrm{h}$, leaves continue translocation of tritium-labeled carbohydrates, resulting in a contamination of phloem and a successive contamination of vascular tissues through hydrogen exchange reactions between organic compounds. In addition, since water flux in vascular due to transpiration is small in nighttime, molecular diffusion of HTO from leaf to vascular may occur, contaminating vascular. Thereby, after the time $30\,\mathrm{h}$, when the transpiration of water starts, HTO transport from vascular into leaves may have occurred.

*[Figure 6]* Time series of TFWT concentrations $\chi_v$ (a), and, HTO fluxes in leaves at a height of $0.85\,\mathrm{m}$ (b) over the five-day observation period. Shaded area indicates the period when the exposure was conducted. Mean in figure (a) is the mean of $\chi_v$ over the leaves at the three heights.

**Table 2** Geometrical mean of the ratio of the calculation to the observation for TFWT concentration $\chi_v$ and non-exchangeable OBT amount $Q_{OBT-N}$ during and after the exposure. Number of the data adopted is expressed by n.

| | During the exposure (9–13 h, n = 8) | After the exposure (13–120 h, n = 30) |
|:--|:-----------------------------------:|:-------------------------------------:|
| TFWT concentration $\chi_v$ | 1.3 | 0.5 |
| Non-exchangeable OBT amount $Q_{OBT-N}$ | 0.6 | 1.4 |

### 4.2. Carbohydrates and OBT in leaves

#### 4.2.1. Calculated carbohydrate amount

Fig. 7 shows time series of calculated carbohydrate amount $W_i$ in each carbohydrate pool for leaves at $z = 0.6\,\mathrm{m}$. Carbohydrates in structural pool increased in daytime, and, that in intermediates pool continued increase throughout five days. For both starch and sucrose pools, carbohydrate accumulated daytime is larger than the total carbohydrate exported from these pools during nighttime. As a result, both $W_{\mathrm{sta}}$ and $W_{\mathrm{suc}}$ moderately increased throughout the five-day period. After the five-day calculation, total carbohydrates $\sum W_i$ in a leaf increased by $17\%$ by weight from the initial value.

*[Figure 7]* Carbohydrate amount $W_i$ in structural pool (a), intermediates and starch (b), and, sucrose pool (c) calculated for the leaves at $z = 0.6\,\mathrm{m}$.

#### 4.2.2. Calculated OBT amount

**(1) Amount of OBT in each carbohydrate pool**

Amount of OBT by weight $S_{\mathrm{int}}$ in the intermediate pool and $S_{\mathrm{suc}}$ in the sucrose pool, shown in Fig. 8 (a), increased soon after the start of exposure. Then $S_{\mathrm{int}}$ and $S_{\mathrm{suc}}$ reached to their maximum at $13\,\mathrm{h}$ for $S_{\mathrm{int}}$ and, at $14\,\mathrm{h}$ for $S_{\mathrm{suc}}$. After that, both $S_{\mathrm{int}}$ and $S_{\mathrm{suc}}$ declined down to about half the maximum value by the sunset at $19\,\mathrm{h}$, when the photosynthesis stops. These decreases in $S_{\mathrm{int}}$ and $S_{\mathrm{suc}}$ in daytime are caused by dilution with additional input of newly formed carbohydrates into the two pools. Carbohydrates formed after the end of the exposure have smaller $S_i$ than that of the carbohydrates formed during the exposure, because $\chi_v$ decreases rapidly after the exposure. During nighttime $19-29\,\mathrm{h}$, $S_{\mathrm{int}}$ moderately decreased, and $S_{\mathrm{suc}}$ successively decreased, because of the carbohydrate inputs from starch pool that has smaller OBT amount $S_{\mathrm{sta}}$. Contrary to this, during the period after the second day, $S_{\mathrm{int}}$ and $S_{\mathrm{suc}}$ increased in nighttime, since $S_{\mathrm{sta}}$ is larger than $S_{\mathrm{int}}$ and $S_{\mathrm{suc}}$.

For the starch pool, $S_{\mathrm{sta}}$ gradually increased daytime in the first and second day and peaked at time $32\,\mathrm{h}$, at which $S_{\mathrm{int}}$ equals $S_{\mathrm{sta}}$. After that, $S_{\mathrm{sta}}$ moderately decreased in daytime, because of the dilution by carbohydrate input from the intermediate pool. For the structural pool, increase in $S_{\mathrm{str}}$ is negligibly smaller than that of other three pools because of much larger carbohydrate amount in the structural pool (Fig. 7 (a)).

**(2) Inventory of OBT in each carbohydrate pool**

Fig. 8 (b) shows temporal change in OBT inventory $(\mathrm{Bq}\,\mathrm{m}^{-2})$, defined as $W_i$ $(\mathrm{kg}\,\mathrm{m}^{-2}) \times S_i$ $(\mathrm{Bq}\,\mathrm{kg}^{-1})$, in each carbohydrate pool. Inventory of OBT in the intermediate pool is the largest among four pools, and markedly changed over the five-day period. These are attributable to the relatively large carbohydrate amount $W_{\mathrm{int}}$ (Fig. 7 (b)) and the large changes in the OBT amount $S_{\mathrm{int}}$ (Fig. 8 (a)) in the pool. On the other hand, inventory of OBT in sucrose pool is much smaller than that of the other carbohydrate pools. Although $S_{\mathrm{suc}}$ is comparable to $S_{\mathrm{int}}$ (Fig. 8 (a)), sucrose does not contribute to total OBT inventory in a leaf because of much smaller $W_{\mathrm{suc}}$ in a leaf, an order lesser than $W_{\mathrm{int}}$ and $W_{\mathrm{sta}}$ (Fig. 7).

For starch pool, OBT inventory increased in daytime $13-19\,\mathrm{h}$ and thereafter gradually decreased, exhibiting diurnal variations caused by the variation in $W_{\mathrm{sta}}$ (see Fig. 7 (b)). Inventory of OBT in the structural pool $S_{\mathrm{str}} \times W_{\mathrm{str}}$ moderately increased daytime $13-19\,\mathrm{h}$ and $30-42\,\mathrm{h}$ due to the OBT input from the intermediate pool. Then, increase in $S_{\mathrm{str}} \times W_{\mathrm{str}}$ became smaller as $S_{\mathrm{int}}$ attenuates. Finally, $S_{\mathrm{str}} \times W_{\mathrm{str}}$ remained almost unchanged three days after the exposure at a value of c.a. $6.5\,\mathrm{kBq}\,\mathrm{m}^{-2}$.

**(3) Non-exchangeable OBT**

Fig. 8 (c) compares calculated and observed non-exchangeable OBT amount $Q_{OBT-N}$ in leaves. Calculated $Q_{OBT-N}$ linearly increased soon after the start of exposure, and peaked at $13\,\mathrm{h}$ at values of $0.6-0.8\,\mathrm{MBq}\,\mathrm{kg}^{-1}$, depending on the height of the leaves. Then calculated $Q_{OBT-N}$ decreased rapidly over $13-19\,\mathrm{h}$, and moderately over $19-43\,\mathrm{h}$, and after that, changes in the calculated $Q_{OBT-N}$ were relatively small. These rapid decrease in $Q_{OBT-N}$ soon after the exposure and moderate decrease over the subsequent several-day period are consistent with the observation for leaves of rice plants and winter wheat (Choi et al., 2002; Diabaté and Strack, 1997).

Difference in the calculated $Q_{OBT-N}$ across height is attributable to the difference in OBT assimilation flux $E_{\mathrm{phot}}$ (Eq. (15)) across height, caused by vertical variation in $\chi_v$ (Fig. 5 (c)) and variation in photosynthesis rate $A_n$ (data not shown). As discussed in Section 4.1.1, $g_{\mathrm{total}}$ is larger for leaves at higher positions. Therefore, $A_n$ calculated with Eq. (6) is larger for leaves at a higher position. These vertical profile in $\chi_v$ and $A_n$ resulted in a larger OBT fixation at a higher position during the exposure.

There are some noticeable discrepancies between the calculation and the observation in that: (1) underestimation in the calculation for $Q_{OBT-N}$ peaked around $13\,\mathrm{h}$, (2) disagreement in the rapid decrease in $Q_{OBT-N}$ observed soon after the exposure (13–19 h), and, (3) systematic overestimation over $48-120\,\mathrm{h}$. As a result, calculated $Q_{OBT-N}$ underestimated the observation by $40\%$ of the magnitude during the exposure, and, overestimated by $40\%$ during the period after the exposure (Table 2).

For the discrepancy (1), probable reasons are an overvaluation of the initial carbohydrate amount in a leaf $\sum W_i$ calculated with Eq. (21), and, an underestimation of the isotope discrimination factor $f_{An}$ at photosynthesis reaction adopted in Eq. (15). Concerning the first one, the calculated $Q_{OBT-N}$ has an uncertainty of a factor of 1.3 (see Table 1). If this factor was multiplied to the calculated $Q_{OBT-N}$ at $13\,\mathrm{h}$, the highest $Q_{OBT-N} = 0.8\,\mathrm{MBq}\,\mathrm{kg}^{-1}$ at $z = 0.85\,\mathrm{m}$ and the lowest $Q_{OBT-N} = 0.6\,\mathrm{MBq}\,\mathrm{kg}^{-1}$ at $z = 0.4\,\mathrm{m}$ respectively calculates $0.8 \times 1.3 = 1.0\,\mathrm{MBq}\,\mathrm{kg}^{-1}$ and $0.6 / 1.3 = 0.5\,\mathrm{MBq}\,\mathrm{kg}^{-1}$. These values are in well consistence with the highest and the lowest values observed around $13\,\mathrm{h}$. For the second reason, we adopted $f_{An} = 0.78$, a value reported by McFarlane (1976), as a first trial for the model calculation. However, $f_{An}$ ranges over $0.54-0.88$, depending on vegetation type (Boyer et al., 2009; Garland and Ameen, 1979; Guenot and Belot, 1984; McFarlane, 1976). Further experimental studies on hydrogen isotope discrimination in photosynthesis reaction are needed, if we would need more realistic calculations for the experimental grape plants.

For the discrepancy (2), change in $Q_{OBT-N}$ over $13-19\,\mathrm{h}$ were mainly determined by decrease in the OBT inventory $S_{\mathrm{int}} \times W_{\mathrm{int}}$ in the intermediates pool, and by increase in both $S_{\mathrm{str}} \times W_{\mathrm{str}}$ and $S_{\mathrm{sta}} \times W_{\mathrm{sta}}$ (Fig. 8 (b)). Therefore, disagreement in $Q_{OBT-N}$ over this period can be attributable to the underestimation of the carbohydrates into and out of the sucrose pool (termed as $0.48E_{An}$ and $0.46E_{An}$ in Fig. 2), and, an overestimation of carbohydrates flux into the starch ($0.19E_{An}$) and structural pools ($0.26E_{An}$).

The residual OBT over $48-120\,\mathrm{h}$ is mainly consisted of OBT in the structural pool (Fig. 8 (b)). Therefore, overestimation in $Q_{OBT-N}$ during this term is attributable to the overvaluation of the carbohydrate flux of $0.26E_{An}$ from the intermediates to the structural pool (Fig. 3). This overvaluation is also deduced from that the experimental leaves are source leaves that should export most of the photosynthates to other sink parts, and, from the discussion made the above paragraph. In addition, for the discrepancy (3), difference in photosynthetic activity across height resulting from aging of leaves is attributable. Leaves in basal canopy are older, and hence their photosynthetic activity is smaller than the upper young leaves (Addo-Quaye et al., 1986; Collins and Scarisbrick, 1994; Taiz and Zeiger, 2002), a process which is not included in our model. This can have resulted in an overestimation of the OBT production during the exposure for the leaves in lower canopy.

Although the above-addressed discrepancies between the calculation and the observation exist, calculated $Q_{OBT-N}$ roughly agreed with the observations. Hence, the calculation results are adopted to elaborate fates of OBT fixed by leaves during the exposure.

As can be expected from Fig. 8 (b), if much longer time has passed, total OBT remaining in the leaf will equal to the inventory of OBT in the structural pool $S_{\mathrm{str}} \times W_{\mathrm{str}}$ since OBT inventory in the other pools eventually becomes zero. Then $S_{\mathrm{str}} \times W_{\mathrm{str}}$ at $120\,\mathrm{h}$ is calculated, being $15\%$ of the total OBT fixed during the exposure as shown in Fig. 9. This calculated $S_{\mathrm{str}} \times W_{\mathrm{str}}$ at $120\,\mathrm{h}$ roughly equal to the total inventory of the leaf after much longer time has passed, since change in $S_{\mathrm{str}} \times W_{\mathrm{str}}$ is quite small around $120\,\mathrm{h}$ (Fig. 8 (b)). From these elaborations, it is deduced that a larger fraction, about $85\%$ of the total OBT fixed during the exposure will be eventually translocated from leaves and fixed to other developing parts.

*[Figure 8]* Time series of OBT amounts in leaves; (a) calculated OBT amount $S_i$ by weight for each carbohydrate pool; (b) OBT inventory $S_i W_i$ in each carbohydrate pool; (c) observed and calculated non-exchangeable OBT amount $Q_{OBT-N}$ for leaves at different height in the crown. Shaded area indicates the period when the exposure was conducted.

*[Figure 9]* Calculated fraction of OBT that translocated, respired, or remained as residue at different stages in the five-day observation period. Amount of OBT fixed to the structural compounds are also indicated.

We further elaborate detailed fates of these OBT fixed to leaves during the exposure (Fig. 9). In the first day ($13-24\,\mathrm{h}$) nearly a half of the total OBT fixed during the exposure is exported to elsewhere other than the leaves. In the second day ($24-48\,\mathrm{h}$) $21\%$ of the remaining OBT is additionally translocated, and, in the third to fifth day ($48-120\,\mathrm{h}$) amount of OBT translocated is small, being only $7\%$. Finally, at $120\,\mathrm{h}$ $28\%$ of the total OBT fixed during the exposure is left in the leaves, and eventually $15\%$ will be left as the structural compounds. These relatively large amounts of OBT translocated within several days after the exposure is consistent with the observations for winter wheat, rice plants, and, cabbages (Brudenell et al., 1997; Choi et al., 2002; Diabaté and Strack, 1997). The results shown in Fig. 9 also indicate only a small fraction of the total OBT fixed is decomposed through respiration. Our results also have shown that apparent decrease in $Q_{OBT-N}$ due to dilution with newly formed carbohydrates is small for source leaves, since the total carbohydrate amount in the leaf increased only by $17\%$ of the initial value (Section 4.2.1).

## 5. Conclusions

A numerical model simulating transport of tritiated water (HTO) in atmosphere-soil-vegetation system, and, accumulation of organically bound tritium (OBT) in vegetative leaves was developed. For dynamically calculating these tritium transport and exchange, the model cooperated with an atmosphere-soil-vegetation model (SOLVEG-II) that calculates transport of heat and water, and, exchange of $\mathrm{CO}_2$. The processes included for calculating tissue free water tritium (TFWT) in leaves are HTO exchange between atmosphere and leaf interior, root uptake of aqueous HTO in soil due to transpiration, photosynthetic assimilation of TFWT into OBT, and, TFWT formation through decomposition of OBT in carbohydrates by respiration. The last two processes are related to a carbohydrate allocation/translocation compartment model in leaves. The carbohydrate compartment model has four carbohydrate pools, and, calculates carbohydrate fluxes between the pools and flux for translocation, by using daytime photosynthetic $\mathrm{CO}_2$ assimilation and nighttime respiration. A simulation of a previously-reported acute exposure of grape plants to atmospheric HTO was carried out, and, model performance was examined by comparing the calculated TFWT concentrations and non-exchangeable OBT amounts in leaves with those observed.

Calculated TFWT concentration in leaves increased soon after the start of $4\text{-}\mathrm{h}$ HTO exposure, and, reached to an equilibrium with the atmospheric HTO within a few hours, giving near zero HTO exchange flux between canopy air and leaf interior. After the end of the exposure, calculated TFWT concentration rapidly decreased, reaching nearly ambient HTO concentration. These changes in the calculated TFWT concentrations during and soon after the exposure, dominated by HTO exchange, were well agreed with the observations. The calculated results obtained also showed that change in the TFWT concentration differs for leaves at different height in the crown, affected by difference in conductance for transpiration across height. Calculated non-exchangeable OBT amount in leaves increased linearly during the exposure, reaching the maximum value at the end of the exposure. After the exposure, calculated OBT amount decreased rapidly in daytime and moderately nighttime, affected by translocation of OBT-containing sucrose. These calculated OBT amounts fairly agreed with the observations, within average errors of a factor of two.

Calculated results were applied to elaborate the fate of OBT fixed during the acute exposure of HTO. It showed that about two-thirds of the total OBT fixed during the exposure was translocated from leaves to elsewhere within two days after the exposure, and, eventually about $15\%$ of the total OBT fixed would be left in leaves. Amount of OBT spent by respiration was much smaller than that translocated from the leaves, and, dilution of OBT amount with newly synthesized carbohydrates was also small for these source leaves. From a point of application study for dose assessment through food chain, further models assessing final OBT amount in ears, fruits etc. at harvest stages are necessary as a future task.

## Acknowledgments

The authors would like to thank Dr. Belot Y. for providing experimental data set used in the model validation, and, also would like to thank him and Dr. Andoh-Atarashi M. for their helpful comments on our calculation results.

## References

- Ackley, W.M.B., 1954. Seasonal and diurnal changes in the water contents and water deficits of Bartlett Pear leaves. Plant Physiol. 29, 445–448.
- Addo-Quaye, A.A., Scarisbrick, D.H., Daniels, R.W., 1986. Assimilation and distribution of $^{14}\mathrm{C}$ photosynthetic in oiled rape (Brassica Napus L.). Field Crops Res. 13, 205–215.
- Aggarwal, O.M., Shinha, S.K., 1984. Differences in water relations and physiological characteristics in leaves of wheat associated with leaf position on the plant. Plant Physiol. 74, 1041–1045.
- Al-Riahi, M., Al-Karaghoulia, A., Hassona, A.M., Al-Kayssia, A., 1989. Relations between radiation fluxes of a greenhouse in semi-arid conditions. Agric. For. Met. 44, 329–338.
- Atarashi, M., Amano, H., Ichimasa, M., Ichimasa, Y., 1998. Deposition of $\mathrm{D}_2\mathrm{O}$ from air to plant and soil during an experiment of $\mathrm{D}_2\mathrm{O}$ vapor release into a vinyl house. Fusion Eng. Des 42, 133–140.
- Barry, P.J., Watkins, B.M., Belot, Y., Davis, P.A., Edlund, O., Galeriu, D., Raskob, W., Russell, S., Togawa, O., 1999. Intercomparison of model predictions of tritium concentrations in soil and foods following acute airborne HTO exposure. J. Environ. Radioact 42, 191–207.
- Bartels, H.W., 1991. Comparison of predicted doses due to a continuous HTO release. Fusion Eng. Des 17, 373–380.
- Belot, Y., Gauthier, D., Camus, H., Caput, C., 1979. Prediction of the flux of tritiated water from air to plant leaves. Health Phys 37, 575–583.
- Biddulph, O., Cory, R., 1957. An analysis of translocation in the phloem of the bean plant using THO, $^{32}\mathrm{P}$ and $^{14}\mathrm{C}$. Plant Physiol. 32, 608–619.
- Boyer, C., Vichot, L., Fromm, M., Losset, Y., Tatin-Froux, F., Guétat, P., Badot, P.M., 2009. Tritium in plants: a review of current knowledge. Environ. Exp. Bot. 67, 34–51.
- Brudenell, A.J.P., Collins, C.D., Shaw, G., 1997. Dynamics of tritiated water (HTO) uptake and loss by crops after short-term atmospheric release. J. Environ. Radioact 36, 197–218.
- Choi, Y.H., Lim, K.M., Lee, W.Y., Diabaté, S., Strack, S., 2002. Tissue free water tritium and organically bound tritium in the rice plant acutely exposed to atmospheric HTO vapor under semi-outdoor conditions. J. Environ. Radioact 58, 67–85.
- Choi, Y.H., Lim, K.M., Lee, W.Y., Park, H.G., Choi, G.S., Keum, D.K., Lee, H., Kim, S.B., Lee, C.W., 2005. Tritium levels in Chinese cabbage and radish plants acutely exposed to HTO vapor at different growth stages. J. Environ. Radioact 84, 79–94.
- Choi, Y.H., Kang, H.S., Jun, I., Keum, D.K., Lee, H., Kim, S.B., Lee, C.W., 2007. Fate of HTO following its acute soil deposition at different growth stages of Chinese cabbage. J. Environ. Radioact 97, 20–29.
- Collins, C.D., Scarisbrick, D.H., 1994. The effects of the plant growth retardant RSW0411 on assimilate distribution in evening primrose. Field Crop Res. 36, 59–67.
- Couchat, P., Puard, M., Lasceve, G., 1983. Tritiated water vapor exchange in sunflowers. Health Phys 45, 757–764.
- Diabaté, S., Strack, S., 1993. Organically bound tritium. Health Phys 65, 698–712.
- Diabaté, S., Strack, S., 1997. Organically bound tritium in wheat after short-term exposure to atmospheric tritium under laboratory conditions. J. Environ. Radioact 36, 157–175.
- Farquhar, G.D.S., von Caemmerer, S., Berry, J.A., 1980. A biochemical model of photosynthetic $\mathrm{CO}_2$ assimilation in leaves of C3 species. Planta 149, 78–90.
- Fondy, B., Geiger, D.R., 1982. Diurnal pattern of translocation and carbohydrate metabolism in source leaves of Beta vulgaris L. Plant Physiol. 70, 671–676.
- Garland, J.A., Ameen, M., 1979. Incorporation of tritium in grain plants. Health Phys. 36, 35–38.
- Galeriu, D., Melintescu, A., Beresford, N.A., Crout, N.M.J., Peterson, R., Takeda, H., 2007. Modeling 3H and 14C transfer to farm animals and their products under steady state conditions. J. Environ. Radioact 98, 205–217.
- Guenot, J., 1984. Compartment du tritium dans les vegetaux superieurs Rapport CEA-R-5269 (in French).
- Guenot, J., Belot, Y., 1984. Assimilation of 3H in photosynthesis leaving leaves exposed to HTO. Health Phys 47, 849–855.
- Gulden, W., Raskob, W., 1992. Accidental tritium doses based on realistic modeling. Fusion Technol. 21, 536–543.
- ICRP, 1995. Age-dependent Doses to Members of the Public from Intake of Radionuclides: Part 5. In: Comparison of Ingestion and Inhalation Dose Coefficients. International Commission on Radiological Protection Publications, vol. 72. Pergamon Press, Oxford.
- Shimomura, Y., Saji, G., ITER Joint Central Team, 1998. ITER safety and operational scenario. Fusion Eng. Des 39, 17–32.
- Kimball, B.A., 1973. Simulation of the energy balance of a greenhouse. Agric. Meteorol. 11, 243–260.
- Kline, J.R., Stewart, M.L., 1974. Tritium uptake and loss in grass vegetation which has been exposed to an atmospheric source of tritiated water. Health Phys. 26, 567–573.
- Komuro, M., et al., 2002. HT oxidation in soils in Ibaraki and isolation, identification of HT oxidizing soil bacteria. J. Fusion Sci. Technol. 41, 422–426.
- Kondo, J., Miura, A., 1985. Surface heat budget of the Western Pacific for may 1979. J. Meteorol. Soc. Jpn. 63, 633–646.
- Kondo, J., Saigusa, N., 1994. Modeling the evaporation from bare soil with a formula for vaporization in the soil pores. J. Meteorol. Soc. Jpn. 72, 413–421.
- Leuning, R., 1995. A critical appraisal of a combined stomatal-photosynthesismodel for $\mathrm{C}_3$ plants. Plant Cell Environ. 18, 339–355.
- McFarlane, J.C., 1976. Tritium fractionation in plants. Environ. Exp. Bot. 16, 9–14.
- McFarlane, J.C., 1978. Tritium accumulation in lettuce fumigated with elemental tritium. Environ. Exp. Bot. 18, 131–138.
- Mullen, J.A., Koller, H.R., 1988. Daytime and nighttime carbon balance and assimilate export in soybean leaves at different photon flux densities. Plant Physiol. 86, 880–884.
- Murphy Jr., C.E., 1991. Session Summaries of the Workshop on Tritium Safety and Environmental Effects, Oct. 15–17, 1990, Aiken, South Carolina, USA. Westinghouse Savannah River Co., WSRC-TR-352.
- Nagai, H., 2004. Atmosphere-Soil-Vegetation Model Including $\mathrm{CO}_2$ Exchange Process JEARI-Data/Code, 2004-014 (available from Japan Atomic Energy Agency upon request).
- Nagai, H., 2005. Incorporation of $\mathrm{CO}_2$ exchange processes into a multiplayer atmosphere-soil-vegetation model. J. Appl. Meteorol. 44, 1574–1592.
- Noguchi, H., Yokoyama, S., Kinouchi, N., Murata, M., Amano, H., Atarashi, M., Ichimasa, Y., Ichimasa, M., 1995. Tritium behavior on a cultivated plot in the 1994 chronic HT release experiment at Chalk River. Fusion Technol. 28, 924–929.
- Okada, S., Momoshima, N., 1993. Overview of tritium: characteristics, sources, and problems. Health Phys 65, 595–609.
- Ota, M., Yamazawa, H., Morizumi, J., Iida, T., 2007. Measurement and modeling of hydrogen isotopic gases by soil. J. Environ. Radioact 97, 103–115.
- Raskob, W., 2002. Enhancement of accident consequence assessment model for tritium UFOTRI include a wider variety of human foodstuff. Fusion Sci. Technol. 41, 346–350.
- Raskob, W., Barry, P., 1997. Importance and variability in processes relevant to environmental tritium ingestion dose models. J. Environ. Radioact 36, 237–251.
- Servaites, J.C., Geiger, D.R., 1974. Effects of light intensity and oxygen on photosynthesis and translocation in sugar beet. Plant Physiol. 54, 575–578.
- Strack, S., Diabaté, S., Müller, J., Raskob, W., 1995. Organically bound tritium formation and translocation in crop plants, modeling and experimental results. Fusion Technol. 28, 951–956.
- Sweet, C.W., Murphy Jr., C.E., Lorenz, R., 1983. Environmental tritium transport from and atmospheric release of tritiated water. Health Phys 44, 13–18.
- Taiz, L., Zeiger, E., 2002. Plant Physiology, third ed. Sinauer Associates, Inc., Massachusetts (in Japanese).
- Täschner, M., Wiener, B., Bunnenberg, C., 1988. HT dispersion and deposition in soil after experimental release of tritiated hydrogen. Fusion Technol. 14, 1264–1269.
- Täschner, M., Bunnenberg, C., Raskob, W., 1997. Measurements and modeling of tritium reemission rates after HTO depositions at sunrise and sunset. J. Environ. Radioact 36, 219–235.
- UNSCEAR, 2000. Sources and Effects of Ionizing Radiation. United Nations Scientific Committee on the Effects of Atomic Radiation. 2000 Report to the General Assembly with Scientific Annexes, Annex C.
- Velarde, M., Perlado, J.M., 2003. Molecular tritium contribution to the doses by ingestion and re-emission from releases in inertial fusion reactors. Fusion Eng. Des 69, 789–793.
- Yamada, T., 1981. A numerical simulation of nocturnal drainage flow. J. Meteor. Soc. Jpn. 59, 108–122.
- Yamazawa, H., Nagai, H., 1997. Development of One-dimensional Dynamical Soil-atmosphere Model. JEARI-Data/Code 97-041. Japan Atomic Energy Agency (in Japanese).
- Yamazawa, H., 2001. A one-dimensional dynamical soil-atmosphere tritiated water transport model. Environ. Model. Softw 16, 739–751.