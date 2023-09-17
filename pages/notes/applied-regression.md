---
layout: notes
title: Applied Linear Regression
subtitle: Selected Notes from STAT 504 + CSE 546, University of Washington
---

### Table of Contents
{:.no_toc}
* TOC 
{:toc}
{::options toc_levels="3" /}

## Introduction

This note is mainly built on STAT 504 about linear regression from a **nonparametric approach/population first approach**, which means we will define interested parameter as operations rather than assuming that these distributions can be fully characterized by a distribution function with a ﬁnite number of parameters. Hence, we are going to *empirical distribution* to describe the sample and *population joint distribution* for the associational concepts in the population level. I also include some materials from machine learning practical side (CSE 546), such as Bias-Variance Tradeoff and Cross-Validation.

| Tranditional Approach Examples | Nonparametric Approach                                      |
| :----------------------------- | :---------------------------------------------------------- |
| Sample average                 | Statistical functional of the empirical distribution        |
| Population mean                | Statistical functional of the population joint distribution |

For prerequite knowledge on probability and linear algebra, please refer to sepreate pages. For some topics highly related to linear regerssion, please refer to: casual inference using linear regression.



### Conditional Expectation Function












### Linear Regression

#### Best MSE predictors

- $$E[Y\vert X]$$ is the best MSE predictor of $$Y$$ by using $$X$$. 
- $$E[Y\vert X]=\mbox{argmin}_{f}E[(y-f(x))^2]$$, all possible functions of $$X$$ we can choose which can get the minimal loss from our loss function (MSE). 

- $$E[(y-f(x))^2\vert X=x]=Var(y\vert X=x)+(E[y\vert X=x]-f(x))^2$$ and the solution is $$f(x)=E[Y\vert X=x]$$. 
  

##### CEF decomposition property (for all CEFs)

- For any R.V. $$Y,X$$, we have $$Y=\mu(X)+\epsilon$$, where $$\mu(X)=E[Y\vert X]$$ and $$\epsilon$$ is unknown (with <u>some properties</u>, not assumptions)

  - $$E(\epsilon\vert X)=0$$, $$E(\epsilon)=E[E(\epsilon\vert X)]=0$$
  - $$Var(\epsilon\vert X)=Var(Y\vert X)=E(\epsilon^2\vert X)-E(\epsilon\vert X)^2$$, $$Var(\epsilon)=E[Var(Y\vert X)]$$
  - $$E[h(X)\epsilon]=0$$ for any function $$h(x)$$, which means $$\epsilon$$ is not correlated with any function of $$X$$

- So $$Y$$ can be decomposed to two parts:  $$E[Y\vert X]$$, a part can be explained by $$X$$, and a <u>residual</u> that is uncorrelated with any function of $$X$$. 


##### ANOVA theorem (law of total variance)

- $$Var(Y)=Var[E(Y\vert X)+\epsilon]=Var[E(Y\vert X)]+E[Var(Y\vert X)]$$ 

  - Note: $$Cov[E(Y\vert X),\epsilon]=0$$



#### Best linear predictors

- In general, the CEF maybe too ambitious, or for other reasons, we may need to provide a simple summary of the relationship of $$Y\vert X$$

- Linear regression (OLS) is the best linear approximation to conditional expectation function (CEF) in terms of MSE

- We may want to restrict the class of $$f$$ belongs to the form: $$f(x)=\alpha+\beta x$$ 

  - OLS linear regression is the best linear predictor of $$Y$$

  - $$BLP(Y\vert X) = \alpha+\beta x$$, where:
    
    - $$\alpha=E(Y)-\beta E(X)$$
    
    - $$\beta=\frac{Cov(Y,X)}{Var(X)}$$
      


##### Linear decomposition principle

- $$Y=a+bX+e$$

  - where $$E[e]=0$$, $$E[Xe] = 0$$ and $$Cov(x,e)=0$$ 

- Linear ANOVA

  - $$Var(Y)=Var(a+bX)+Var(e)=b^2Var(X)+Var(e)$$ 

- Linear $$R^2$$ / coefficient of determination

  - $$R^2_{y\sim x}=\frac{Var(a+bX)}{Var(Y)}=1-\frac{Var(\epsilon)}{Var(Y)}=Cor(X,Y)^2$$   
    


##### CEF and LR

- Linear regression is the best linear approximation of the CEF ($$E[Y\vert X]$$)

  - $$BLP(Y\vert X)=argmin E[(E(Y\vert X)-f(X))^2]$$ 
    - $$\alpha^*=E(E(Y\vert X))-\beta E(X)$$
    - $$\beta^*=\frac{Cov(E[Y\vert X]+\epsilon,X)}{Var(X)}$$ 
  - we can estimate BLP based on aggregated data

- If the CEF is linear, then LR is the CEF

  - $$E[Y\vert X]=a+bX, a= E[Y]-bE[X]$$

  - $$Cov(Y,X)=Cov[a+bX+\epsilon]=bVar[X]$$
    


#### Further decomposition of CEF and LR

- ![[Pasted image 20230206181101.png\vert 350]]

- $$e:=Y-\alpha-\beta Y=U+\epsilon$$

- $$\epsilon := Y-E[Y\vert X]$$

  - irreducible error or noise in a sense that we cannot prevent this error

- $$U=E[Y\vert X]-\alpha-\beta Y$$

  - non-linearity error or approximation error and in theory we can minimize
    


#### Special cases of regression

##### Binary X and Y

- True CEF is linear: $$E[Y\vert X]=\alpha+\beta X$$

  - $$\alpha:=E[Y\vert X=0]$$ and $$\beta:=E[Y\vert X=1]-E[Y\vert X=0]$$
  - $$\beta$$ here means the change of $$E[Y\vert X]$$ due to the existence of $$X$$.

- $$Var(Y\vert X)$$ is not constant

  - $$Var[Y\vert X]=P(Y=1\vert X)[1-P(Y=1\vert X)]$$ 

- We can generalize it to multiple categorical variablaes which is [[#Saturated regression]].

- However, to make **predictions** (in finite sample estimate), that’s a different story.


##### Bivariate Gaussian

- The bivariate normal distribution is fullly described by $$\mu$$ and $$\Sigma$$. Also, the maginal and conditional distribution are normal.

  $$
  \left(
  \begin{matrix} 
  X \\ Y
  \end{matrix}
  \right)
  \sim N(\mu,\Sigma), \mbox{where }\mu =
  \left(
  \begin{matrix} 
  \mu_x\\\mu_y
  \end{matrix}
  \right)
  \mbox{ and }
  \Sigma=
  \left(
  \begin{matrix} 
  \sigma_x^2 & \sigma_{xy} \\
  \sigma_{xy} & \sigma_y^2
  \end{matrix}
  \right)
  $$

- $$Y\vert X \sim N(\alpha+\beta X,\sigma^2)$$ 

  - $$\alpha=\mu_y-\beta\mu_x$$, $$\beta=\frac{\sigma_{xy}}{\sigma_x^2}$$, $$\sigma=\sigma_y^2-\beta^2\sigma^2_x$$
  - These results tells us that we have **linear** CEF, constant conditional variance and normally distributed error terms. (no need to proof this)

- $$E[Y\vert X]=\alpha+\beta X$$ 

  - $$\beta = E[Y\vert X=x_0+1]-E[Y\vert X=x_0]=\frac{\partial E[Y\vert X=x]}{\partial x}\vert _{X=x}:=Q$$

  - $$Q$$ is the change in one unit of $$X$$ leads to the change in conditional expectation of $$Y$$.

  - The value of $$Q$$ does not depend on $$X_n$$.
    
    - But $$Q$$ is not always equal to $$\beta$$, only equal when CEF is linear
      


#### Multivariate Regression

##### Theory

- $$LR(Y_i\vert X_i)=X_i^T\beta$$

  - $$\beta=E[X_iX_i^T]^{-1}E[X_iY_i]$$
    - why we get this result? $$\frac{\partial L}{\partial \beta}=0$$
  - where $$X=[1,X_{1i},X_{2i}...,X_{pi}]^T$$, $$\beta=[\beta_o,\beta_1,\beta_2,...,\beta_p]^T$$  

- CEF is the best predictor of Y using X

  - $$E[Y_i\vert X_i]=argmin_{f}E[(Y_i-f(X_i))^2]$$ 

- CEF decomposition

  - $$Y_i=E[Y_i\vert X_i]+\epsilon_i$$
    - $$E(\epsilon_i\vert X_i)=0$$, $$E(\epsilon_i)=E[E(\epsilon_i\vert X_i)]=0$$  
    - $$Var(\epsilon_i\vert X_i)=Var(Y_i\vert X_i)$$, $$Var(\epsilon_i)=E[Var(Y_i\vert X_i)]$$
    - $$E[h(X_i)\epsilon_i]=0$$ for all $$h$$

- Multivariate BLP

  - $$\beta_{OLS}=argmin_\beta E[(Y_i-X)i^T\beta)^2]=E[X_iX_i^T]^{-1}E[X_iY_i]$$
  - Decomposition
    - $$Y=X_i^T\beta+e_i$$
    - where $$E[X_ie_i]=0$$ (vector)
      - $$e_i$$ is uncorrelated with $$X$$ or any linear function of $$X$$

- If the CEF is linear then it equal to BLP = LR

  - $$E[Y\vert X]=X^T\beta$$ then $$\beta=E[XX^T]^{-1}E[xy]$$

- BLP is also the best linear approximation of the CEF

  - $$\beta^*=argminE[(E[Y\vert X]-X^T\beta)^2]=E[XX^T]^{-1}E[xy]=\beta_{OLS}$$ 
    
    - the trick used in this proof: $$E[XE(Y\vert X)]=E[E(XY\vert X)]=E[XY]$$
      


##### Special case: Saturated regression

- Suppose we have: $$Y$$ (income, continuous), $$X_1$$ (PhD/MS graduation, 1/0), $$X_2$$ (other covariates, 1/0), dummy variables

  - how many potential values CEF have? 4. So we can perfectly fit the function using 4 parameters

- $$E[Y\vert X_1,X_2]=\beta_0+\beta_1X_1+\beta_2X_2+\beta_{12}X_1X_2=X^T\beta$$

  - using matrix, we can write down $$\overrightarrow{X}$$ and $$\overrightarrow{\beta}$$

- We can get the solutions for $$\beta$$ 

- **NOT** assumption at all here but a property of dummy variables


##### Special case: Polynomial Regression

- $$E[Y\vert X_1,X_2]=\beta_0+\beta_1X_1+\beta_2X_2+\beta_{3}X_1^2+\beta_{4}X_2^2+\beta_{5}X_1X_2$$ 

  - Using matrix, we can write down $$\overrightarrow{X}$$ and $$\overrightarrow{\beta}$$

- $$E[Y\vert X]=X^T\beta=BLP(Y\vert X)$$ 

  - we can fit the polynomials using OLS by simply transforming the variables.
  - in theory, we can appxroximate any CEF in a <span style="background:#fff88f">bounded domain to arbritory precision</span>. ?
  - with finite data (samples), we need to pay attention to <u>overfitting</u> issue. 

- Marginal effects (how much $$y$$ will change if we change $$x$$) -》将带次方的换成平均变化

  - $$E[\frac{\partial E[Y\vert X_{1i},X_{2i}]}{\partial X_{1i}}]=E[\beta_1+2\beta_3X_{1i}+\beta_{5}X_{2i}]$$ 

- $$x^*=argmax_xE[Y_i\vert X_i=x]=-\frac{\beta_{1}}{2\beta_{2}}$$  

  - find the max value of $$Y$$ 
    


#### FWL Theorem (Regression anatomy)

- Let $$BLP(Y_i\vert X_i)=\beta_0+\beta_1X_{1i}+\beta_2X_{2i}+,...,+\beta_pX_{pi}$$:

  - $$\beta_k=\frac{Cov(Y_i,\tilde X_{ki})}{Var(\tilde X_{ki})}=\frac{Cov(\tilde Y_i,\tilde X_{ki})}{Var(\tilde X_{ki})}$$ 
  - where $$\tilde X_{ki}=X_{ki}-BLP(X_{ki}\vert X_{(-k)i})=X_{ki}^{\bot X_{(-k)i}}$$ and $$\tilde Y_{i}=Y_{i}-BLP(Y_{i}\vert X_{(-k)i})$$
  - $$X_{(-k)i}$$ is all other variables other than $$X_k$$
  - Explaination
    - $$\tilde X_{ki}$$ is the **residual** of the regression of $$X_k$$ on all other $$X$$, 使用除$$X_k$$之外的所有$$X_{-k}$$去解释$$X_k$$
    - $$\tilde Y_{i}$$ is the **residual** of the regression of $$Y$$ on all other $$X$$, 使用除$$X_k$$之外的所有$$X_{-k}$$去解释$$Y$$
    - We usually call this operation **partialling out**

- <span style="background:#fff88f">Notation</span>: $$X^{\bot Z}=X-BLP(X\vert Z)$$

$$$$\beta_k=\frac{Cov(Y_i^{\bot X_{(-k)i}},X_{ki}^{\bot X_{(-k)i}})}{Var(X_{ki}^{\bot X_{(-k)i}})}$$$$

- Properties
  
  - linear operator: $$V=X+W\Rightarrow V^{\bot Z}=X^{\bot Z}+W^{\bot Z}$$
  
  - $$Z^{\bot Z}=0$$
  
  - $$e^{\bot Z}=0$$, $$e$$ is the original residual from regression
    
  

#### Omitted Variable Bias

- Let $$Y_i=\tau D_i +X_i^T\beta+\gamma Z_i+e_i$$, and we omit the variable $$Z$$, then: $$Y_i=\tau_rD_i+X_i^T\beta_r+e_{ri}$$
  $$$$\tau_r=\tau+\gamma \delta \mbox{,  where }\delta=\frac{Cov(D_i^{\bot X_i},Z_i^{\bot X_i})}{Var(D_i^{\bot X_i})}$$$$

- Explanation: 

  - $$\gamma$$: the real predective impact of omitted variable $$Z$$ on $$Y$$

  - $$\delta$$: imbalance of $$Z$$ among levels of $$D$$ (not sure what this mean)
    


#### Partial $$R^2$$

- how much prediction power a random variable $$Z$$ has in explaining variation of $$Y$$ after taking into account what is already explained by other covariates $$D$$ and $$X$$.
  $$$$R^2_{Y\sim Z\vert D,X}:=\frac{R^2_{Y\sim Z+D+X}-R^2_{Y\sim D+X}}{1-R^2_{Y\sim D+X}}$$$$

- Note: $$R^2_{Y\sim X}=\frac{Var(a+bX)}{Var(Y)}$$

- Properties of the Partial $$R^2$$

  - $$0\leq R^2_{Y\sim Z\vert D,X}\leq 1$$

  - $$R^2_{Y\sim Z\vert D,X}=1-\frac{Var(Y^{\bot Z,D,X})}{Var(Y^{\bot D,X})}=Cor^2(Y^{\bot Z,D,X},Z^{\bot D,X})=R^2_{Z\sim Y\vert D,X}$$
    


##### Omitted variable bias ($$Z$$) with partial $$R^2$$ parametrization

- $$Bias=\tau_r-\tau=\delta\gamma$$, which is the coefficient difference of $$D$$, then:
  $$$$Bias^2=(\gamma\delta)^2=\frac{R^2_{Y\sim Z\vert D,X}\times R^2_{D\sim Z\vert X}}{1-R^2_{D\sim Z\vert X}}\times\frac{Var(Y^{\bot D,X})}{Var(D^{\bot X})}$$$$

- Explaination:

  - The first part is the component of the bias that depends on $$Z$$; tells us how $$Z$$ changes our regression coefficient of $$D$$. <span style="background:#fff88f">(The part of bias depends on Z.)</span>
  - The second is the residual variation of $$Y$$ after accounting for $$D$$ and$$X$$, *divided* by residual variation of $$D$$ after accounting for $$X$$. <span style="background:#fff88f">(This part is not related to Z.)</span>

- Application

  - Use this to bound the maximum change you would see in a regression coefficient due to the inclusion/omission of Z.
  - Because we only need to observe two values about $$Z$$: $$R^2_{Y\sim Z\vert D,X}$$ and $$R^2_{D\sim Z\vert X}$$.

- How about mutliple unobserved variables? $$Z=[Z_1,Z_2,...,Z_p]^T$$

$$$$Bias^2\leq \frac{R^2_{Y\sim Z\vert D,X}\times R^2_{D\sim Z\vert X}}{1-R^2_{D\sim Z\vert X}}\times\frac{Var(Y^{\bot D,X})}{Var(D^{\bot X})}$$$$

### Independence, Mean independence, Uncorrelatedness

- Independence  $$X\bot Y\Leftrightarrow Y\bot X$$ 
  
  - $$P(Y,X)=P(X)P(Y)$$  or $$P(Y\vert X)=0, \forall X,Y$$  
  - Learning about X does not change $$P(Y)$$ and vice verse, but independent does not mean no causal relationships

- Mean Independence
  
  - Y is mean independent of X if $$E[Y\vert X]=E[Y]$$ 
  - This is NOT symmetric!

- Uncorrelatedness
  
  - $$Cov(X,Y)=0$$
  - This is symmetric and $$BLP(Y\vert X)$$ and $$BLP(X\vert Y)$$ are constant

- Independence $$\Rightarrow$$ Mean Independence $$\Rightarrow$$ Uncorrelatedness

- $$e=Y-BLP(Y\vert X)$$ $$\Rightarrow$$ e is **uncorrelated** with linear function of X

- $$\epsilon=Y-E[Y\vert X]$$ $$\Rightarrow$$  is mean independence of X

- Implications
  
  - $$Y\bot X\Rightarrow E[Y\vert X]=E[Y]\Rightarrow Cov(Y,X)=0\Rightarrow BLP(Y\vert X)=\alpha$$
  
  - If we say $$e:=Y=X\beta, E[e\vert X]=0$$: it's an assumption (implying that the CEF is linear)
  
  - If we say $$Y=f(X)+\epsilon, \epsilon \bot X$$: it's an <span style="background:#fff88f">assumption</span>?
    
  

### Finite Samples

- In reality, we just have a sample from the distribution not the whole population.

- To connect the samples with the population/distribition, we need assumptions.

  - All samples are independent and identifcally distributed samples from $$P(y,x)$$. (IID)

  - The notion of IID: independent, identical distributed
    


#### Estimation

- Suppose we have $$(Y_i,X_i)\sim^{iid} P(Y_i,X_i), 1\leq i\leq N$$  AND suppose we do not want to more assumption about $$P(Y,X)$$ 

- How would you like to estimate the $$BLP(Y\vert X)$$? 

  - $$\hat{BLP}(Y\vert X)=\hat\alpha+\hat\beta X$$    
  - $$\hat Y=E_n[Y]$$ emprical version, same opreation but the ture empiral distribution
  - $$\hat Var(X) =E_n[(X_i-E_N(X_i))^2]$$ sample / emprical version 
  - $$E_n[g(x_i)]=\frac1n\sum_ig(x_i)$$ emprical version ($$P_n$$ is the same thing for some books)

- For multiple regression

  - $$\beta=E[XX^T]^{-1}E[XY]$$ 
    
    - $$\hat\beta=E_n[X_iX_i^T]^{-1}E_n[X_{i}Y]=(\frac1n\sum_iX_iX_i^T)^{-1}(\frac1n\sum_ix_iy_i)$$ ($$(X^TX)^{-1}(X^Ty)$$ formula we always see in other books or previous classes)   
      
      - $$X_i=[1,x_{i1},...,x_{in}]^T$$ 
    
    - we can rewrite $$\hat e_i =y_i-x_i^T\hat\beta$$ 
      
      - and all other proofs stay and just change the symbol
        


#### Plug-in Principle

- Target parameters: $$Q=f(P)$$ a function of the distribution of our variable

  - e.g. $$Q=E[\partial E[Y_i\vert X_i]/\partial x_i]$$ 

- Estimate: $$\hat Q=f(P_m)$$, $$P_m$$ is the empirical distribution

  - sample analog of the population solution 
  - $$\hat\beta =E_n[X_iX_i^T]^{-1}E[X_iY_i]=[\frac1n\sum X_iX_i^T]^{-1}[\frac1n\sum X_iY_i]=(X^TX)^{-1}(X^TY)$$  
    - the last one is the traditional textbook formula 

- Another way to see the OLS estimates

  - Population version: $$\beta_{OLS}=argmin E[(y_i-X_i^T\beta)^2]$$ 
  - Sample version: $$\hat\beta_{OLS}=argmin E[(y_i-X_i^T\beta)^2]$$ 

- In general, all properties we derived for the population OLS/BLP will also valid in the sample case. So we get immediately from everything we have done so far. 

- Don't conflict the sample quantities with the population quantities.

  - $$\hat e_i\neq e_i$$, $$\hat \beta_{OLS}\neq \beta_{OLS}$$
  - $$\hat \beta_{OLS}$$ is an estimator and a random variable; $$\beta_{OLS}$$ is fixed and a property of population
  - we call the distribution of $$\hat \beta_{OLS}$$ as <span style="background:#fff88f">sampling distribution</span> 

- We may ask some questions about the estimator: 

  - does it coverage to the true with the sample size grows? (consistence)
    
    - $$\hat\beta_n\rightarrow \beta, n\rightarrow \infty$$ 
    - In general, plug-in estimators are consistant. 
    - $$\hat \theta_n$$ is consistent for $$\theta$$ if: $$\lim_{n\rightarrow\infty} P(\vert \theta_n-\theta\vert \leq\epsilon)=0, \forall \epsilon\leq 0$$

  - $$Q_n$$ average, does it get the correct answer? (unbiasness) 
    
    - $$E[\hat\beta_n]=\beta$$

  - how variable is our estimator? (sampling variability) 
    
    - $$Var(\hat\beta_n)$$, we want this to decrease as a function of $$n$$
      
      ##### Bias
      
      Let's think about an estimator $$\hat\theta_n$$ for some parameter $$\theta$$

- Bias $$\hat\theta_n$$ with $$\theta$$: $$Bias[\hat\theta_n,\theta]=E[\hat\theta_n]-\theta$$

  - If bias = 0, and we call it is unbiased.
  - $$\hat\beta_{OLS}$$ is unbiased, <u>NOT</u> in general, for $$\hat\beta_{OLS}=E[X_iX_i^T]^{-1}E[X_iY_i]$$
    - Proof: $$\hat\beta_{OLS}=\beta+[\frac1n\sum X_iX_i^T]^{-1}[\frac1n\sum X_ie_i]$$ 
    - $$E[\hat\beta_{OLS}\vert X]=\beta+[\frac1n\sum X_iX_i^T]^{-1}[\frac1n\sum X_iE[e_i\vert x_i]]$$ 
      - $$E[e_i\vert x_i]]$$ is not 0 in general, so our $$\hat\beta_{OLS}$$ is <u>biased in general</u>. 
      - But if $$E[y_i\vert x_i]]=X_i^T\beta$$ (ths CEF is linear), then $$E[e_i\vert x_i]]=0$$, and <span style="background:#ff4d4f">TWO (un)conditional unbiasness</span>
      - Unbiasness used to receive a lot of attention, but it's not so important nowadays. Most estimators will be biased.

- Sampling variance of $$\hat \theta_n$$

  - $$Var(\hat \theta_n)$$: variance of the sampling distribution

- Standard error

  - $$SE[\hat \theta_n]:=SD[\hat \theta_n]$$ (standard devidiation of the sampling distribution)
    - Standard error is for the **population**, also called unbiased standard error
  - important because we need to evluate the quality of estimator

- MSE decomposition

  - $$MSE(\hat \theta_n,\theta)=E[(\hat \theta_n-\theta)^2]=Var(\hat \theta_n)+(E[\hat \theta_n]-\theta)^2$$ 

- An estimator is anampyidly normal if 

  - $$\frac{\hat \theta_n-\theta}{SE}\rightarrow^d N(0,1)$$ 
  - if an estimator is ama normal, we can use this fact to make approximate inference 
  - $$P(\frac{\vert \hat \theta_n-\theta\vert }{se}\leq Z_\alpha)=0.95$$ 
    - just use the <font color="#ff0000">tail</font> of the standard normal distribution
  - $$P(\hat \theta_n-se*Z_{\alpha/2}\leq \theta\leq \theta_n+ se * Z_{\alpha/2})=0.95$$ 

- confidence interval

  - A confidence interval for a parameter is an intervla in proof:
    - $$P(\theta\in C_n)\leq1-\alpha, \forall \theta$$ 
      - \theta is fixed and C_n is random
    - $$(1-\alpha)\%$$ of the sampling XXX, $$\theta$$ will be with in $$C_n$$

#### Nonparametric bootstrap

- $$V_i\sim^{iid} P$$ 
- We can define the empircal distribution P_n as a distribution that assigns probability for all point V_i
- $$F_n\Rightarrow$$ emprical CDF, $$F\Rightarrow$$ ture CDF 
  - it can be shown that with the larger sample size, $$F_n\rightarrow F$$ 
- bootstrap
  - the idea of bootstrap is that: if the $$F_n$$ is closed to $$P$$, then I can approximate the sampling distribution of my estimator $$\theta_n$$ empircal distribution as the ture distribution, and resample from it
  - algoriltm
    - n is the sample size
    - B is the number of Boostrap sample
    - for i in B:
      - sample n observations (each one is row) with replacement from ture data
      - compute our statistics in the sample data ($$\theta_j^n$$)
    - That gvie us the bootstrap sample $$\hat\theta^*=[\tilde\theta_1,...,\tilde\theta_B]$$ 
      - This is an approximation of true sampling distribution of $$\hat\theta$$
  - two simple ways
    - one: the normal approximation interval 
      - $$\hat se_{boot}=SD(\hat\theta^*)$$
      - $$\hat\theta_n\pm \hat se_{boot}\times Z_{\alpha/2}$$
    - two: $$C_n=[\hat\theta_{\alpha/2},\hat\theta_{1-\alpha/2}]$$ 
      R doc

Feb 13

- Plan
  
  - traditional classical linear regression model
    - exact distribution for the estimators: t distribution with n-p degree of freedom
  - robost standard errors
    - asymptotic analysis: asymptotic normal; we will the variance-covariance matrix $$\hat\beta_n$$
      - The law of large number
      - CLT
      - shetccy theoem

- Classical linear regression model

- $$Y_i\vert X_i \sim ^{iid} N(\mu_0,\sigma^2)$$
  
  - $$\mu_o=X_i^T\beta$$

- Assumptions:
  
  - $$\mu_o=E[Y_o\vert X_i]=X_i^T\beta$$, linearity of the CEF
    - this give us unbiasness
  - $$Var(Y_i\vert X_i)=\sigma^2=E[e_i^2]$$ 
    - give us a simple analytical formula for the variance of $$\hat\beta_n$$
    - $$Var(\hat\beta_n\vert X)=\frac{\sigma^2}{n}[\frac1n\sum_iX_iX_i^T]^{-1}=\sigma^2(X^TX)^{-1}$$ 
      - disganal of this matrix give us the true variances for the elements of $$\hat\beta_n$$, the square root is the standard errors 
  - $$e_i\sim_{iid} N(0,\sigma^2)$$ normally distributed
    - $$\hat\beta\vert X\sim N(\beta,\frac{\sigma^2}{n}[\frac1n\sum_iX_iX_i^T]^{-1})$$ 
    - $$\frac{\hat\beta_k-\beta_k}{SE(\hat\beta_k)}\sim N(0,1)$$  
      - we need to estimate $$\sigma^2$$, $$\hat\sigma^2=\frac{\hat e^T \hat e}{n-1}$$ 
        - n-1, degree of freedom (DF)

- Our esitmated variance-covariance matrix $$\hat\beta_n$$
  
  - $$\hat\sigma^2(X^TX)^{-1}$$ 
  - $$\frac{\hat\beta_k-\beta_k}{\hat{SE}(\hat\beta_k)}\sim t(n-p)$$  student t distribution with (n-p) degree of freedom 

- <font color="#ff0000">consistant intervals using t distribution </font>

- for a fixed P, $$n\rightarrow\infty$$ this convenge to standard normal distribution

- There're many strong linearity assunptions
  
  - linear of CEF
  - consistant variance
  - Gaussian error

Feb 15

- robost standard errors

- $$\hat\beta_{OLS}=\beta+[\frac1n\sum X_iX_i^T]^{-1}[\frac1n\sum X_ie_i]$$ 

- As we have seen, plug-in estimators all (in general) consistent and ansmphoroly

- We saw how to use the nonparameteric to compute standard errors and estimate confidence intervals without >>> tthe variance of $$\hat\beta_n$$ explicitly. 

- But now we derive a closed form expainsion for the congmptoties >>> of $$\hat\beta_n$$. 

- law of large numbers
  
  - empricial moments converge to population moments
    - $$E_n[X_i]\rightarrow^P E[X_i]$$ 

- central limit theorm 

![[Pasted image 20230215144827.png]]
![[Pasted image 20230215222256.png]]
![[Pasted image 20230215222334.png]]

### Causal inference

- I want to estimate the causal effect of $$D$$ on $$Y$$
- How do I explain this question mathmatically? 
  - $$E[Y\vert D=1]-E[Y\vert D=0]$$  (all obeserved of $$Y$$) Can this be seen as causal effect? No. 
  - We need to define a new object for causal quantilities
    - for causal inference, we need the concept of a causal model
      - <span style="background:#fff88f">conceptuals outcome</span> >>>>
- Potential outcomes
  - $$Y(1)$$: mortality (outcome) if we <u>force</u> the person to take the drug (treatment)
  - $$Y(0)$$: mortality (outcome) if we <u>force</u> the person to now take the drug (treatment)
  - $$\tau_i=Y_o(1)-Y_i(o)$$ 
  - $$E[\tau_i]=E[Y_o(1)]-E[Y_i(o)]=E[Y_i(1)]-E[Y_i(o)]$$  
    - $$E[Y_i(1)]$$ the average of Y if we intervine
- Suppose we have data on $$P(Y_i,X_0,D_i)$$ 
  - we have no data on $$Y_0(1)$$ and $$Y_0(0)$$ 
    - to connect the observed data to the conceptual (potential outcome) we need assumptions (causal assumptions)
- Consistence
  - $$D_i=d \Rightarrow Y_i=Y_i(d)$$ 
  - for binary treatment $$Y_i=D_iY_i(1)+(1-D_0)Y_i(0)$$ 
- Conditional ignordilion (of the trearment assignment)
  - suppose D_i is randomized
    - $$D_o \bot Y_i(1),Y_i(0),X_i$$ 
    - with this, we can already prove that randomlizetion >>> ATE
    - $$ATE=E[Y(1)]-E[Y(0)]=E[Y(1)\vert D=1]-E[Y(0)\vert D=0]=E[Y\vert D=1]-E[Y\vert D=0]$$
  - with a binary treatment, this can be >>> with a regression coef
  - $$\frac{Cov(Y,D)}{Var(D)}=ATE$$ 
- Unconfoundence/Conditional ignordilion
  - $$Y(1),Y(0)\bot D\vert X$$  (assume no obsersed compound for now)
  - the treatment is not confounded with the outcome once we >>>
  - the treatment is an of random conditional on X
    - which X should include in my regression such that conditional ignordilion holds?
- This is suffcient to identitfy (explain our causal effect in terms of the observed data) the ATE
- $$ATE=E[Y(1)]-E[Y(0)]=E[E(Y_i\vert D_o=d,X_i)-E(Y_0\vert D_i=0,X_i)]$$ statistical estimation
- How to estimate ATE? Plug-in: $$\hat{ATE}=\frac1n\sum_i[\hat E(Y_i\vert D_o=d,X_i)-\hat E(Y_0\vert D_i=0,X_i)]$$
  - $$\hat E(Y_0\vert D_i=0,X_i)$$ fitted regression model
  - Just use the nonparameteric bootstrap
- When does regression coef reflect ture ATE?
  - suppose $$E(Y_0\vert D_i,X_i)=\tau D_i+X_o^T\beta$$ 
  - consistency + Unconfoundence
  - Then: $$ATE=\tau$$ 
  - But we do not need commit the lineaity
    - $$E[Y\vert D,X]=\beta_0+\beta_1DX+\beta_3X$$
    - $$ATE=\beta_1+\beta_2E[X]$$  not a single regression coef but we know how to estimate this <span style="background:#fff88f">MIDTERM</span>

![[Pasted image 20230217145734.png]]

Feb 23

- regression and causal inference
  
  - structual models and causal diagrams
  - good and bad controls (based on the empircal domain knowledge)

- Review
  
  - query / causal estimator: for example: ATE (one estimator)
  - causal assumptions: 
    - consistency 
    - conditianal ingoreabiliy / unconfoundment 
  - identification 
  - inference
    - point estimation: plug-in estimation
    - non-parameteric booststrap
    - other ways
  - what about the ATE is equal to the regression coef? 
    - if the CEF is linear on $$D_i, X_i$$ 
  - when should we expect conditional ignoreablity to hold on confound
    - or which variables should I include in the regression equation
    - to answer this question, we need structual models and causal diagrams

- Structual causal models (SCM)
  
  - $$X$$ socio-economics factors, $$D$$ drug, $$Y$$ mortality 
  - $$X\leftarrow f_x(U_x)$$ huge complicated function  
  - $$D\leftarrow f_D(X,U_D)$$; 
  - $$y\leftarrow f_y(D,X,U_y)$$, $$Y=(X,D,y)$$ endogamous variable
  - $$U=(U_x,U_D,U_y)$$ exogenous variables
  - $$F=\{f_x,f_D,f_y\}$$: structual equations, potential outcome variables

- $$U\sim P(U)$$, joint distribution of the exogenous variables
  
  - $$P(U)=P(U_x)*P(U_D)*P(U_y)$$
    
    - this is a strong assumption
  
  - Causal diagrams
    
    - all models we study here are **no circles**
    - direct aegclic graph
    - usually we will omit exogenous variable from ture diagrams
    - moreover, if a latent variables exists more than one Structual model, or if the  exogenous variable are not independent, then we will express this iwth dashed 
      - $$X\leftarrow f_x(U_x)$$ huge complicated function  
      - $$D\leftarrow f_D(X,U_X)$$; 
      - $$y\leftarrow f_y(D,X,U_y)$$, $$Y=(X,D,y)$$ endogamous variable
      - figrue 2 in the notes
        - we can partalliy spliting a structual model using a causal diagrams

- how can defind causal effects

- we can define causal effects as expicfic thern as the model
  
  - modify the machinism of $$M$$
  - For example, $$do (D=d)$$
    - replace the machinism $$D\leftarrow f_D(X,U_D)$$ with $$D\leftarrow d$$
    - figure 3

![[IMG_0040.png]]

![[IMG_0041.png]]

Feb 27

- common mistakes in midterm
  - boostrap: resampling with the full dataset: n is the row number of  your dataset

#### Good and bad controls

- the problem we want to solve: given the observation data $$D_v$$ and a causal diagram $$G$$, can we identify the ATE via regression adjustment? 
  - if X is a valid adjustment set, then the $$ATE  = E[E[Y\vert D=1,X]-E[Y\vert D=0,X]]$$ or $$Y(d)\bot D\vert X$$ (unconfounded)
  - example: suppose we have the DAG: ![[Pasted image 20230227145411.png\vert 200]]
  - suppose the SE are linear
    - $$D=\lambda_{XD}X+u_D$$
    - $$Y=\lambda_{Dy}D+\lambda_{xy}X+u_y$$
    - X, U_D, U_y are indenpdent 
  - What's the ATE
    - $$ATE=\lambda_{Dy}$$ 
    - relation with OLS
    - y ~ D![[Pasted image 20230227150301.png]]
    - adjusting for X will block the non-causal path
    - y ~ D+X
    - ![[Pasted image 20230227150727.png]]
  - Now, lets understand in general how these two things work?
    - which path is causal/non-causal
    - when the path closed or opened?
    - there are 3 building blocks/pattern
      - mediators (chain): D -> X -> Y, x mediate the effect of D on Y
        - a causal path. by default, it is opened
        - conditioning on X block this flow 
      - common causes (confounders) /form
        - ![[Pasted image 20230227151528.png\vert 200]]
        - non-causal between D and Y (asscoation). by default, its closed
        - conditioning on will block the flow
      - common effect (collides)
        - ![[Pasted image 20230227152125.png\vert 200]]
        - a common effect does not induce association between its causes
        - conditioning on the X, **open** this no-causal flow association

Mar 1

- Crash course about good and bad control

### Penalized Regression

- We used to assume that our sample size n >> p (number of feature), but the high-dimensional regressors are common nowadays due to rich features and non-linear models

- Whenever p/n is not small, tranditional inference can break down and we can overfit; if p >> n, we cannot even fit on OLS model.

- To this seeting, in-sample awareness of goodness of fit ($$R^2$$, MSE) may be too optimistics

- There are ways to account for this outfitting by comparing the goodness of fit matirx, such as the adjusted $$R^2$$. 

- In machine learning, a simple and effective way to deal with the overfitting issues: 
  
  - Two goal: getting a accurate methods of model estimation + avoid overfitting 

- Sample splitting (still need IID data): 
  
  - Trainning and validation (before model selection)
  - Test data (model performance)
  - How can we select the best model for prediction from a set of candidate models?
    - Cross-validation, the most popular approach now
    - K-fold cross-validation 
      - mimic predictions out of samples
      - <u>Example</u>: suppose $$E[Y\vert X]=g(x)$$ and we suppose it is non-linear
      - We could use polynomial to approximate: 
        1. Define a matrix of performance ($$R^2$$, MSE)
        2. Split all dafta into $$k$$ folders (usually 5 or 10)
        3. For each folder $$f_j$$:
           1. Fit the models using all data except fold $$f_j$$
           2. Use fold $$f_j$$ to predict and compute the performance matrix 
           3. Compute the average of the performance matrix
        4. Select the model with better average of the performance matrix

- Let $$Y_i=E[Y\vert X_i]+\epsilon_i=g(X_i)+\epsilon_i$$  
  
  - $$\hat{g}(X_i)$$ is a prediction function tarined on IID smaple $$P(X,Y)$$
  - Now consider an assume observation $$y,x\sim P(X,Y)$$, which are independent from existing data 
  - $$E[(y^{NEW}-\hat g(X^{NEW}))^2\vert X^{NEW}=x^{new}]$$ 
  - <u>Bias-variance tarde-off</u>
    - We maybe able to get better out of sample performance by introducing a <u>little</u> bias if the compensiton by XXX the variance.

- Therefore, we are going to add a penalized term:
  
  - h0 penality: $$\beta H_0$$ = # of non zero ceof. --- subset regression
  
  - h1 penality: $$\beta H_1$$ = $$\sum_j \vert \beta_j\vert $$   --- Lasso
  
  - h2 penality: $$\beta H_2$$ = $$\sum_j \beta_j^2$$     --- Ridge
    

#### Lasso regression

$$$$argmin_{\beta\in R^P}\frac1n \sum_i (Y_i-X_i^T\beta)^2+\lambda\sum^p_{j=1}\vert \beta_j\vert $$$$

The general matrix format solution: 

The lasso penality will shriinke some coeffcientts to zero

#### Ridge regression

$$$$argmin_{\beta\in R^P}\frac1n\sum_i(Y_i-X_i^T\beta)^2+\lambda\sum^p_{j=1}\beta^2_j$$$$

- $$\lambda$$ fixed penlity

- $$\sum^p_{j=1}\beta^2_j$$ the measurement of model complexity 

- The general matrix format solution: 

- for the penlity, it treats all coeffcients the same; so we need to standardize all covariates

- In general, which one is best, lasso or ridge? 
  
  - It depends on the sample data generation process

- We can use lasso and ridge to fit non-linear models. 

Go back to causal inference
