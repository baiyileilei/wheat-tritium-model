# Post-Accident Radiocesium Uptake in Eastern Oregon Wheat Crops: A Preliminary Estimate Using a Modified "PATHWAY" Model

**Author:** Joshua A. Palotay

**Degree:** Master of Science in Radiation Health Physics

**Institution:** Oregon State University

**Date:** January 10, 2006

**Major Professor:** Kathryn A. Higley

## Abstract

An experimental environmental uptake model was developed for the purpose of estimating the final harvest concentration of contaminant following an acute accidental release of radiocesium onto an eastern Oregon winter wheat crop. The system was developed using the PATHWAY environmental uptake model as presented by Whicker and Kirchner (1987) for its basis. The experimental system was constructed and operated with the STELLA™ modeling software.

Two source terms were considered for the experiment. The first was a mixture of $62.8\%$ $^{137}\mathrm{Cs}$ and $37.2\%$ $^{134}\mathrm{Cs}$, and the second was $^{137}\mathrm{Cs}$ by itself. Both were assumed to be in the form of cesium chloride. These isotopes of cesium were chosen because of their presence within the nuclear industry and as fission products.

A primary alteration to the PATHWAY model was the incorporation of the growing degree day (GDD) concept. This allowed the model to adjust the length of the growing season based on the average temperature to which the crop was exposed. It was found that higher average growing temperatures resulted in increased radiocesium concentrations $(\mathrm{Bq\cdot kg^{-1}})$ in the harvested crop.

The day on which the contaminant was dispersed during the growing season also changed the final harvest concentration. The day during the growing season which results in the highest final concentration is referred to as the optimum day of dispersal (ODD). During the 261 day growing season for winter wheat, with an average temperature of $9.58^{\circ}\mathrm{C}$, the ODD was on day 96 for $^{134/137}\mathrm{Cs}$ and day 85 for $^{137}\mathrm{Cs}$. The area contamination which resulted in a harvest concentration equal to the derived intervention level for radiocesium contaminated foods (1200 $\mathrm{Bq}\cdot \mathrm{kg}^{-1}$) was $1.50 \times 10^{4} \mathrm{Bq}\cdot \mathrm{m}^{-2}$ and $1.43 \times 10^{4} \mathrm{Bq}\cdot \mathrm{m}^{-2}$, respectively.

The exposure rates at $30 \mathrm{cm}$ for $1.50 \times 10^{4} \mathrm{Bq}\cdot \mathrm{m}^{-2}$ ($^{134/137}\mathrm{Cs}$) and $1.43 \times 10^{4} \mathrm{Bq}\cdot \mathrm{m}^{-2}$ ($^{137}\mathrm{Cs}$) were calculated to be $5.05 \times 10^{-5} \mathrm{mR}\cdot \mathrm{hr}^{-1}$ and $6.70 \times 10^{-5} \mathrm{mR}\cdot \mathrm{hr}^{-1}$, respectively, excluding natural background. These levels suggest that conventional area surveys could not detect the level of radiocesium contamination which would require the embargo of an eastern Oregon wheat crop.

---

© Copyright by Joshua A. Palotay January 10, 2006 All Rights Reserved

---

## ACKNOWLEDGEMENTS

I would first like to thank God, the author of all sciences, for giving me the understanding and endurance necessary to complete this work, and to whom this, and all my future work is dedicated. Next, I would like to thank my wife and son for their constant encouragement and support while working to achieve this point in my life. Thanks are also in order to the rest of my extended family and close friends who have offered their time and prayer to assist in my professional goals.

A great deal of thanks and appreciation is owed to my major professor Dr. Kathryn Higley for all the advice and direction she has given over the course of the RHP program. Her contributions and encouragement has helped to refine my abilities, and focus my talents for success within the science and community of health physics.

I would also like to thank Dr. David Hamby and the rest of the faculty in the Department of Nuclear Engineering and Radiation Health Physics. I am very grateful for their patience and availability to assist in my learning and understanding of the science. I also thank Dr. Gwil Evans and members of the OSU College of Agricultural Science. Dr. Evans offered his time to assist me in finding persons and resources which contributed to my thesis research.

I thank all the members of the Radiation Center staff who provided an excellent working environment and assisted in matters of administration. Without their help, my work would have been much more difficult.

Special thanks go to those who agreed to be on my graduate committee: Dr. David Hamby, Dr. Steve Binney, and Dr. Solomon Yim. I appreciate the time they have taken out of their schedules to hear my defense and to review my thesis work.

---

## TABLE OF CONTENTS

1. INTRODUCTION ................................................................................................................ 1
2. LITERATURE REVIEW ..................................................................................................... 8
   2.1 The PATHWAY Model ................................................................................................ 8
   2.2 Wheat and the SPADE Model .................................................................................... 10
   2.3 General Application of the Model .............................................................................. 11
   2.4 Other Environmental Modeling .................................................................................. 12
   2.5 Wheat and the Growing Degree Day Concept .......................................................... 14
3. MATERIALS and METHODS .......................................................................................... 17
   3.1 Model Functions ........................................................................................................ 17
   3.2 Input Constants and Parameters ................................................................................ 25
4. RESULTS .......................................................................................................................... 51
   4.1 Purpose and Introduction of the Experiments ........................................................... 51
   4.2 Experiments and Results: The Harvest Concentration .............................................. 54
   4.3 Experiments and Results: Dose and Exposure .......................................................... 61
   4.4 Sensitivity Analysis ................................................................................................... 64
5. DISCUSSION .................................................................................................................... 67
6. CONCLUSION .................................................................................................................. 71
References .............................................................................................................................. 73
Appendices ............................................................................................................................. 77
   Appendix A: Model Parameters ...................................................................................... 78
   Appendix B: Experimental Model Diagram .................................................................... 79
   Appendix B: Mathematical Relationships ....................................................................... 83
   Appendix C: Dual Isotope Compartment Tabular Values ............................................... 98
   Appendix D: Single Isotope Compartment Tabular Values ........................................... 114

---

## LIST OF FIGURES

2.1 PATHWAY model ........................................................................................................... 9
3.1 Example of compartmental flow .................................................................................... 18
3.2 Soil parameters input table created in STELLA™ ......................................................... 20
3.3 Percolation model created in STELLA™ ....................................................................... 21
3.4 Percolation model with radioactive decay ...................................................................... 22
3.5 GDD relationship to emergence and maturity in STELLA™ ......................................... 24
3.6 Wheat height extrapolation ............................................................................................ 34
3.7 Fraction to soil modeled in STELLA™ .......................................................................... 36
3.8 Radiation detection of a wheat crop ............................................................................... 48
4.1 System dynamic with experimental standard ................................................................. 55
4.2 Compartmental comparisons using experimental standard ............................................ 55
4.3 Dual isotope dynamic comparison on vegetation surface .............................................. 57
4.4 Optimum day of dispersal .............................................................................................. 58
4.5 Dual isotope ratio ($^{137}\mathrm{Cs}/^{134}\mathrm{Cs}$) ................................................................................... 60
4.6 Effects of temperature on radiocesium uptake ................................................................ 61
4.7 Graph of system parameter sensitivities ......................................................................... 65

## LIST OF TABLES

3.1 Monthly mean temperatures ........................................................................................... 31
3.2 Wheat crop time scale .................................................................................................... 33
3.3 Wheat height as a function of temperature ..................................................................... 33
3.4 FGR No. 12 dose rate factors with adjustment for distance ........................................... 50
4.1 Dose and contamination limits ....................................................................................... 62
4.2 Exposure rates from contaminated crops ........................................................................ 64

## LIST OF EQUATIONS

2.1 Growing degree days (GDD) ......................................................................................... 16
3.1 Mathematical relationship between compartments ......................................................... 18
3.2 Surface to labile transfer ................................................................................................ 21
3.3 Biomass of straw per unit surface area ........................................................................... 28
3.4 Harvested biomass per unit surface area ........................................................................ 29
3.5 Total fresh above-ground biomass ................................................................................. 30
3.6 Total number of days to maturity ................................................................................... 32
3.7 Above-ground growth rate ............................................................................................. 35
3.8 Source term fraction to soil and vegetation .................................................................... 36
3.9 Wheat plant growth rate ................................................................................................. 37
3.10 Resuspension ................................................................................................................ 41
3.11 Background exposure rate ............................................................................................ 46
3.12 Adjustment for detection distance from a plane source ................................................ 49
4.1 Source term to equal the background exposure rate ....................................................... 63
4.2 Exposure rate for a given source term ............................................................................ 63
4.3 Parameter sensitivity ...................................................................................................... 65

---

## Chapter 1: INTRODUCTION

The extreme importance of an uninterrupted flow of foodstuffs to a populous goes without question. By mere observation of history, one can see that the total devastation of a crop can bring about local food shortages causing increased prices for the consumer and risk of severe financial loss to the grower. Food shortages or the interruption of supply can occur when its safety for consumption comes into question. Crops can be destroyed or become unfit for human consumption by several means; among them is chemical and/or radiological contamination.

This study examines the radiocesium uptake behavior of eastern Oregon wheat crops using the "PATHWAY" model (Whicker and Kirchner 1987) with alterations made by the author. In particular, the study estimates the total surface deposition of $^{134}\mathrm{Cs}$ and $^{137}\mathrm{Cs}$ necessary to cause the wheat crop to reach a Derived Intervention Level (DIL) of 1200 becquerels per kilogram ($\mathrm{Bq} \cdot \mathrm{kg}^{-1}$) of fresh wheat grain, as determined by the U.S. Food and Drug Administration (2005). Once this limit is reached, the crop is considered no longer suitable for consumption. Research was conducted with three primary objectives in mind: 1) Model the radiocesium uptake of a wheat crop resulting from an acute deposition. 2) Estimate the area contamination to yield the $^{134/137}\mathrm{Cs}$ Derived Intervention Level (DIL). 3) Predict immediate post-dispersal event radiation fields.

The U.S. Food and Drug Administration (FDA) adopted updated guidelines for restricting domestic foods contaminated with radioactivity. The Compliance Policy Guide (CPG) publicized in 1998 suggests limits for radioactive contamination levels in foodstuffs to minimize health risks to the consumer. The new Protective Action Guidelines (PAG) limit a total committed effective dose equivalent (CEDE) of $5\mathrm{mSv}$ or $50\mathrm{mSv}$ to any tissue or organ. At this dose, the chance for an individual to contract cancer is approximately 1 in 4400. By comparison, the chance of contracting cancer during a lifetime is roughly 1 in 5 (U.S. Food and Drug Administration 2005). Therefore, a food commodity must not deliver a dose greater than the established PAG if it is to be released for public consumption.

In the event of a radiologic accident (i.e., reactor event, weapon detonation, or radiological dispersion device), if materials such as radiocesium are deposited over agricultural crops it will become necessary to evaluate the contaminated crops in comparison to the DILs for each contributing nuclide to ensure the health and safety of the consumer. Also, the possibility of a massive financial loss to the grower and local economy must be evaluated and prepared for in the case of a total crop embargo. Both scenarios have the potential to cause great disturbance among a population. In such a situation, public authorities must decide on the fate of contaminated crops by carefully weighing both the health and economic impacts associated with the available options: to embargo, or release to market.

The Food and Agriculture Organization (FAO) of the United Nations identifies six sources from which a radiological accident could pose a threat to agriculture. These sources are listed below in the order of importance (Food and Agriculture Organization of the United Nations 1989, pp. 11):

1) Land-based nuclear power reactors.
2) Mobile marine nuclear power reactors and air or space-vehicles carrying nuclear facilities.
3) Reactors used for research, teaching, and radioisotope production.
4) Fuel processing plants, waste discharges, etc. (especially into aquatic or marine ecosystems).
5) Mining, storage and transport of radioactive materials as part of the nuclear fuel cycle (excluding 4).
6) Nuclear-medical, industrial irradiation, and research facilities.

Another threat that must also be considered in the post 9/11 era is purposely released nuclides onto agricultural crops in an act of terrorism.

In nearly all of the above items listed by the FAO, $^{134}\mathrm{Cs}$ and/or $^{137}\mathrm{Cs}$ can be found as a common component in the overall nuclide profile. Due to the relatively long half lives of the nuclides, 2.062 and 30.0 years respectively, and the highly soluble nature of the cesium ion, these isotopes are important contaminants to consider (Environmental Protection Agency 1988, National Council on Radiation Protection 1977, White and Broadley 2000).

Estimating the contamination concentration of a crop after harvest as a function of total surface contamination immediately after a radiological event can be of help to gauge remedial actions. The local emergency management authorities, community, and growers can forecast the safety of a crop in reference to a dispersal event which may have occurred during the growth period. Such foresight may reduce a premature economic downturn resulting from unnecessary fear of a lightly contaminated crop or provide an early warning for growers in preparation for loss in harvest revenue due to a probable mandatory embargo.

Throughout history wheat has been an important source of nourishment for most people. "Today, wheat is grown on more land than any other commercial crop and continues to be the most important food grain source for humans. Its production leads all crops, including rice, maize and potatoes (Food and Agriculture Organization of the United Nations 2002, pp. 1)." "It is the best of the cereal foods and provides more nourishment for humans than any other food source (Food and Agriculture Organization of the United Nations 2002, pp.2)." Since 1990, the world wheat utilization has remained near 550 million tons with the United States, Canada, France and Australia being the major exporting countries in recent years (Food and Agriculture Organization of the United Nations 2002). Making such a large contribution to the modern diet and agricultural economy, it is for this reason that wheat was selected for the subject of the uptake study.

Wheat can be classified into two categories: spring wheat and winter wheat. The difference is determined by the climatic season in which it is grown. A spring wheat crop is planted during the spring and harvested in late summer. Winter wheat on the other hand is planted in the fall or autumn months and is harvested around mid-summer (Food and Agriculture Organization of the United Nations 2002). The total time in which the winter wheat crop is in contact with the soil, or total growing time, is noticeably longer as compared to spring wheat. This is due to the fact that wheat grows most efficiently in temperatures near to $25^{\circ}\mathrm{C}$ and will cease to grow in temperatures of $0^{\circ}\mathrm{C}$ or less (Food and Agriculture Organization of the United Nations 2002, Cook et al. 2005). Winter wheat, being the most common type of wheat grown in Oregon, is used specifically in this study$^{1}$ (National Information Service for the Regional IMP Centers 2005).

$^{1}$ In 1998, eastern Oregon represented $92.5\%$ of the winter wheat growing acreage (National Information Service for the Regional IMP Centers 2005).

The PATHWAY model is based on a compartment-type system which estimates the flow of contaminants from one compartment to another through a series of differential equations. The model expresses the change in time in units of days (Whicker and Kirchner 1987). This unit is useful when average rates of uptake and migration for a contaminant are known. However, the growth and development of a plant depends highly on the climatic temperatures to which it is exposed (Wikipedia 2005). This becomes important since the PATHWAY model only considers plant growth as an average rate in units of day$^{-1}$.

The use of an average growth rate becomes problematic because of the temperature differences that can be observed from one agricultural region to another. The average growth rates for any crop or plant species will only reflect the characteristics of the sample group. Since growth rate can be considered a function of ambient temperature, it becomes necessary to address a specific climate if a particular agricultural region is being considered.

As stated earlier, wheat will stop actively growing at or below $0^{\circ}\mathrm{C}$. Depending on the climatic trend and season, wheat growth can be affected and change from one day to the next. Therefore, the author has incorporated the concept of growing degree days (GDD) into the model. By doing so, the model is made more adaptable to the growth characteristics of a given crop in a specific temperature climate. The growing degree day is a unit of accumulated heat over a given time period (Cook et al. 2005). Every plant or crop species has a unique number of total growing degree days necessary for it to reach physical maturity. With this addition, the output values of the PATHWAY model can be viewed as a function of temperature as it relates to nuclide uptake and plant growth. Though the base unit of (days) remains as the change in time for the overall equation, the integrated parameter of temperature regulates the speed of growth and the total time in which the plant remains in contact with the contaminant by dictating the length of the growing season.

Foliar absorption has been recognized as a significant, if not the most significant, contributor of radionuclide uptake in plants especially for $^{134}\mathrm{Cs}$ and $^{137}\mathrm{Cs}$ (White and Broadley 2000). The added parameter of temperature will determine when, how long, and to what magnitude the plant surfaces (i.e. leaves and foliage) are available for contaminant interception based on the amount of above-ground biomass that has emerged from the soil at a given point in time as is allowed by the rate of growth.

The ability to adjust for climate in an uptake model is important for concentration predictions of crops grown in a geographically diverse state such as Oregon. Growing conditions can vary greatly from one area of the state to another like those of the temperate Willamette Valley to the high desert environment of eastern Oregon. Standardized variables are good reference points for an initial estimation; however, once the point of study becomes specific, so too must the input variables be specific to that point. Uptake models should be constantly revised to allow for greater flexibility and ease of use. By making the length of the growing season a function of temperature, much of the guess work is removed for estimating the growing period of a crop if the number of growing degree days required to reach physical maturity is known. This allows for a better estimate of the total time in which the plant is in contact with the contaminant before harvest.

---

## Chapter 2: LITERATURE REVIEW

### 2.1 The PATHWAY Model

The work of F. Ward Whicker and T. B. Kirchner (1987), has resulted in the development of a radionuclide uptake model for food crops using a "dynamic" compartment-type transfer methodology. Each environmental component such as the surface soil, vegetation tissues, and deep soil are treated as compartments or basins in which the contaminant collects. The PATHWAY model uses a set of numerical constants such as plant growth, weathering, foliar absorption and soil leaching to determine the movement of the contaminant from one compartment to the other. The concentration of the radioactive contaminant in any compartment can be determined at a given time by applying the constants to groups of differential equations, which are related by a series of linear operations to represent the system as a whole (Whicker and Kirchner 1987).

The PATHWAY model (Figure 2.1) uses many average input constants to give generic values for a number of different crops with a variety of source terms. Although the parameters provided by the authors of the PATHWAY model can offer a prediction for crop concentrations, they are only truly representative of the environment in which they were modeled. Though the PATHWAY model, as published, was tuned to a specific geographical region (the Nevada Test Site), it has the flexibility to be adapted to other regions with differing environmental conditions (Whicker and Kirchner 1987).

The PATHWAY model can be adjusted for a variety of diverse agricultural situations by merely changing the numerical constants within the compartmental equations to be representative of the area in question. By allowing for such flexibility inherent in the model, Whicker and Kirchner (1987), provide an excellent tool to the scientific community for evaluating a variety of agricultural contamination situations and new modeling techniques. This thesis research takes the flexible nature of the PATHWAY model and adapts it to a specific agricultural environment.

**Figure 2.1** PATHWAY model. Reprinted with permission (Whicker and Kirchner 1987, pp. 719)

### 2.2 Wheat and the SPADE Model

A similar work (Jackson et al. 1987) to PATHWAY use the Soil Plant Animal Dynamic Evaluation (SPADE) model, a compartmental-type uptake model, to simulate a variety of deposition scenarios and predict the concentration of various radionuclides in a number of crops and other foodstuffs. Among these scenarios is an acute release, deposition, and uptake of $^{137}\mathrm{Cs}$ in a generic cereal crop (Jackson et al. 1987).

In one example the authors examined a "spike deposition" (Jackson et al. 1987, pp.146) scenario totaled $3.15 \times 10^{7} \mathrm{~Bq} \cdot \mathrm{m}^{-2}$ of $^{137}\mathrm{Cs}$ onto the surface. In this simulation the contaminating event is acute and discrete, occurring at time equals zero of the model which represents the beginning of the growing season. At the end of 120 days the model resulted in a concentration of $4.8 \times 10^{6} \mathrm{~Bq} \cdot \mathrm{kg}^{-1}$ (fresh weight) in cereals (Jackson et al. 1987).

According to Jackson et al. (1987), results generated from the $^{137}\mathrm{Cs}$ simulation corresponded well to field data of concentration ratios in a variety of food products. The authors stated there was some discrepancy between the data for cereal crops. However, they note that this could be due to assumptions made about the contribution from the husk. The authors conclude, based on the comparative date between the generated results and the field data that the model appears to have credibility (Jackson et al. 1987). Therefore, the values given by the SPADE model in the previous simulation seem to make a reasonable point of reference from which to evaluate the results of the experimental model.

### 2.3 General Application of the Model

The PATHWAY model by Whicker and Kirchner (1987), was used as the framework for the experimental model developed by this author. In essence, it is nearly identical to PATHWAY with some slight variation to suit the specific situation being simulated. Some of the PATHWAY parameters and flow dynamics were altered for this purpose. One of the more pronounced changes to the PATHWAY model was the incorporation of growing degree days (GDD). This parameter adjusts the total length of the growing season, providing the day which the crop will reach full maturity as a function of the average temperature during the growing season. In this way, the expected duration of crop uptake becomes elastic and dependent on climate trend as compared to using a more rigid crop-specific average growing time. The details of this and other adjustments to the model will be discussed in detail later on in the document.

The general approach used in the SPADE model is very similar to that used in the PATHWAY model. The exact parameters used for the numerical constants utilized by Jackson et al. (1987), were unknown to the author of this thesis. However, due to its agreement with field observations and similarities to the PATHWAY methodology, the output of the SPADE model was used as a benchmark for the outputs generated by the experimental model.

It is the author's opinion that through the use of the PATHWAY model and the reference output provided by the SPADE model, as utilized by Jackson et al. (1987), a fairly accurate prediction for the behavior of cesium in eastern Oregon wheat crops can be made. This is done by altering the PATHWAY parameters to more closely match the conditions likely to be observed in the eastern Oregon climate. With the new experimental model tuned to agricultural conditions of the area in question, the total surface deposition required to cause the wheat grain to reach the DIL can then be determined.

### 2.4 Other Environmental Modeling

There are several other environmental uptake and transport models being used in experimental settings. Starting in 1996, a large scale effort was made to assess and improve several models being developed around the globe. The International Atomic Energy Agency began a program called the Biosphere Modeling Assessment (BIOMASS) for this purpose. The program ran a scenario simulating the 1986 Chernobyl accident, releasing $^{137}\mathrm{Cs}$ into the environment. The program evaluated $^{137}\mathrm{Cs}$ distribution, transport, and several pathways for human internal and external dose. The simulation also considered the uptake of $^{137}\mathrm{Cs}$ in several crops (International Atomic Energy Agency, 2003).

The program incorporated various models developed by scientists from around the world. The models used slightly different means to provide a dynamic simulation of the source term moving through the environment and assorted pathways. The IAEA report gives somewhat of a cross section for the current state of radiologic modeling and showcases the performance of several models. Some of the models involved in this work were:

- RadCon (Radiological Consequences) model from the Australian Nuclear Science and Technology Organization.
- TAMDYN-UV model from the University of Veszprém, Hungary.
- CLRP (Concentration Levels Rapid Predictions) model from the Central Laboratory for Radiological Protection, Department of Radiation Hygiene, Warsaw, Poland.
- SPADE (Soil Plant Animal Dynamic Evaluation) model from the group presently known as the Food Standards Agency, United Kingdom.
- ECOMOD model from the SPA, "Typhoon," Obninsk, Russia.

This collaboration of environmental transport models provide a summary of current and developing tools for radiologic assessment and allows one to compare and contrast the results generated by each. (International Atomic Energy Agency, 2003)

In general, the majority of the parameter categories used in the above models appeared analogous to those used in the PATHWAY model. The models used similar compartment-based, differential processes to evaluate the extent of contamination with different software codes. The information given in the IAEA report about the various models illustrated that though computational technology has changed over time, the general compartmental or layered approach to environmental modeling remains somewhat constant within the realm of uptake analysis. (International Atomic Energy Agency, 2003)

### 2.5 Wheat and the Growing Degree Days Concept

Due to the agricultural nature of this study it was necessary for the author to understand the development of wheat crops and how they are grown for purposes of consumption. Several works specific to the cultivation of wheat crops were consulted. The text "Bread Wheat" published by the Food and Agriculture Organization of the United Nations (1989), provided a wealth of information on the subject. This information is helpful not only to better comprehend wheat cultivation, but also to give perspective on wheat production in the state of Oregon.

Wheat is grown all over the world, in a wide variety of environments. In general, wheat is grown in two seasons: spring and winter. In eastern Oregon, it is the winter variety that is most commonly grown. The winter wheat crop is planted in fall or autumn. During the cold months the growth of the wheat slows down and comes to a halt once $0^{\circ}\mathrm{C}$ is reached (Cook et al. 2005, Food and Agriculture Organization of the United Nations 2002). During this time the wheat remains in a vegetative state until the ambient temperature increases. Typically, a winter wheat crop will reach full physical maturity sometime around mid-summer (Food and Agriculture Organization of the United Nations 2002).

Plant growth is a cumulative process, contingent upon the surrounding temperature climate (Wikipedia 2005). This makes the rate of growth and time to maturity variable, depending on the local climatic trends of the agricultural region in question. Yearly trends and fluctuation in average temperature can alter the total time of growth from one season to the next, introducing error into a standard growth coefficient. This is where the concept of growing degree days can aid in estimating contamination uptake while taking into consideration regional and trend-based temperature changes.

The growing degree day is a unit of accumulated heat over a given time period (Cook et al. 2005). Every plant or crop species has a unique number of total growing degree days necessary for it to reach physical maturity. Rao et al. (2000), reported that wheat takes an average of 2500 growing degree days (GDD) to become fully mature. It also can be used to mark different stages of development. For example, it takes an accumulated $180^{\circ}\mathrm{C}$ after planting for a wheat plant to emerge from the soil (or time to emergence) (Cook et al. 2005).

However, this accumulation of heat only considers the contributing temperatures. These temperatures are those whose value is greater than the temperature at which a specific plant becomes vegetative. This temperature is known as the baseline temperature and must be subtracted from the calculated average temperature per unit time (Wikipedia 2005). As with the GDD required to reach maturity, each plant species has its own unique temperature where growth will not occur or is severely reduced. Baseline temperatures used for wheat range from $0^{\circ}\mathrm{C}$ to $10^{\circ}\mathrm{C}$ (Cook et al. 2005, Food and Agriculture Organization of the United Nations 2002, Wikipedia 2005). In the work prepared by Cook et al. (2005), a baseline temperature of $0^{\circ}\mathrm{C}$ is used for the GDD calculations for wheat grown in northeastern Oregon; therefore, this baseline temperature is used for the study.

$$GDD = \frac{\text{High temperature}(^{\circ}\mathrm{C}) + \text{Low temperature}(^{\circ}\mathrm{C})}{2} - \text{Baseline}$$

**Equation 2.1** Growing degree days (GDD).

The GDD is an average of temperatures which contribute to the growth of the plant. The accumulated number of growing degree days is the integral of the average contributing temperature with respect to time. As stated above, wheat requires a standard 2500 GDD to reach maturity. If the average daily temperature is low, the total time to reach maturity will be greater than if the average temperature were higher. Thus, the higher average ambient temperatures result in a shorter growing period from planting to maturity, and vice versa.$^{2}$

$^{2}$ The baseline temperature of $0^{\circ}\mathrm{C}$ means that any day with an average temperature $\leq 0^{\circ}\mathrm{C}$ contributes zero GDD.

---

## Chapter 3: MATERIALS and METHODS

### 3.1 Model Functions

This section discusses the general operation of the PATHWAY model and the software used to generate the PATHWAY-based experimental model. A more detailed description of the parameters and constants used will be discussed in section 3.2. The mathematical expressions generated by the STELLA™ software representing the experimental model and its components can be reviewed in Appendix B. This includes a map of the model circuitry for visual reference.

#### 3.1.1 The PATHWAY Concept

The PATHWAY model uses the compartment concept to account for and simulate the movement of radionuclides from one environmental compartment to another (Whicker and Kirchner 1987). An example would be the movement of radionuclides down through the soil system. As shown in figure 3.1, radioactivity from the initial contaminating event settles onto the surface soil. From there it will begin to accumulate into the labile soil as indicated by the direction of the arrow (direction of flow) where it becomes available for root uptake. Once in the labile compartment, the radioactivity splits its movement into two directions. It can go into either the fixed soil where it binds minerals or into the deep soil where it is beyond the physical reach of the root system. The movement of contaminant between the labile and fixed compartments is a cyclical process. In such case, radioactivity is simultaneously and continuously transferred between these compartments at specified rates (Whicker and Kirchner 1987).

**Figure 3.1** Example of compartmental flow.

The movement of radioactivity between compartments is a continual process characterized by sets of first order differential equations (Whicker and Kirchner 1987). The mathematical description for the movement between individual compartments as described by Whicker and Kirchner (Whicker and Kirchner 1987, pp. 720) is shown below in equation 3.1.

$$Q^{\prime}_h = \sum_{i=1}^{n} R_{\text{in},i} - \sum_{j=1}^{m} R_{\text{out},j}$$

where,
$Q^{\prime}_h$ is "the time derivative of the radionuclide in compartment $h$"
$R_{\text{in},i} =$ "$i$th inflow rate to compartment $h$, $\mathrm{Bq\ m^{-2}\ d^{-1}}$"
$R_{\text{out},j} =$ "$j$th outflow rate from compartment $h$, $\mathrm{Bq\ m^{-2}\ d^{-1}}$"

**Equation 3.1** Mathematical relationship between compartments.

PATHWAY considers all the inter-compartmental flow processes as a series of interlocked differential equations. The equations are solved based on a change in time with units of $(\mathrm{d}^{-1})$. The solution yields a contaminant inventory for each compartment $(\mathrm{Bq}\cdot \mathrm{m}^{-2})$ at a given point in time (Whicker and Kirchner 1987). The $4^{\mathrm{th}}$ order Runge-Kutta algorithm is used by Whicker and Kirchner (1987), to compute the activity within the various compartments of the system. This algorithm was also used as the computational basis in the experimental model.

#### 3.1.2 The STELLA® Modeling Tool

The experimental model was built and operated in a modeling software package called STELLA™ version 8.1.4 from isee™ systems. The software allows compartment-type models (such as PATHWAY) to be built on a user interface called the model construction layer, using a menu of construction tools. The tools allow a model to be designed through graphic representations (Appendix B). In addition, the software has a high-level mapping layer which allows the user to break the total model up into usable sections. This layer also allows the user to interact with the model through a series of available input tools such as input tables, on-off buttons, and adjustment knobs. The user can also view the calculated outputs and specified results through dynamic tables and graphical displays.

STELLA™ allows models using ordinary first order differential processes to be calculated using the Euler, Runge-Kutta 2 and Runge-Kutta 4 methods. As the model is constructed, it generates a mathematical expression for each compartment characterizing the incoming and outgoing flow of contamination (Appendix B: Mathematical Relationships) (isee™ systems, Inc. 2005a, isee™ systems, Inc. 2005b).

**Figure 3.2** Soil parameters input table created in STELLA™.

Above in figure 3.2 is an image of an input table used for the experimental model as generated in the high-level mapping layer of the STELLA™ software (isee™ systems, Inc. 2005a). In the left-hand column are the names of various input constants. The right-hand column contains the corresponding input value in units of $(\mathrm{d}^{-1})$ with the exception of the rooting zone (meters). A specific table was generated for four groups of input constants: source term, plant variables, soil parameters, and ingestion.

A basic construction diagram using the STELLA™ software is shown below in figure 3.3 along with the corresponding mathematical equation as automatically generated by the software. The process illustrated is that of radioactivity migrating from the surface soil compartment to the labile soil compartment. STELLA™ refers to the compartments as "stocks," the flow arrow as a "flow," and the circle containing the rate constant as a "converter". The smaller arrows called "connectors," indicates mathematical relationships between values, where as the larger flow arrow indicates the direction of exchange between compartments (isee™ systems, Inc. 2005a).

**Figure 3.3** Percolation model created in STELLA™.
