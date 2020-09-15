# Chapter 2. Overview of Supervised Learning

## Definitions

- **inputs** (alt: predictors, features, independent variables)
- **outputs** (alt: responses, dependent variables)
* variable types
  - **quantitative**
  - **qualitative variables** (alt: categorical variables, discrete variables,
    factors)
    * values have no particular order
    - values are an element of a set of **classes**
    - often represented numerically by **codes**. these **codes** are
      also called **targets**
      - for multiclass, often use **dummy variables**
  - **ordered categorical** (e.g. small, medium, large). an ordering
    exists, but no metric is defined (nor appropriate).

## Conventions
- Denote input variable with $X$ (may be vector with attributes $X_j$)
- Quantitative outputs denoted $Y$, qualitative denoted $G$.
- Observed values are lowercase, $x_i$ is the $i$th observed value of
  vector $X$.
- Matrices are bold uppercase letters: $N$ input $p$-vectors is $N \times p$
  matrix $\mathbf{X}$.
- Vectors are not bolded unless referring to the $N$-vector of observed
  values $\mathbf{x}_j$ (the vector of $N$ observations of attribute $j$),
  aka the $j$th column of $\mathbf{X}$.
- $\hat{Y}$ and $\hat{G}$ represent predictions.
- The set $\{(x_i, y_i)\}, i \in (1:N)$ is the training data.


## Two approaches to prediction: _least squares_ and _nearest neighbors_

### Linear models and least squares

- Given: Vector of inputs $X^T = (X_1, X_2, ..., X_p)$
- Predict: Output $Y$ via model $\hat{Y} = \hat{\beta}_0 + \sum_{j=1}^{p} {X_j\hat{\beta}_j}$
- Introduce a $1$ to $X$ to get $\hat{Y} = X^T\hat{\beta}$
