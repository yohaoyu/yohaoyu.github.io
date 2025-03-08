---
layout: notes
title: Probability and Mathematical Statistics
subtitle: Selected Notes from STAT 512 + STAT 513, University of Washington
---



## More general hypothesis testing
Suppose we are interested in testing one of the following sets of hypotheses:
$$
\begin{array}{rll}
H_{0}: \theta=\theta_{0} & \text { vs } & H_{1}: \theta \neq \theta_{0} \\
H_{0}: a \leq \theta \leq b & \text { vs } & H_{1}: \theta<a \text { or } b<\theta
\end{array}
$$
### General LRT for composite hypotheses
#### Well-seperated cases
(*Not an interesting case because it's almost impossible*) The test setting: $H_{0}: \theta \in \Omega_{0}$ and $H_{1}: \theta \in \Omega_{1} \equiv \Omega-\Omega_{0}$. If either If $\Omega_0$ and $\Omega_1$ are **pointwisely seperated** or **uniformly seperated**: 
- If $\Omega_0$ and $\Omega_1$ are **pointwisely seperated** w.r.t. K-L divergence:  
$$
\begin{aligned}
& \inf _{\theta \in \Omega_{1}} K L\left(f_{\theta_{0}}, f_{\theta_{1}}\right)>0, \forall \theta_{0} \in \Omega_{0} \\
& \inf _{\theta \in \Omega_{0}} K L\left(f_{\theta_{1}}, f_{\theta_{0}}\right)>0, \forall \theta_{1} \in \Omega_{1}
\end{aligned}
$$
 - If $\Omega_0$ and $\Omega_1$ are **uniformly seperated** w.r.t. K-L divergence:  
$$
\begin{aligned}
&\inf_{\theta_0 \in \Omega_0,\, \theta_1 \in \Omega_1} \mathrm{KL}\bigl(f_{\theta_0}, f_{\theta_1}\bigr) \;>\; 0 
\newline
&\inf_{\theta_0 \in \Omega_0,\, \theta_1 \in \Omega_1} \mathrm{KL}\bigl(f_{\theta_1}, f_{\theta_0}\bigr) \;>\; 0 
\end{aligned}
$$
In both case, the LRT (likelihood ratio test) is still recommended test:
$$
\phi\left(x_{1},\dots, x_{n}\right)= \begin{cases}0 & \text { if } \frac{\prod f_{\hat{\theta}_{1}}\left(x_{i}\right)}{\prod f_{\hat{\theta}_{0}}\left(x_{i}\right)} \leq C 
\\
\gamma &\text{ if } \frac{\prod f_{\hat{\theta}_{1}}\left(x_{i}\right)}{\prod f_{\hat{\theta}_{0}}\left(x_{i}\right)} = C 
\\ 1 & \text { if } \frac{\prod f_{\hat{\theta}_{1}}\left(x_{i}\right)}{\prod f_{\hat{\theta}_{0}}\left(x_{i}\right)}>C\end{cases}
$$
Where $\hat{\theta}_{i}$ is the MLE under the constraints that $H_{0}: \theta \in \Omega_{0}$ and $H_{1}: \theta \in \Omega_{1}$.
In other words, the LRT in the general case, is deponding on this if the HT problem is well seperareted.
$$
\begin{aligned}
\frac{\sup_{\theta\in\Omega_1}\prod f_{\theta}\left(x_{i}\right)}{\sup_{\theta\in\Omega_0}\prod f_{\theta}\left(x_{i}\right)}
\end{aligned}
$$

#### Not well-seperated cases
However, in most situation, well-spearatedness is unrealistic, such as $H_{0}: \theta \leq \theta_{0}  \text { vs }  H_{1}: \theta>\theta_{0}$. So, we have a more interesting and realistic setup:
- $H_{0}: \theta \in \Omega_{0}$ versus $H_{1}: \theta \in \Omega$ where $\Omega_{0} \subset \Omega \subset \mathbb{R}^{k}$
- $\operatorname{dim}(\Omega)=k-r$ ($r$ can be $0$) and $\operatorname{dim}\left(\Omega_{0}\right)=k-r-s$ where $s$ is additional constraint and $\dim{(\Omega_0)}$ can be understand as the number of free parameters
$$\begin{aligned}
\lambda(x)&=\frac{\sup_{\theta\in\Omega_0} f_{\theta_0}\left(x_{i}\right)}{\sup_{\theta\in\Omega} f_{\theta}\left(x_{i}\right)} \in [0,1]\\
& =\frac{f_{\hat\theta_0}\left(x_{i}\right)}{f_{\hat\theta}\left(x_{i}\right)}
\end{aligned}$$
So then the LRT is:
$$
\phi\left(x_{1},\dots, x_{n}\right)= \begin{cases}0 & \text { if } \frac{f_{\hat{\theta}_{0}}\left(x_{i}\right)}{f_{{\hat{\theta}}}\left(x_{i}\right)}>c \\ 1 & \text { if } \frac{f_{\hat{\theta}_{0}}\left(x_{i}\right)}{f_{\hat{\theta}}\left(x_{i}\right)}<c \\ \gamma & \text { if } \frac{f_{\hat{\theta}_{0}}\left(x_{i}\right)}{f_{\hat{\theta}}\left(x_{i}\right)}=c\end{cases}
$$

Where $\hat{\theta}_{0}$ is the MLE restricted to $\Omega_{0}$ and $\hat{\theta}$ is the unrestricted MLE.
And the p-value is:
$$
p=\sup _{\theta_{0} \in \Omega_{0}} P\left(\lambda \leq \lambda_{\mathrm{obs}}\right)
$$

#### T-test and one-sample normal model

Example 18.25 in MP (One-sample normal model - t-test)
Example 18.26 in MP (Two-sample normal model - t-test)

How to decide the threshold C in the general LRT framework? 
- In the special cases of 1 or 2-sample t-test, which follows a t-distribution
- Alternatively, resovt to asymptotic distribution results such as the CLT. Then, we need to know the distribution of $\lambda(x)$ under the H0 and as $n\rightarrow \infty$   

#### Wilks Theorem
Let $f_{\theta}$ be a sample from a regular family (satisfies Cramer and Wald conditions). Let the LRT statistic, $\lambda\left(x_{1}, \ldots, x_{n}\right)=\frac{f_{\hat{\theta}_{0}}\left(x_{i}\right)}{f_{\hat{\theta}}\left(x_{i}\right)}$, under $H_{0}$ has asymptotic chi-square distribution with $\mathrm{df}=\#$ of free parameters:
$$
-2 \log (\lambda) \xrightarrow{d} \chi_{s}^{2} \quad\left(\text { Where } s=\operatorname{dim}(\Omega)-\operatorname{dim}\left(\Omega_{0}\right)\right)
$$