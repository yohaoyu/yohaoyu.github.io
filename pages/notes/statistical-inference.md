---
layout: notes
title: Probability and Mathematical Statistics
subtitle: Selected Notes from STAT 504 + CSE 546, University of Washington
---



## Probability and Statistics

### Probability spaces

- Probability space: $$(\Omega, S, P)$$
  - Non-negativity: $$\forall A \in S, P(A) \leq 0$$, where $$P(A)$$ is ﬁnite and real.
  - Unitarity: $$P(\Omega) = 1$$
  - Countable additivity: if $$A_1,A_2,A_3,... \in S$$ are pairwise disjoint, and $$P(A_{1}\cup ...) = P(A_1)+ ... = \sum\limits P(A_i)$$
- measurement space: $$(\Omega, S)$$
- sample space: $$\Omega$$
- event space: $$S$$,  $$\sigma$$-algebra/field 

  - $$S\neq \emptyset$$  
  - if $$A\in S$$, then $$A^{C}\in S$$
  - if $$A_{1}, A_{2}...\in S$$, then $$A_{1}\cup A_{2}...\in S$$  

- probability measure: $$P:S\rightarrow R$$, assigns a probability (just like a funcion $$P$$) to every event in the event space. 

- Bayes' rules: $$P(B)=\frac{P(B|A)P(A)}{P(B)}$$ 

  - Another form (related to law of total probablity): 
  - $$P(A_i|B)=\frac{P(B|A_i)P(A_i)}{\sum ^k _{j=1} P(B|A_j)P(A_j)}$$

- Joint and Conditional Probabilities

  - For $$A,B \in S$$, the joint probability of A and B is $$P(A \cap B)$$. 
  - $$P(A\cup B)=P(A)+P(B)-P(A\cap B)$$
  - Conditional probablity of $$A$$ *given* $$B$$: $$P(A|B)=\frac{P(A\cap B)}{P(B)}$$

- Independent: $$P[A|B]=P[A]\ and \ P[A|B]=P[A|B^c]$$ if they are independent.

- **Partition**: If $$A_1 ,A_2 ,... \in S$$ are nonempty and pairwise disjoint, and  $$\Omega = A_{1 }\cup A_{2}\cup...$$, then $${ A_{1},A_{2},A_{3},...}$$ is a partition of $$\Omega$$.

### Random Variables

- A **random variable is a function** $$X:\Omega \rightarrow R$$ such that, $$\forall r\in R, \{a\in \Omega :X(a)\leq r\}\in S$$  

  - takes on a real value that is determined by a *random generative process*
  - Thus, it is often remarked that, technically, a random variable is neither random nor a variable, as it is merely a *function*.
  - uppercase letters to denote random variables and lowercase letters to denote generic outcome

- Function of a Random Variable

  - Deﬁnition: Let $$g : U → R$$ be a function, where $$X(\Omega) ⊆ U ⊆ R$$. Then, if $$g◦X:→R$$ is a random variable, we say that $$g$$ is a function of $$X$$, and write $$g(X)$$ to denote the random variable $$g◦X$$.
  - $$g◦X$$![[Pasted image 20230107213144.png]]
  - Eg: $$A=\{ω∈: X(ω) = 1\}=\{X=1\}$$, which means $$A$$ is the event that $$X$$ takes on the value of one

- Operator on a Random Variable

  - Deﬁnition: An **operator** $$A$$ on a random variable maps the function $$X(·)$$ to a real number, denoted by $$A [ X ]$$.



## Transformation











## Expectation

## Conditional Expectation






### Review of probability theory

- - 

#### Univariate distribution

##### Discrete/Continous Random Variables

- $$X\sim P(x)$$

- Probability Mass Function (PMF)/Probability Density Function (PDF)

- Cumulative Distribution Functions (CDF)

- For Continous Random Variables, event probability: $$\forall x \in R,P [ X = x ] = 0$$.

- Any **association** is represented by the distribution

  ##### Support

- The set of values at which the PMF or PDF of a random variable is positive is called its *support*.

- For a random variable X with PMF/PDF $$f$$, the support of $$X$$ is $$Supp [ X ] = { x \in R : f(x) > 0 }$$.

  - The notion of the support of a random variable will be particularly important in Section 2.2.3, when we deﬁne conditional expectations, and in Part III, in which assumptions about support will comprise key elements of our approach to identiﬁcation.

    ##### Expectation (first linear regression)

- Two different forms for discrect and continous R.V.

  - Expected Value and Expectation of a Function (below) are different
    - $$E(g(X))=\sum\limits_xg(x)f(x)\mbox{ or }\int^\infty_{-\infty}g(x)f(x)dx$$ 
  - $$E(X)$$ is the best predictors when we use MSE.

- If $$Y=g(X)$$, $$E(Y)=\sum\limits g(X)P(X)$$ 

- $$E[a+bX]=a+bE[X]$$ (Expected value of linear functions)

- Variance and standard deviatation: $$\sigma^2=Var[X]$$

  - higher varience means higher unpredictbility
  - $$Var(X)=E(X^2)-E(X)^2$$
  - Variance of a linear function: $$Var(a+bX)= b^2Var(X)$$ 

- $$SD(X)=\sqrt{Var(X)}$$ , $$SD(a+bX)=|b|\cdot SD(X)$$  

  ##### Best predictor

- We need to define what is the best when we talk about 

- **Loss function** is used to present

  - Squared loss: $$L(x,c)=(x-c)^2$$ 
  - Absoluate value loss: $$L(x,c)=|x-c|^2$$

- Mean square error

  - $$MSE(c) = E[(x-c)^2]$$, where $$c$$ is the predictors
  - decomposition of MSE: $$E[(x-c)^2]=Var(X)+(E(X)-c)^2$$
    - $$Var(X)$$: minimal error and we cannot aviod
    - We can know from here that the best predictor under MSE is $$c=E(X)$$.

- Mean decomposition 

  - $$X=\mu +\epsilon$$
    - $$\mu=E[X]$$ , $$\epsilon$$ is error/deviation from the mean
    - $$E(\epsilon)=0, Var(\epsilon)=Var(X)$$ 
  - We decomposite a $$X$$ to two parts, one we can get from the data ($$\mu$$) and one we cannot predict ($$\epsilon$$). These are properties of the error/NOT assumption.

#### Bivariate random variables

- Basic concepts of bivariate distribution

  - joint distribution

  - conditional distribution

    - conditional expectatioin function: **regression functions**
    - best linear predictors **(OLS)**

  - property of error terms

  - ANOVA (analysis of variance)

    ##### Joint distribution

- $$y$$ is the variable we are interested in predicting (response, outcomes, etc.)

- $$x$$ is the features, independent variables

- Key object:  **joint distribution**

  - CDF: $$P(Y\leq y, X\leq x) =F(x,y)$$ 

  - PDF/PMF are different

  - Joint distribution tells us **everything** about the association of $$X$$ and $$Y$$. 

    ##### Conditional distribution

- Usually, if interested in predicting, explain $$Y$$ as a function of $$X$$, and we will use the **conditional distribution** $$Y|X$$. 

  - This conditional distribution is just a univariate distribution and we can use the previous techniques. 
  - $$p(Y|X)=\frac{p(Y,X)}{p(X)}$$ , and little $$p$$ here represent both PMF and PDF.

- Conditional variance $$Var[y|x]=E[(y-E(y|x))^2|X=x]$$ 

- You can treat any function $$X$$ as constant when conditional on $$X$$. 

  - $$E[g(x)y+h(x)|X=x]=g(x)E(Y|X=x)+h(x)$$

    ##### Conditional expectation function

- For discrete random variables X and Y with joint PMF f, the conditional expectation of Y given X = x is: $$E [ Y | X = x ] = \sum\limits yf_{Y|X}(y | x),\forall x \in Supp [ X ]$$

- For jointly continuous random variables X and Y with joint PDF f, the conditional expectation of Y given X = x is: $$E [ Y | X = x ] = \int ^\infty_\infty yf_{Y|X}(y | x)dy,\forall x\in Supp [ X ]$$

- Conditional Expectation of a Function of Random Variables

  - similar to function of expectations

- Conditional Variance

  - $$V [ Y | X = x ] = E Y − E [ Y | X = x ] )^2X = x ,\forall x \in Supp [ X ]$$ 
  - Alternative Formula: $$E [ Y^{2}| X = x ] - E [ Y | X = x ]^2$$ 

- <u>Conditional Expectation Function</u> (CEF)

  - For random variables X and Y with joint PMF/PDF f, the conditional expectation function of Y given X = x is: $$G_Y(x) = E [ Y | X = x ], \forall x \in Supp [ X ]$$

  - We will generally write $$E [ Y | X = x ]$$ to denote the CEF rather than $$G_Y(x)$$

  - Law of Iterated Expectations: the most important one in applied regression

    - $$E [ Y ] = E [ E [ Y | X ] ]$$

  - Law of Total Variance

    - $$V [ Y ] = E [ V [ Y | X ] ] + V [ E [ Y | X ] ]$$

  - Properties of Deviations from the CEF: Let X and Y be random variables and let $$ε = Y − E [ Y | X ]$$. Then: (the proof process in P74 of [Peter M. Aronow, Benjamin T. Miller, 2019](zotero://select/items/@aronowFoundationsAgnosticStatistics2019))

    - $$E [ ε | X ] =E [ ε ] = 0$$

    - If $$g$$ is a function of $$X$$, then $$Cov [ g(X),ε ] = 0$$

    - $$V [ ε | X ] = V [ Y | X$$

    - $$V [ ε ] = E [ V [ Y | X ] ]$$

      ##### Corvariance and Correlation

- Covariance

  - $$Cov [ X,Y ] = E(X - E [ X ] )( Y - E [ Y ] )=E [ XY ] - E [ X ] E [ Y ]$$, $$\mbox{Cov}(X,Y)\in[-1,1]$$
  - Measure how $$X$$ and $$Y$$ covary or vary together. 
    - When $$\mbox{Cov}(X,Y)>0$$, $$X$$ and $$Y$$ are in the same direction; and when $$\mbox{Cov}(X,Y)<0$$, $$X$$ and $$Y$$ are in different directions. 
    - $$\mbox{Cov}(X,Y)=1/-1$$ if $$X$$ can be perfectly predict **linear** by $$Y$$ or vice verse. 
  - Variance Rule of Covariance: $$V [ X + Y ] = V [ X ] + 2Cov [ X,Y ] + V [ Y ]$$
  - Some Properties of Covariance
    - $$Cov [ X,X ] = V [ X ]$$
      - Variance is effectively a special case of covariance
    - $$\forall a,b,c,d \in R,Cov [ aX + c,bY + d ] = abCov [ X,Y ]$$
    - $$Cov [ X + W,Y + Z ] = Cov [ X,Y ] + Cov [ X,Z ] + Cov [ W,Y ] +Cov [ W,Z ]$$
    - $$\mbox{Cov}(X,Y)=\frac{\mbox{Cov}(Y,X)}{SD(X)SD(Y)}$$ 
    - $$\mbox{Cov}(X,Y)=\mbox{Cov}(Y,X)$$ if it's symmetric. 

- Correlation

  - $$\rho[X,Y]=\frac{Cov[X,Y]}{\sigma[X]\sigma[Y]}$$

  - Even if two random variables are not exactly linearly dependent, they can be more or less nearly so.

  - $$\rho [ X,Y ] = 1/-1\leftrightarrow \exists a,b \in R \mbox{ with } b > 0 \mbox{ such that }Y = a +/- bX$$

  - Properties of Correlation

    - $$\rho [ X,Y ] = \rho [ Y,X ]$$

    - $$ρ [ aX + c,bY + d ] = ρ [ X,Y ]$$ when a and b with same sign

    - $$ρ [ aX + c,bY + d ] = -ρ [ X,Y ]$$ when a and b with different sign

    - $$\rho(X,Y) = 0$$ does **not** generally imply $$X \bot Y$$

      ##### ANOVA

- $$Var(Y)=Var[E(Y|X)]+E[Var(Y|X)]$$

- Nonparameteric $$R^2$$ (Pearson correlation ratio)

  - Percentage of variation of $$Y$$ explained by $$X$$
  - $$\eta^{2}_{y \sim x}=\frac{Var[E(Y|X)]}{Var(Y)}=1-\frac{Var(\epsilon)}{Var(y)}\in[0,1]$$ 

<span style="background:#fff88f">updating all notes below</span>