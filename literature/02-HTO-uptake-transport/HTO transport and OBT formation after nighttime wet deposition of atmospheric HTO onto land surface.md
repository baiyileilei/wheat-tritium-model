# HTO transport and OBT formation after nighttime wet deposition of atmospheric HTO onto land surface

**M. Ota and H. Nagai**

*Japan Atomic Energy Agency, Tokai, Ibaraki, Japan*

**Abstract.** To quantitatively evaluate OBT production after a nighttime wet deposition of atmospheric HTO onto land surface, numerical experiments using a sophisticated tritium transport model (SOLVEG-II) were conducted. For a nighttime rain actually observed at a grassland site, two hypothetical scenarios for wet deposition of HTO were made; 0.1-folded and 10-folded case, each having rain HTO concentration at 0.1 folds and 10 folds of equilibrium concentration of ground-level air HTO concentration. Calculation results showed atmospheric HTO concentration after the rain at 10-folded case was more than an order of magnitude larger than that at 0.1-folded case, affected by interception and evaporation of rain HTO with leaves, and, by a larger HTO re-emission from soil. After the rain, due to these heightened atmospheric HTO, TFWT concentration in leaf cellular water at 10-folded case kept an order, or more, larger than that at 0.1-folded case. As a result, OBT produced in leaves over nine-day after the rain at 10-folded case was 18 times larger than that at 0.1-folded case. We therefore concluded that nighttime wet deposition of HTO pronouncedly increases OBT formation if rain HTO concentration exceeds equilibrium concentration for the air HTO near the ground.

## 1. INTRODUCTION

Formation of organically-bound tritium (OBT) is a key process for safety assessment for tritium release, since dose from tritium is largely dominated by ingestion of OBT [1, 2]. After HTO release to the atmosphere, as shown in Fig. 1, atmospheric HTO in vegetation canopy deposits into leaf interior through stomata and cuticle. Tissue free water tritium (TFWT) in leaf cellular water then becomes OBT through photosynthesis [3]. Atmospheric HTO also deposits into soil, and after the passage of the primary plume re-emission of the deposited HTO increases atmospheric HTO concentration (secondary plume) [4, 5]. In case of nighttime HTO release, OBT formation may be dominated by the secondary plume, because OBT is formed daytime at which the primary plume has already disappeared and in turn the secondary plume exists. In addition, if rain occurred during the passage of the primary plume, OBT formation at the re-emission phase would be further increased due to a larger re-emission flux caused by a heightened soil HTO concentration through the wet deposition [6, 7]. Although we have these theoretical concerns for aftereffects of nighttime wet deposition on the successive OBT formation, we still have no quantitative conclusions on this because of the difficulties in conducting field experiments on nighttime wet deposition and successive OBT formation. The present study therefore aims to quantitatively evaluate OBT formation after a nighttime wet deposition of HTO. Then we conducted numerical experiments assuming a hypothetical nighttime wet deposition of HTO, by using a sophisticated tritium transport model for land surface ecosystem SOLVEG-II [8-10] in which HTO transfers related to wet deposition are newly modeled.

## 2. MODEL DESCRIPTION

In the employed model SOLVEG-II, atmosphere including vegetation canopy and soil are divided into sub-layers and tritium transfers shown in Fig. 1 are calculated by cooperating with transfer for momentum, heat and water [8], and, exchanges for $\mathrm{CO}_2$ [9, 10]. In the atmospheric sub-model [10],

*[Figure 1]* Land surface tritium transfer (black arrows) and exchanges (white arrows) considered in SOLVEG-II.

atmospheric HTO vapor concentration $\chi_a$ $(\mathrm{Bq}\,\mathrm{m}^{-3})$ is calculated by a diffusion equation:

$$
\frac{\partial\chi_a}{\partial t} = \frac{\partial}{\partial z} K\frac{\partial\chi_a}{\partial z} + a(E_{stom} + E_{ls}) + e_{rain} \tag{1}
$$

where $t$, $z$, $K$ and $a$ respectively are time (s), vertical coordinate (m), turbulent diffusivity $(\mathrm{m}^2\,\mathrm{s}^{-1})$ and leaf area density $(\mathrm{m}^2\,\mathrm{m}^{-3})$ of vegetation canopy. Source term $a(E_{stom} + E_{ls})$ expresses HTO exchanges between the canopy air and leaf cellular water, and, between the canopy air and leaf surface water, each having HTO flux $E_{stom}$ and $E_{ls}$ $(\mathrm{Bq}\,\mathrm{m}^{-2}\,\mathrm{s}^{-1})$ for unit leaf area. Term $e_{rain}$ $(\mathrm{Bq}\,\mathrm{m}^{-3}\,\mathrm{s}^{-1})$ expresses HTO exchange between atmosphere and rainwater. In the soil sub-model [8], gaseous and aqueous HTO concentration, $\chi_{sa}$ and $\chi_{sw}$ $(\mathrm{Bq}\,\mathrm{m}^{-3})$, in soil are calculated by diffusion/advection equations as:

$$
\frac{\partial\eta_s\chi_{sw}}{\partial t} = -\frac{\partial E_w\chi_{sw}}{\partial z} +\frac{\partial}{\partial z}\left(D_{sw}\frac{\partial\chi_{sw}}{\partial z}\right) - e_b - e_r \quad \text{for aqueous} \tag{2}
$$

and

$$
\frac{\partial\left\{\left(\eta_{sat} - \eta_s\right)\chi_{sa}\right\}}{\partial t} = \frac{\partial}{\partial z}\left(D_{sa}\frac{\partial\chi_{sa}}{\partial z}\right) + e_b \quad \text{for gaseous} \tag{3}
$$

where $\eta_s$, $\eta_{sat}$, $E_w$ $(\mathrm{m}^3\,\mathrm{m}^{-2}\,\mathrm{s}^{-1})$, $D_{sw}$, $D_{sa}$ $(\mathrm{m}^2\,\mathrm{s}^{-1})$, $e_b$ and $e_r$ respectively are volumetric soil water content, porosity, water flux, effective diffusivity for aqueous and gaseous HTO, HTO evaporation $(\mathrm{Bq}\,\mathrm{m}^{-3}\,\mathrm{s}^{-1})$ and root-uptake $(\mathrm{Bq}\,\mathrm{m}^{-3}\,\mathrm{s}^{-1})$. Equations (2) and (3) are connected through the evaporation $e_b$, termed as a volumetric sink for aqueous and source for gaseous. The soil and atmospheric sub-models are connected at the ground surface through HTO vapor exchange and downward aqueous HTO input by rain. In the vegetation sub-model [10], TFWT concentration $\chi_v$ $(\mathrm{Bq}\,\mathrm{m}^{-3})$ in leaf cellular water is calculated by:

$$
\frac{\partial\eta_v\chi_v}{\partial t} = E_{stom} + E_{root} + E_{phot} - E_{res} \tag{4}
$$

where $\eta_v$ are leaf cellular water content in unit leaf area $(\mathrm{m}^3\,\mathrm{m}^{-2})$, and fluxes $E_{stom}$, $E_{root}$, $E_{phot}$ and $E_{res}$ $(\mathrm{Bq}\,\mathrm{m}^{-2}\,\mathrm{s}^{-1})$ in unit leaf area respectively express HTO exchange between the canopy air and leaf cellular water through stomata and cuticle, gain of HTO through root-uptake of aqueous HTO in soil, photosynthetic OBT production and decomposition of OBT into TFWT through respiration. Exchange flux $E_{stom}$ is introduced to the atmospheric sub-model by Eq. (1). Physiological variables (conductance for transpiration, photosynthesis, respiration and transpiration rate) needed for calculating these HTO fluxes in r.h.s. of Eq. (4) are determined by the vegetation sub-model for $\mathrm{CO}_2$ in SOLVEG-II [9]. For these original SOLVEG-II, in the present study, to simulate wet deposition, we newly modeled HTO exchange between rainwater and atmosphere (term $e_{rain}$ in Eq. (1)), and, HTO exchange between canopy air and liquid water existing on leaf surface (flux $E_{ls}$ in Eq. (1)).

## 3. NUMERICAL EXPERIMENTS

### 3.1 Site, input meteorological data and OBT definition

To simulate tritium dynamics in land surface ecosystems, transport of heat, water and $\mathrm{CO}_2$ incorporation by plants should be precisely assessed, since they largely affect HTO transfer and OBT formation [2, 3] and [10]. Then numerical experiments were conducted under actually-observed meteorological conditions at a grassland site (AmeriFlux site in Oklahoma), at which performance of SOLVEG-II for heat, water and $\mathrm{CO}_2$ calculations has been validated [9]. In our calculation, atmosphere (model top at $z = 12\,\mathrm{m}$), including vegetation canopy over $z = 0 - 0.7\,\mathrm{m}$, was divided into ten layers and underlying soil (model bottom at $z = -2\,\mathrm{m}$) was divided into 14 layers. See the literature [9] for more detailed site descriptions and model settings. Half-hourly averaged observed meteorological data were used as input atmospheric variables at the model top. Among the meteorological data set we selected nighttime rain for our analysis; 1.0, 0.6, $1.0\,\mathrm{mm}\,\mathrm{h}^{-1}$ each observed at 20:00–20:30, 20:30–21:00, 22:30–23:00 in Aug. 7, 1999 LST.

Amount of OBT was evaluated by a net OBT produced in unit leaf area, $A_{OBT}$ $(\mathrm{Bq}\,\mathrm{m}^{-2})$, as:

$$
A_{OBT} = \int (E_{phot} - E_{res})dt \tag{5}
$$

where $E_{phot}$ and $E_{res}$ $(\mathrm{Bq}\,\mathrm{m}^{-2}\,\mathrm{s}^{-1})$ are defined in Eq. (2).

### 3.2 Wet deposition scenarios

We assumed a scenario that the rain occurred during passage of a primary plume. Hence input air HTO concentration $\chi_{a,top}$ at the top atmosphere $(z = 8 - 12\,\mathrm{m})$, corresponding to the HTO concentration in the primary plume, was set to be $\chi_{a,top} = 1\,\mathrm{Bq}\,\mathrm{m}^{-3}$ during the rain (20:00–21:00 and 22:30–23:00). Other than these periods, $\chi_{a,top}$ was set to be zero. To simulate wet deposition, rain HTO concentration $\chi_{r,top}$ at the top atmosphere should be given. However, $\chi_{r,top}$ depends on wash out which occurs at a higher altitude beyond SOLVEG system. Concerned with this matter, Belot [6] reported rain HTO concentration at ground level ranges from 0.1 folds to 10 folds of the equilibrium concentration for the air HTO concentration at the ground. Here, 0.1-folded case corresponds to, for example, a situation where the plume reaches to the ground and ground level air HTO is highly concentrated. Conversely, 10-folded case corresponds to a situation when the plume remains up in the air. We then made two scenarios. For the reference air HTO concentration $\chi_{a,top} = 1\,\mathrm{Bq}\,\mathrm{m}^{-3}$-air, equilibrium concentration $\chi_{eq,top}$ was calculated, being $\chi_{eq,top} = 50\,\mathrm{kBq}\,\mathrm{m}^{-3}$-water in this study. Then $\chi_{r,top}$ for the objective rain was assumed to be $5\,\mathrm{kBq}\,\mathrm{m}^{-3}$-water at 0.1-folded case and $500\,\mathrm{kBq}\,\mathrm{m}^{-3}$-water at 10-folded case. Numerical experiments were independently performed for these two cases.

## 4. RESULTS AND DISCUSSION

### 4.1 Leaf surface HTO and atmospheric HTO during rain

During rain, leaf surface water (liquid water existing on the leaf surface) increased through the rain interception with leaves, and HTO exchange between the canopy air and the leaf surface water occurred. At 10-folded case, HTO in the leaf surface water evaporated to the canopy air and then the canopy air HTO concentration $\chi_a$ increased up to $4 - 5\,\mathrm{Bq}\,\mathrm{m}^{-3}$ (Fig. 2(a)). At 0.1-folded case, on the other hand, $\chi_a$ unchanged from the air HTO concentration in the primary plume at $1\,\mathrm{Bq}\,\mathrm{m}^{-3}$ since HTO concentration in the leaf surface water was low and HTO exchange between the canopy air and the leaf surface water was quite small.

### 4.2 Soil HTO, HTO vapor flux at soil/atmosphere interface and atmospheric HTO

Leaf surface HTO became almost zero at several hours after the rain, and thereafter HTO re-emission from soil affected canopy air HTO concentration. During the rain, affected by HTO deposition, aqueous HTO concentration $\chi_{sw}$ in soil near the surface increased. At the end of the rain, $\chi_{sw}$ at 10-folded case was 40 times larger than $\chi_{sw}$ at 0.1-folded case. Here, the difference in $\chi_{sw}$ between the two cases is not exactly two-order of magnitude (difference in $\chi_{r,top}$ between the two cases, see section 3.2), since at 0.1-folded case dry deposition also increased $\chi_{sw}$. After the end of the rain, these aqueous HTO near surface diffused downward and $\chi_{sw}$ near the surface decreased, being nearly two-order of magnitude smaller value at nine-day after the rain. Affected by $\chi_{sw}$, HTO vapor flux $F_0$ at the ground surface after the rain at 10-folded case was 40-fold of $F_0$ at 0.1-folded case (Fig. 2(b)), and $F_0$ at both cases decreased by two orders of magnitude over the nine-day re-emission phase. Hence, during the nine-day re-emission phase, affected by these $F_0$, canopy air HTO concentration $\chi_a$ at 10-folded case was 40 folds of that at 0.1-folded case and $\chi_a$ at both cases continues decrease (Fig. 2(a)).

### 4.3 TFWT concentration and OBT amount

Transpiration conductance $g_d$ at night (e.g. $19\,\mathrm{h} < \mathrm{t} < 30\,\mathrm{h}$ in Fig. 2(c)) was two–three orders of magnitude smaller than daytime $g_d$, because stomata closed and cuticle having greater resistance regulated transpiration. After the start of solar radiation at $30\,\mathrm{h}$, stomata opened and $g_d$ increased. During the rain TFWT concentration $\chi_v$ increased, and $\chi_v$ decreased after the end of rain (Fig. 2(d)). Increase in $\chi_v$ during the rain was caused by the atmospheric HTO deposition into the leaf cellular water through cuticle, driven by the HTO vapor pressure deficit across the two sites. Deposition flux at 10-folded case was larger than that at 0.1-folded case, since at 10-folded case canopy air HTO concentration $\chi_a$ was heightened through HTO release from leaf surface water (section 4.1). As a result, during the rain, $\chi_v$ at 10-folded case increased more pronouncedly than $\chi_v$ at 0.1-folded case. After the end of rain, as $\chi_a$ decreased, TFWT transpired to the canopy air and $\chi_v$ decreased. Due to the smaller $g_d$ at night, this decrease in $\chi_v$ is moderate and $\chi_v$ has not equilibrated with $\chi_a$ until $38\,\mathrm{h}$. Thereafter, $\chi_v$ kept almost equilibrium with $\chi_a$ and hence $\chi_v$ at 10-folded case kept 40 folds of $\chi_v$ at 0.1-folded case, affected by the difference in $\chi_a$ between the two cases (section 4.2).

As photosynthesis rate $A_n$ started increase at $30\,\mathrm{h}$ (Fig. 2(c)), OBT amount $A_{OBT}$ began increase (Fig. 2(e)). Increase in $A_{OBT}$ became smaller as time passed (see also Table 1), as $\chi_v$ decreased throughout the re-emission phase. Affected by the magnitude of $\chi_v$, increase in $A_{OBT}$ is more pronounced at 10-folded case and $A_{OBT}$ at 10-folded case at $240\,\mathrm{h}$ (nine days after the rain) is 18 times larger than that at 0.1-folded case (Table 1). We therefore conclude that nighttime wet deposition having larger rain HTO concentration increases OBT production by an order or more.

We further evaluate effects of re-emission from soil on the OBT formation after the rain. Since $\chi_v$ has not equilibrated with $\chi_a$ until $38\,\mathrm{h}$, OBT synthesized by $38\,\mathrm{h}$ is mainly affected by the atmospheric HTO deposition to the leaf cellular water during the rain. At 0.1-folded case, $A_{OBT}$ at $38\,\mathrm{h}$ accounts for $74\%$ of $A_{OBT}$ at $240\,\mathrm{h}$ (Table 1). On the other hand, at 10-folded case, $A_{OBT}$ at $38\,\mathrm{h}$ accounts for only $29\%$ of $A_{OBT}$ at $240\,\mathrm{h}$. These results mean HTO deposition to leaf cellular water during the rain almost dominated successive OBT formation at 0.1-folded case, while HTO re-emission from soil was more effective for the OBT production at 10-folded case.

*[Figure 2]* Time series for canopy air HTO concentration $\chi_a$ (a), HTO vapor flux $F_0$ upward positive at soil/atmosphere interface (b), transpiration conductance $g_d$ and photosynthesis rate $A_n$ (c), TFWT concentration $\chi_v$ (d), and OBT amount $A_{OBT}$ (e). Variables $\chi_a$, $g_d$, $A_n$, $\chi_v$ and $A_{OBT}$ are the mean over the canopy $z = 0 - 0.7\,\mathrm{m}$. Arrows indicate the time when the rain occurred.

**Table 1.** OBT amount at several stages after the rain.

| Elapsed time from 00:00 on the day of rain | OBT amount $A_{OBT}$ $(\mu\mathrm{Bq}\,\mathrm{m}^{-2})$ (0.1-folded case) | OBT amount $A_{OBT}$ $(\mu\mathrm{Bq}\,\mathrm{m}^{-2})$ (10-folded case) |
|:--------------------------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 38 h                                        | 2.5                                                                 | 18.2                                                                |
| 48 h                                        | 2.6                                                                 | 25.2                                                                |
| 144 h                                       | 3.3                                                                 | 55.3                                                                |
| 240 h                                       | 3.4                                                                 | 61.7                                                                |

## 5. CONCLUSION

OBT formation after a nighttime wet deposition of HTO is quantitatively evaluated through numerical experiments using a sophisticated tritium transport model. When the rain HTO concentration is an order of magnitude smaller than the equilibrium concentration of the ground level air HTO (0.1-folded case), OBT formation is affected mainly by the atmospheric HTO deposition into the leaf cellular water during rain and increase in OBT amount at the re-emission phase is rather small. On the other hand, if rain HTO concentration exceeds equilibrium of the ground level air HTO by an order (10-folded case), TFWT concentration is considerably heightened through interception and evaporation of rain HTO with leaves and through larger HTO re-emission from soil after the rain. As a result OBT amount after the rain at 10-folded case become an order of magnitude, or more, larger than that at 0.1-folded case. We therefore conclude that wet deposition of HTO considerably increases successive OBT production when the rain HTO concentration exceeds equilibrium concentration for the ground level air HTO concentration.

## References

[1] W. Gulden and W. Raskob, Fusion Eng. Des. 75-79 (2005) 1211-1216.
[2] W. Raskob and P.J. Barry, J. Environ. Radioact. 36 (1997) 237-251.
[3] C. Boyer, L. Vichot, M. Fromm, Y. Losset, F. Tatin-Froux, P. Guetat and P.M. Badot, Environ. Exp. Bot. 67 (2009) 34-51.
[4] J. Feinhals and C. Bunnenberg, Fusion Technol. 14 (1988) 1253-1257.
[5] M. Taschner, C. Bunnenberg and W. Raskob, J. Environ. Radioact. 36 (1997) 219-235.
[6] Y. Belot, Deviation of parameters for use in tritium washout predictions, Workshop of IEA Task Group on Tritium Safety and Environmental Effects, AECL, Canada, May 11-12. (1998)
[7] A. Golubev, M. Khabibulin and S. Mavrin, Radioprotection - Colloques. 37 C1 (2002) 465-470.
[8] H. Yamazawa, Environ. Model. Softw. 16 (2001) 739-751.
[9] H. Nagai, J. Appl. Meteorol. 44 (2005) 1574-1592.
[10] M. Ota and H. Nagai, J. Environ. Radioact. (2011) (in press).