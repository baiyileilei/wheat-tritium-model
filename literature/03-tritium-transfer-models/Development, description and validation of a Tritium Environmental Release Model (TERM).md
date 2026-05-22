# Development, description and validation of a Tritium Environmental Release Model (TERM)

**Authors:** Rebecca S. Jeffers, Geoffrey T. Parker
**Journal:** Journal of Environmental Radioactivity
**Year:** 2014
**Volume:** 127
**Pages:** 95-104

## Abstract
Tritium is a radioisotope of hydrogen that exists naturally in the environment and may also be released through anthropogenic activities. It bonds readily with hydrogen and oxygen atoms to form tritiated water, which then cycles through the hydrosphere. This paper seeks to model the migration of tritiated species throughout the environment - including atmospheric, river and coastal systems - more comprehensively and more consistently across release scenarios than is currently in the literature. A review of the features and underlying conceptual models of some existing tritium release models was conducted, and an underlying aggregated conceptual process model defined, which is presented. The new model, dubbed Tritium Environmental Release Model (TERM), was then tested against multiple validation sets from literature, including experimental data and reference tests for tritium models. TERM has been shown to be capable of providing reasonable results which are broadly comparable with atmospheric HTO release models from the literature, spanning both continuous and discrete release conditions. TERM also performed well when compared with atmospheric data. TERM is believed to be a useful tool for examining discrete and continuous atmospheric releases or combinations thereof. TERM also includes further capabilities (e.g. river and coastal release scenarios) that may be applicable to certain scenarios that atmospheric models alone may not handle well.

## 1. Introduction
Tritium ($^{3}\mathrm{H}$, T) is an isotope of hydrogen (H) formed naturally in the stratosphere that, like H, readily forms a chemical bond with oxygen (O) and another H atom to form tritiated water (HTO, as opposed to the more common $\mathrm{H}_2\mathrm{O}$). Notwithstanding isotopic effects, T behaves essentially identically to its stable analogue (hydrogen), and thus traces a similar path through biological and chemical systems in the environment. The physico-chemical similarity of HTO to water is even greater, as the supplemental H and O elements in the molecule effectively reduce the relative significance of the two extra neutrons on the radioactive isotope.

Anthropogenic sources of tritium include nuclear power, medical and industrial applications: these can raise concentrations in the global hydrosphere above levels naturally induced by cosmic ray bombardment. Weapons use and testing have also raised ambient concentrations significantly in the past. The physical half-life of $^{3}\mathrm{H}$, which decays via beta emission, is 12.32 years, and knowledge of past peaks in ambient background concentrations can be used to date recharge and withdrawals of water in, for instance, aquifers (Gat, 2010; Michel, 2005).

Like all beta-emitters, $^{3}\mathrm{H}$ also poses potential risks to human health. These risks are exacerbated because of the significant role, ready dispersion and uptake by biological systems of the two chemical forms, tritiated gas (HT) and tritiated water vapour (HTO). This is further complicated by the relative difficulty of beta particle detection at practicable distances in various environmental compartments. Thus, models capable of tracking $^{3}\mathrm{H}$ concentrations in compartments of interest over short- and long-term time-scales form a valuable asset - alongside monitoring - in the regulatory, assessment and engineering asset toolset. Widely used models previously described in the literature are discussed in the next section. This paper proposes to supplement the existing literature with a novel conceptual model, dubbed Tritium Environmental Release Model TERM. The underlying conceptual model, major processes and assumptions are described herein, followed by a series of validation tests and findings. Like other work in the literature, the model proposed deals with understanding transfers from source to air to receptors, considering all pathways. An integrative approach for short-term and long-term exposures in terrestrial and aquatic media is less well developed, and it is the aim here to present a new dynamic model of tritium transfer in both terrestrial and aquatic systems. This novel model is designed to both supplement and bridge the capabilities of existing models, with particular respect to environmental media (and hydrological systems especially) and release duration.

## 2. Overview of approach and methods

### 2.1. Methodology
A review of the features and underlying conceptual approaches of existing tritium release models was conducted. From these, gaps and needs were identified which were useful in finalizing model structure and formulation of TERM. We proceed with the review of four typical tritium models of significantly different complexity, which are currently in use. They are designated here as: DRLG/Hart (Hart, 2008), PCCREAM (Smith and Simmonds, 2009), GENII (Napier et al., 2004) and UFOTRI (Raskob, 1990, 1993).

The first two models are intended to provide regulatory guidance for long-term releases at relatively low emission levels, consistent with routine or near-routine releases, for instance. The third, GENII, has also been modified for use in cases of a discrete release to the atmosphere. The first three of these models (DRLG/Hart, PCCREAM and GENII) are primarily geared towards modelling the release of other radionuclides. In multi-isotopic release (e.g. fission reactor accident) scenarios, the tritium component is typically much less significant as a source of radiological dose (and also biochemical toxicity, where this may be considered) than other radionuclides (though this simplification may not hold in e.g. the aquatic environment where tritium can be a key radionuclide and contribute significantly to the doses received by aquatic biota and humans). Accordingly, these three models avoid use of detailed tritium-specific processes and opt instead for a simplistic Specific Activity concept that can broadly estimate the significance of the tritium release as a supplementary release and risk component. In contrast to these, UFOTRI is a model focused specifically on the radiological consequences of an accidental atmospheric tritium release. The processes modelled by UFOTRI are significantly more extensive and, as some also assume equilibrium conditions, more robust for a dynamic case. Of the four models discussed here, UFOTRI is probably the best model for use in the dynamic, discrete atmospheric release case. A range of other models not considered here also exists, but UFOTRI in general compares well, for our purposes, to alternatives due to its physical basis, its documented application for generic, as well as site-specific, assessments and the range of trials in literature it has undergone (C.F. Raskob, 2007; Galeriu et al., 1995).

There is also a wide discrepancy between the chemical forms and compartments considered in each model. This lack of harmony between model forms leads to inherent challenges in addressing novel conditions and conditions including multiple release types. None of the models reviewed are well suited for both discrete and prolonged releases of tritium or are capable of considering simultaneous release to multiple environmental systems (e.g. river and atmosphere). Specific inclusion of these features in the model, as well as other important hydrological systems, would be a significant and useful contribution to the modelling and assessment of tritium releases to the environment (see also, for instance, International Atomic Energy Agency [IAEA], 2012).

The methodology presented here began with a detailed review of each of the above models, and particularly an assessment of alternative formulations of component processes. This review led in turn to the formulation of a new aggregate model which emphasizes the aforementioned characteristics. The new model, TERM, was then tested against multiple validation sets from the literature, including experimental data and reference tests for tritium models.

### 2.2. State of the art
Release of tritium to the environment entails cycling of its chemical forms through several compartments, including those comprising plants and animals. Implied is the significant role the organically bound tritium (OBT, a chemical form also considered in TERM) can play in dose calculations, though the focus in this paper will remain on environmental concentrations. A summary of characteristics of the reviewed models is shown in Fig. 1.

The first three models in Fig. 1 are generalized radionuclide dispersion models and, regardless of the number of compartments tracked, make simplifying assumptions to estimate, broadly, specific activities of T in the environment. In contrast, the final model, UFOTRI, is significantly more granular, as it is tailored to tritium processes and, even more specifically, to those relevant for very short-term, discrete, releases thereof. GENII can also model discrete releases to the atmosphere, as well as continuous river releases. No model is suitable for discrete releases to rivers, lakes/reservoirs or coastal regions, though these are generally significant compartments from the hydrological perspective. Therefore, no model is well suited for combined scenarios, or comparison of scenarios, that involve discrete and continuous releases to the whole hydrosphere. This article proposes to find improvements to bridge and advance these research gaps (that may also reflect regulatory and compliance gaps).

## 3. Model definition
TERM is, first and foremost, a conceptual modelling framework that seeks to integrate existing state-of-the-art models for the migration of tritium in the environment. The conceptual submodels are selected for overall appropriateness to the discrete/continuous release scenarios, and for other properties that emphasize robustness, scalability (alongside transparency and moderate complexity/data requirements) across the entire hydrologic system in the region of interest. Thus, for example, many submodels are readily simplified (or even altogether ignored) through the use of constants en lieu of equations. One advantage this provides for is direct comparison with existing datasets and models (by selecting equivalent processes to be considered), but also insights such as which advantages further model complexity, parameterization, and/or data might offer. Some discussion of these features will be presented in the model validation section later in this article, while this section details the underlying conceptual model and major processes considered. Fig. 2 shows an outline of the model functionality and organizational structure.

Fig. 2 illustrates the structure of the model as two major branches (though the model can, in fact, also consider these together, which is a distinctive feature when compared with other models reviewed here). The first major branch is the discrete release case, which represents a relatively short-term, finite release. This is consistent with scenarios such as sudden discharges or accidental release. The discrete model routes the initial release into one of three transport pathways: two atmospheric pathways (one for each chemical form of T), and river releases (where HTO-related processes should dominate). Atmospheric releases use a simple Gaussian dispersion model from a point (though more complex cases may be modelled using multiple sources, for example), whereas river releases may be considered as planar, point, or line source (e.g. diffusers for a controlled released event). The model construction makes no significant a priori assumption on the reasonableness of any given release scenario, and leaves such decisions to the modeler.

The second major branch represents the continuous model, with assumptions more suited for long term releases. This may be consistent for routine release scenarios through, for example, management or leakage. This branch offers the same basic functionality as the discrete release (adjusted, as necessary, for the continuous release case). Also included here is a coastal release model, which may be of use for non-inland releases. A discrete coastal release, implying an acute, unmanageable and unsteady release is not included. The 'secondary' uncertainties (e.g. hydrodynamics, ecology, temperature and salinity gradients) associated with such an instantaneous coastal dispersion would often, in practice, eclipse any predictive or forensic capability of even a relatively sophisticated conceptual tritium circulation and speciation model.

Regardless of the branch selected, following the source/transport modules in the model flowchart are the exchanges between the principal soil, atmospheric, and water compartments, as well as the secondary vegetable and animal ones. The additional compartments considered include soil pore water, pond water, well water, plant water, plant organic matter, animal water and animal organic matter. These exchanges form the conceptual core of the model and are based on literature and best practices, as outlined in this paper generally and, in much additional detail, the references cited herein. Considerably more material can be found by reviewing material referenced herein (e.g. Raskob, 1990, 1993), as well as the freely-available reports generated during the development of the TERM model and code (available online and by request to the corresponding author at http://www-g.eng.cam.ac.uk/werg/).

### 3.1. Source description
TERM includes conceptual models for atmospheric and river releases, and associated physical advection and diffusion of tritiated species. Also included is a coastal region release model, consistent with Hart (2008).

### 3.2. Atmospheric dispersion
The governing models for the dispersion of both continuous and discrete releases are the Gaussian puff (discrete)/plume (continuous) representations. The puff representation can be formulated as in Eq. (1):

$$
\begin{array}{r}
C(x,y,z,t) = \frac{M}{(4\pi t)^{3/2}\sqrt{D_{xt}D_{yt}D_{zt}}} \\
\times \exp \left(-\frac{(x - x_{0} - U_{xt}t)^{2}}{4D_{xt}t} -\frac{(y - y_{0} - U_{yt}t)^{2}}{4D_{yt}t} -\frac{(z - z_{0})^{2}}{4D_{zt}t}\right) 
\end{array} \quad (1)
$$

where,
- $C$: concentration at calculated location and time ($\mathrm{M}/\mathrm{L}^{3}$)
- $M$: mass of pollutant released ($\mathrm{M}$)
- $x_{0}, y_{0}, z_{0}$: 3-dimensional spatial coordinates of the point source (L)
- $x, y, z$: coordinates of the concentration being calculated at a given time $t$ (T) after the instantaneous release
- $D_{it}$: diffusion coefficients in the $i$-dimension with respect to time, $t$ with $i\in \{x,y,z\}$ ($\mathrm{L}^{2}/\mathrm{T}$)
- $U_{i}$: bulk flow velocity in the $i$-dimension with $i\in \{x,y\}$ ($\mathrm{L}/\mathrm{T}$)

Eq. (1) describes the concentration at a point in space and time as a function of a puff (instantaneous) release, into a bulk flow medium of known velocity in 2 dimensions (i.e. velocity profile with height), of a known quantity of dispersible substance at a known position with known diffusion coefficients in each spatial dimension.

For continuous releases under time-varied wind and stability conditions, Eq. (1) can be integrated over a set of polar sectors (conveniently compatible with windrose data discretization schemes), formed by subdividing the region around the source into 'pie slice' shaped elements spanning 360 decimal degrees, and then further slicing these regions at increasing radii so as to form a polar grid, with a specific element associated with a given angle and distance from the release point.

Eq. (2) is derived from the previously discussed framework, with the same principal variables. The major distinction is that the dispersible substance is now defined as being emitted from a continuous source - released at a known, steady, rate over time - and the concentration at any specified location is considered as unchanging (steady state conditions) and, therefore, no longer a function of time.

$$
C(x,y,z) = \frac{Q}{4\pi(x - x_0)\sqrt{D_{yt}D_{zt}}}\exp \left(-\frac{(y - y_0)^2}{4D_{yt}\frac{(x - x_0)}{U}} -\frac{(z - z_0)^2}{4D_{zt}\frac{(x - x_0)}{U}}\right) \quad (2)
$$

where,
- $Q$: release rate of pollutant ($\mathrm{M}/\mathrm{T}$)

Eqs. (1) and (2) are valid in the infinite domain. In the finite (i.e. real world) domain, the continuous fluid assumption is invalid, so reflective effects from constraining features - such as mixing layers, the ground, or river banks (for the analogous river release model discussed subsequently) - need also be considered. These effects are included in dispersion calculations using the concept of image sources, which can be used to represent reflections from the original release (that would not need to be accounted for in the infinite domain). Shifts in plume direction during instantaneous or continuous release can be considered using image sources.

### 3.3. Transformations in the continuous release case

#### 3.3.1. Atmospheric processes
Transfers from the atmosphere to other compartments are calculated using the same equations as in Hart (2008). They are summarized in Fig. 3, for the reader's convenience. In all cases, Subscript species is the concentration in the subscript compartment for each tritiated species considered ($\mathrm{Bq}/\mathrm{L}$ in water, $\mathrm{Bq}/\mathrm{m}^3$ in air, $\mathrm{Bq}/$ (kg fresh weight) in living organisms). $\mathrm{RF_{sw}}$ and $\mathrm{RF_{p}}$ values are, respectively, the (unitless) ratio of tritiated water in soil and plant water to that in atmospheric moisture. $\mathrm{DW_{a}}$ and $\mathrm{DW_{p}}$ are the dry to fresh weight of animal and plant tissues, $\mathrm{WE_{a}}$ and $\mathrm{WE_{p}}$ are the corresponding water equivalents of animal and plant dry matter, and the $f$ values represent which fraction of animal or plant water is derived from the ingestion or inhalation pathways. Bucket ratio is an empirical relationship between the tritium concentration in precipitation in a bucket to that in air. Hart (2008) should be consulted for a more reductionist discussion of these processes and parameters.

#### 3.3.2. Terrestrial processes
Expressions for transfers between terrestrial compartments are summarized in Fig. 4 (which uses the same parameter naming convention as Fig. 3, and Hart, 2008). As for the atmospheric case, the transfers between compartments in the terrestrial environment are very similar to several of the reviewed models, however the transfer from plant water and plant organic matter to animal water and animal organic matter are subdivided into four separate processes, in contrast to Hart (2008). Another noteworthy issue is that of 'indoor' water concentration, which may be greater than outdoor concentrations due to the evaporation of domestic water.

#### 3.3.3. Chemical processes
For atmospheric releases of HT (as opposed to HTO), the conversion to HTO is via deposition, oxidation in the soil, and reemission. These processes may be grouped into a single equation. Transfer of HT to HTO or OBT in plants is also possible especially via airborne HTO taken up for photosynthesis or via plant roots (for more discussion, see e.g. Belot et al., 2005; Ota et al., 2007; Galeriu et al., 2008). These 3 transfers are shown in Fig. 5. Once transformed to HTO or OBT in the soil and plant systems, the remaining atmospheric HT release model components (i.e. transfers between compartments) is identical to the HTO model previously discussed.

#### 3.3.4. River and surface water processes
As previously described, TERM models both continuous and discrete releases to fluvial systems in 1-, 2-, or 3-spatial dimensions, associated with, respectively, a plane (i.e. instantaneous complete mixing), line (constant concentration with respect to depth) or point source release.

For continuous release cases, the 1-dimensional model simply calculates the initial concentration using a mixing equation as shown in Eq. (3). Transfer to pond water is also modelled, using the relevant equation from Fig. 3.

$$
C_{\mathrm{river}} = \frac{Q}{F} \quad (3)
$$

with,
- $F$: the flow rate in a river ($\mathrm{L}^{3}/\mathrm{T}$)

The 2-dimensional model assumes a series of image sources (the number of which can be specified by the user) in a line in the transverse direction, and constant concentration with respect to depth. The 3-dimensional, point source, model is analogous to the atmospheric release model case and uses a Gaussian plume representation (Eq. (1)).

In the discrete release case, a point source is modelled using the Gaussian Puff model for a point source (Eq. (2)). Image sources are used in the y and z (horizontal and vertical) directions to account for the constraints of the river banks and bottom. For the 1-dimensional case, this same equation is integrated for a planar release and solved according to the chosen discretization along the streamwise direction. A 2-dimensional (linear) source is modelled using the same equation for a line source.

#### 3.3.5. Coastal release
The coastal release model calculates aquatic concentrations from dilution in the coastal region using the same basic formulation as in Hart (2008). The concentrations are calculated using Eq. (4), which is computed over the Cartesian domain around the release location, the geometry of which is input to the model.

$$
C_{\mathrm{coastal\_water}} = \frac{Q\alpha_{\mathrm{coast}}\beta_{\mathrm{coast}}}{D_{\mathrm{F}}Q_{\mathrm{v}}}\exp \left(-\lambda \frac{x}{U_{\mathrm{C}}}\right) \quad (4)
$$

with,
- $\alpha$: the annual average fraction of time that the current direction is from the source towards the point of interest ($-$)
- $\beta$: the annual average effluent recirculation factor for the source ($-$)
- $\lambda$: decay/removal constant (1/T)
- $Q_{v}$: the annual average volumetric discharge rate of effluent ($10^{-3}\mathrm{m}^3/\mathrm{s}$)
- $U_{c}$: the current speed in the direction towards the point of interest ($\mathrm{m}/\mathrm{s}$)
- $x$: the distance between source and the point of interest (m)
- $D_{\mathrm{F}}$: the dilution factor calculated using Eq. (5):

$$
D_{\mathrm{F}} = \left[\left(\frac{1000d\beta_{\mathrm{coast}}\sqrt{\pi k}}{Q_{v}U_{\mathrm{C}}^{0.17}}\right)^{\frac{1}{1 + \gamma}} + D_{0}^{\frac{1}{0.17}}\right]^{\frac{1}{1 + \gamma}} \quad (5)
$$

with,
- $D$: the average water depth in the reach occupied by the plume (m)
- $\kappa$: the proportionality coefficient
- $D_{0}$: the initial dilution at the point of discharge.

Eqs. (4) and (5) assume a continuous release. Therefore TERM is not in its current implementation suitable for modelling discrete releases to coastal regions.

### 3.4. Transformations in the discrete release case
The discrete release case is assumed to occur over relatively short timescales. In this context, though deposition to and reemission from the terrestrial environment is modelled, the effect of this on the air concentrations is not taken into account. Consequently, concentrations in the vicinity of the primary plume are over-estimated, while air concentrations are under-estimated once the plume has passed. The model is structured so that, in cases where these assumptions may not prove acceptable (e.g. during a significant ongoing release), the continuous model may be used.

The discrete release case model is broadly similar to the continuous release case model, with the addition and amendment of several processes that may be significant for short-term releases. These changes are based on the reviewed models, such as UFOTRI, which tend to favour the short-term release scenario. As elaborated in the following sub-sections, the discrete release model is more reductionist than the continuous conceptual model, and involves additional resistances and compartments (e.g. three separate soil layers), which can be lumped together in the continuous case.

#### 3.4.1. Atmospheric processes
In the case of an instantaneous release (or a series of instantaneous releases), the Gaussian Puff model (Eq. (1)) is used. The dispersion coefficients are calculated using the Pasquill-Gifford diffusion formula which are well-tested and well-regarded (Napier et al., 2004). The Pasquill-Gifford approach associates a 'stability class' to the region considered that reflects atmospheric conditions (i.e. degree of plume dispersion, mixing layer height) at the time of release (Gifford, 1959; Pasquill, 1961).

#### 3.4.2. Terrestrial processes
The transfer of atmospheric concentrations to the terrestrial systems are calculated for each cell (i.e. spatial discretization element) at every time step (in the dynamic model case - the user-selected time step must be large enough to justify the other parameters/assumptions detailed throughout the paper), using a resistance model. Total resistances of transfer to soil and grass/plants systems are calculated, comprising aerodynamic, atmospheric and boundary layer resistances in addition to soil- and canopy-specific resistances, respectively.

The terrestrial model includes up to three soil layers that are intended to cover the root zone. HTO deposited on the top layer is routed through the soil layers using the discretized version of Darcy's law (as suggested in Walley and Hussein, 1982). The concentration in well (ground) water is set to be the same as that in the third (lowest) soil layer. An indoor atmospheric concentration associated with the use of domestic water from wells can then also be calculated in the same fashion as for the continuous release case.

Uptake of HTO by vegetation and grass with roots in the modelled soil layers is determined by the transpiration from the canopy, calculated using Monteith's (1965) bulk resistance formula. A 'development factor' model to account for OBT as a function of vegetation development stages (i.e. age - as described in Hart, 2008) is also included, as are transfers to animal compartments (e.g. cattle) that may be of significance if animals are grazing is abundant close to the release.

#### 3.4.3. Chemical processes
In the case of a discrete HT release, the atmospheric dispersion is calculated in the same fashion as above, with washout (but not deposition) considered to be negligible. Many conceptual models recognize not only that HT is only weakly soluble and not washed away by rain, but also has low dry deposition velocity. TERM allows the HT, once deposited, to oxidize quickly to the more biologically available HTO form, and hence for re-emission to the atmosphere, which in this case, becomes more significant. This is consistent with the approach in Raskob (1993) and others.

Re-emission of the oxidized form is calculated above each cell (i.e. spatial discretization unit) at each time step. The emission from soil, grass and plant systems can be summed and then modelled as a Gaussian puff release from an areal source at ground-level.

#### 3.4.4. River and surface water processes
In the case of a discrete release to a fluvial system, there are again three possible release types - planar, linear or point source. Analogously to the continuous case, the discrete release is modelled using a Gaussian representation for a 'puff' release from the specified release coordinates. As before, a user-specified number of image sources are used to account for banks and water surface/river bottom in the 2-d and 3-d cases (i.e. linear and point source representations), respectively.

Transfer to ponds is also modelled using the same equation as the continuous release, with the pond assumed to come into equilibrium with the atmospheric moisture concentration instantaneously.

## 4. Implementation and validation
After the conceptual elements of the model were defined, an implementation of TERM was coded as a basic platform for calculation in commercial software (MATLAB, 2012). Two reference validation data sets were assembled from the literature to assess components of the model, based on CNSC (2009) and Raskob (1990).

### 4.1. Ecometrix/IMPACT validation set (CNSC, 2009)
The Ecometrix validation data set is based on experimental results obtained in 2006 by monitoring at a manufacturing site in Ontario, Canada. In this experiment, air measurements were taken using a passive sampling system to assess concentrations of HTO for a continuous (steady) atmospheric release over one year, totalling 74,000 GBq. This scenario has previously served as the validation data set of the IMPACT model (CNSC, 2009), and those published results are also presented here for comparison. Additional scenario data for site conditions were sourced from EC (2012).

#### 4.1.1. Site conditions
A dataset for scenario conditions was reconstructed by using the annual emission of 74,000 GBq, available from CNSC (2009). No information was available regarding the height of the release or whether the release would be susceptible to plume rise before being advected by the wind. The effective release height in the scenario was, therefore, set to zero.

The IMPACT code used site meteorological data which, unfortunately, were not available (CNSC, 2009). In their place, hourly wind direction and speed data from Ottawa (the location of the nearest weather station) for 2006, obtained from Canada's National Climate Data and Information Archive (EC, 2012), have been substituted. These have then been supplemented with Pasquill stability classes, as defined in Table 1, and inferred from known conditions. Table 2 shows summary results of this elaboration.

Stability classes were computed across 16 polar directions by fitting known conditions to data, but these calculations are inherently difficult and far less ideal than site-measured parameters. The Pasquill stability classes are used to calculate atmospheric dispersion parameters and are thus important inputs. The approach taken here is common in the literature, given that stability observations are often difficult and costly to obtain, however it should be emphasized that these represent a difficulty (albeit an almost routinely accepted one) with the fitting of our dispersion model to true site conditions.

**Table 1. Stability categories of Pasquill (1961).**

| Wind speed at 10 m (m/s) | Day solar intensity | Day solar intensity | Day solar intensity | Night Overcast | Night Clear |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | **Strong** | **Moderate** | **Slight** | | |
| 0–2 | A | A–B | B | — | — |
| 2–3 | A–B | B | C | E | F |
| 3–5 | B | B–C | C | D | E |
| 5–6 | C | C–D | D | D | D |
| >6 | C | D | D | D | D |

**Table 2. Estimated probabilities for each stability class in each wind speed class.**

| Wind speed class (m/s) | A | B | C | D | E | F |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0–2 | 0.5 | 0.5 | 0 | 0 | 0 | 0 |
| 2–3 | 0.0833 | 0.25 | 0.1667 | 0 | 0.25 | 0.25 |
| 3–5 | 0 | 0.25 | 0.25 | 0.25 | 0.25 | 0 |
| 5–6 | 0 | 0 | 0.25 | 0.75 | 0 | 0 |
| >6 | 0 | 0 | 0.1667 | 0.8333 | 0 | 0 |

#### 4.1.2. Validation results
Despite these difficulties in matching modelled site conditions, IMPACT is, like TERM, also a sector-average Gaussian plume model, and thus, offers a good opportunity for comparison in continuous release conditions. Results from the TERM models compare favourably with both the IMPACT simulation and observed values (Fig. 6). All three follow broadly similar trends with changes both in distance and direction.

As would be expected, given the assumed ground-level release height, both models over-estimate measured values in the regions nearest to the release ($< 250\mathrm{m}$). Further away from the release point, TERM tends to underestimate air concentrations. While, in many applications, the more conservative assumption is to overestimate these, some emphasis is merited on the fact that $89\%$ of the TERM predictions are proximal (within a factor of 2) to observed data when compared with the IMPACT results (which only achieve this level $60\%$ of the time). On average, TERM simulation results are $8\%$ lower than measurements, while IMPACT results over-predict values by $83\%$.

The difference in these results may be attributed to the effect of the stability classes which were reconstructed from nearby data, the differences in the conceptual model processes considered (where TERM is more detailed), the associated addition of calibration parameters, issues related to discretization, or some combination of these effects. Further examination of these issues is presented below. There appears to be strong evidence that TERM is capable of modelling site conditions, when compared to observed data, at least as well as the alternative model for continuous release of HTO.

As noted above, the potential for considerable discrepancy between the stability classes as used in the reconstructed model when compared with actual site conditions during the release is one our methodology has had to accept. To supplement the analysis, so as to make some accommodation for this potential problem, the TERM model was also used to simulate two 'bracketing' conditions, with constant stability class D and F (typically the most conservative). These lines are shown in Fig. 6 (alongside the IMPACT simulation values) and, indeed, do bracket the measured results (to which all values in Fig. 6 are normalized), offering further evidence that the TERM implementation is behaving reasonably well.

Discretization effects were also investigated, with windrose data divided into both 12- and 16-radial sectors, and a corresponding representation in the simulation (Fig. 7). Results from both schemes are in close agreement, with the 12-sector discretized case slightly better than the 16-sector discretization at large distances. Thus, increased discretization does not seem to help appreciably.

#### 4.1.3. Parameterization
Fig. 8 shows simulation results for the IMPACT and TERM models. TERM results with various conceptual simplifications are also presented in the same figure for comparison. All model results are normalized to observed values from the IMPACT case study data set.

TERMa to TERMe are simplified versions of the complete TERMF model. TERMe considers 7 image sources (as described in the Methodology section above), less than the 9 considered in the TERMF simulation. TERMd considers 5 image sources, TERMc considers 3, while TERMb considers reflection in the ground plane only and TERMa ignores image sources altogether. TERMb is equivalent to the formulation in the aforementioned Hart (2008) model. In this simulation, there is no appreciable difference between results from TERMb through TERMF, implying that the additional complexity is not improving simulation results. In this particular case, the effect of the image Gaussian image on the ground air concentrations is negligible due to their large distance from the ground plane. This type of insight may be useful when considering similar release conditions for the ground-level air concentration endpoint, and is of particular value when results are used to consider model and parameter uncertainty.

### 4.2. Reference validation set from Raskob (1990)
A second validation scenario was used to assess performance characteristics of TERM when simulating a short-term (discrete) atmospheric release of $100\mathrm{g}$ of HTO. The release inventory details in the original reference are not clearly described, however the report suggests that the scenario assumes a release of approximately $2\cdot 10^{13}$ Bq, so this figure is used for the analysis presented here. The release in the original reference takes place over 2 min, so is considered as an instantaneous release in the TERM results discussed here.

#### 4.2.1. Site conditions
This hypothetical accident scenario is the reference validation case in the UFOTRI model definition documents and may be taken as a test of TERM's suitability for the same type of scenario, namely accidental releases. Accordingly, the TERM implementation was adjusted to match the dispersion model assumptions (i.e. thresholding of dispersion parameters - see Raskob, 1990) used to obtain the reference results.

Results for the UFOTRI reference scenario at release heights of $10\mathrm{m}$ and $20\mathrm{m}$ were generated using TERM and are shown in Fig. 9. Results for the unmodified TERM dispersion model are also shown.

#### 4.2.2. Validation results
The results of the TERM simulation are of similar magnitude and develop in similar fashion with distance (though one should note that both axes are logarithmic scales) when compared to the reference model. The effect of the thresholding dispersion model used in Raskob (1990) is pronounced and can readily be seen in both plots of Fig. 9. The unmodified TERM model also shows a similar change in slope of concentrations versus distance as the plume develops, though this feature happens very proximal to the source, given the Raskob (1990) dispersion assumptions, and is not evident in the plot of the modified TERM model. The discretization has been selected to highlight the model performance at medium to far distances, where small changes in the source parameters are less significant and the conceptual model of environmental processes is most significant. It is here where big differences in e.g. the transfers between compartments are likely to be of most importance for the current validation exercise (which is seeking to understand how the new formulation behaves when compared with alternatives models and data in the literature). The results appear to indicate the TERM model provides adequate estimates under the reference calibration conditions recommended for the UFOTRI model, and simulation results of the TERM model are broadly similar to those from UFOTRI - most importantly when considering specifically the terrestrial, atmospheric and hydrological processes and compartments (as opposed to the dispersion model alone).

## 5. Discussion
The TERM model, as described in the model definition section above, can perhaps best be evaluated through a comparison of its simulation results to other models in the literature and/or site data as measured under reference conditions. This was done in the implementation and validation section above, with some discussion for each case. This section will describe the model performance and characteristics in the aggregate.

While the comparisons presented in the preceding section are generally favourable, it should be emphasized that, in both validation sets (i.e. Raskob, 1990; CNSC, 2009), the reference conditions for the release available in the literature were incomplete and had to be supplemented by external data sources and the authors' best interpretation of available information. While such information is often found wanting, and this is therefore not altogether unusual for this type of exercise, an immediate improvement to the work here would be the addition of a better comparison of several reference models under several release types and conditions (so as to extensively test each model). The benefit of the approach taken here is that the authors have elected to use what amount to reference problems (i.e. scenarios) for several well-regarded models in the literature. The advantage of this approach over the alternative, for example constructing one or more new artificial cases, is that these reference cases are known to, and indeed constructed to, pose a legitimate test of model characteristics (which perhaps a new artificial, possibly trivial, problem would not). Through the use of these reference cases, the authors have effectively elected to test TERM's capabilities and differences when contrasted with alternative models on their own 'turf'.

Under continuous release conditions, TERM appears to match the IMPACT model (CNSC, 2009) both in terms of the broad magnitude of concentrations and also the overall pattern of change of these concentrations with position (and thus time), though some differences are apparent, which can likely be attributed either to differences in the conceptual model/implementation, the difference in the site condition data used, or some combination of these two factors. The preceding section examined the sensitivity of the TERM model results to important parameters and discretization effects. Intriguingly, when compared with site measurements, TERM results appear to significantly outperform the literature model as they are distinctly closer to more of the observations, but also on average, much closer to the measurements than the literature model. This indicates that TERM might compare favourably or even outperform existing models in the literature for such scenarios (i.e. continuous release of HTO).

TERM performed in a similar fashion for the discrete HTO release scenario, when compared to the UFOTRI model (Raskob, 1990). Once again, simulation results for both models were of similar magnitude and changed with position (distance from source and angle) in an approximately compatible fashion. The TERM dispersion model was adjusted to match the Raskob (1990) thresholding assumption, illustrating how the underlying conceptual model is not dependent on a particular atmospheric dispersion model, for instance, and can readily be adjusted to new and existing scenarios or selected representations as needed and warranted (e.g. to provide conservative estimates for dose assessments). Such source description parameters are effectively independent from, and do not affect, the conceptual models governing conversion, transport and speciation in the terrestrial and aquatic systems, for example.

The TERM model has thus been shown to be capable of providing reasonable and broadly compatible results to two atmospheric HTO release models from the literature for both continuous and discrete release conditions. The model has also been shown to compare favourably with observed measurements from an actual HTO release.

## 6. Conclusions
A new model of tritium and tritium-species migration through the hydrological cycle was developed and is described in this paper. The model draws on existing tools, but places emphasis on tritiated species to a greater degree than most models in the literature. It is also distinct in its comprehensive capability to model many types and combinations of release scenarios (e.g. discrete vs. continuous, atmospheric vs. river) when compared to existing models. The model implementation was validated against literature models and data, and found to perform adequately. This shows that the forecasting and estimation of HT and HTO in hydrological compartments could be possible - and the validation exercise against atmospheric data is a first step toward such applications. A more detailed model - such as TERM - that focuses on the whole-hydrosphere approach, has significant potential in the assessment and interpretation of environmental concentrations of tritium species in water systems and related biological complexes. Further investigations are planned to explore the potential of the model for engineering applications, including model validation from whole-hydrosphere experimental data.

## References
- Belot, Y., Watkins, B.M., Edlund, O., Galeriu, D., Guinois, G., Golubev, A.V., Meurville, C., Raskob, W., Täschner, M., Yamazawa, H., 2005. Upward movement of tritium from contaminated groundwaters: a numerical analysis. J. Environ. Radioact. 84 (2), 259-270.
- Canadian Nuclear Safety Commission (CNSC), 2009. Investigation of the Environmental Fate of Tritium in the Atmosphere. Prepared by ECOMETRIX and RWDI Air Inc., Report INFO-0792.
- Environment Canada (EC), 2012. Station 4003 Hourly Data. National Climate Data and Information Archive.
- Galeriu, D., Davis, P., Chouhan, S., Raskob, W., 1995. Uncertainty and sensitivity analysis for the environmental tritium code UFOTRI. Fusion Technol. 28, 853-858.
- Galeriu, D., Davis, P., Raskob, W., Melintescu, A., 2008. Recent progresses in tritium radioecology and dosimetry. Fusion Sci. Technol. 54 (1), 237-242.
- Gat, J.R., 2010. Isotope hydrology: a study of the water cycle. Ser. Environ. Sci. Manag. 6.
- Gifford, F.A., 1959. Statistical properties of a fluctuating plume dispersion model. Adv. Geophys. 6, 117-137.
- Hart, D., 2008. Derived Release Limits Guidance. Candu Owner's Group Report 06-3090-R2-I.
- IAEA, 2012. Environmental Modelling for Radiation Safety (EMRAS). A Summary Report of the Results of the EMRAS Programme (2003-2007). In: Modelling the Environmental Transfer of Tritium and Carbon-14 to Biota and Man. IAEA. TEDCOC-1678 Companion CD.
- MATLAB version 7.14, 2012. The MathWorks Inc., Natick, MA.
- Michel, R.L., 2005. Tritium in the hydrologic cycle. In: Aggarwal, P.K., Gat, J.R., Froehlich, K.F.O. (Eds.), Isotopes in the Water Cycle. Springer, pp. 53-66.
- Monteith, J.L., 1965. Evaporation and the environment. In: The State and Movement of Water in Living Organisms, XIXth Symposium of the Society for Experimental Biology, Swansea. Cambridge University Press, Cambridge, UK, pp. 205-234.
- Napier, B.A., Strenge, D.L., Ramsdell Jr., J.V., Eslinger, P.W., Fosmire, C.J., 2004. GENI Version 2 Software Design Document. PNNL-14584. Pacific Northwest National Laboratory, Richland, WA.
- Ota, M., Yamazawa, H., Morizumi, J., Iida, T., 2007. Measurement and modeling of oxidation rate of hydrogen isotopic gases by soil. J. Environ. Radioact. 97 (2-3), 103-115.
- Pasquill, F., 1961. The estimation of the dispersion of windborne material. Met. Mag. 90 (1063), 33-49.
- Raskob, W., 1990. UFOTRI: Program for Assessing the Off-site Consequences from Accidental Tritium Releases. Kooperation von Forschungszentrum Karlsruhe (KFK) Report 4605.
- Raskob, W., 1993. Description of the New Version 4.0 of the Tritium Model UFOTRI Including User Guide. KFK Report 5194.
- Raskob, W., 2007. Test and Validation Studies Performed with UFOTRI and NORMTRL. FZK Report 7281, Karlsruhe, Germany.
- Smith, J.G., Simmonds, J.R. (Eds.), 2009. The Methodology for Assessing the Radiological Consequences of Routine Releases of Radionuclides to the Environment used in PC-CREAM 08. Health Protection Agency Report RPD-058.
- Walley, W.J., Hussein, D.E.D.A., 1982. Development and testing of a general purpose soil-moisture plant model. Hydrology. Sci. J. 27 (1), 1-17.