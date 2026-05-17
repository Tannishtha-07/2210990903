# ---------------------------------------------------------
# Integrated Burnout Assessment and Coping (IBAC) Framework
# Research Implementation Prototype
# ---------------------------------------------------------

import math

# ---------------------------------------------------------
# SECTION 1: Composite Burnout Risk (CBR)
#
# Formula from research paper:
#
# CBR = α(EE) + β(DP) + γ(PA⁻¹) + δ(SM) + ε(FI)
#
# EE = Emotional Exhaustion
# DP = Depersonalization
# PA = Personal Accomplishment
# SM = Social Media Usage Index
# FI = Financial Insecurity Index
# ---------------------------------------------------------

def calculate_cbr(EE, DP, PA, SM, FI):
    
    # Regression weights (example values)
    alpha = 0.30
    beta = 0.25
    gamma = 0.20
    delta = 0.15
    epsilon = 0.10

    # Inverse PA effect
    PA_inverse = 100 - PA

    # Composite Burnout Risk
    CBR = (
        alpha * EE +
        beta * DP +
        gamma * PA_inverse +
        delta * SM +
        epsilon * FI
    )

    return round(CBR, 2)


# ---------------------------------------------------------
# SECTION 2: Intervention Recovery Probability (IRP)
#
# Formula:
#
# IRP = 1 − e^(−(w1×CBT + w2×MBSR + w3×EX + w4×SS))
#
# CBT  = Cognitive Behavioral Therapy engagement
# MBSR = Mindfulness-Based Stress Reduction
# EX   = Exercise
# SS   = Social Support
# ---------------------------------------------------------

def calculate_irp(CBT, MBSR, EX, SS):

    # Intervention weights
    w1 = 0.35
    w2 = 0.30
    w3 = 0.20
    w4 = 0.15

    score = (
        w1 * CBT +
        w2 * MBSR +
        w3 * EX +
        w4 * SS
    )

    IRP = 1 - math.exp(-score)

    return round(IRP, 4)


# ---------------------------------------------------------
# SECTION 3: Burnout Classification Scale
# ---------------------------------------------------------

def classify_burnout(cbr_score):

    if cbr_score < 25:
        return "Low Burnout Risk"

    elif cbr_score < 50:
        return "Moderate Burnout Risk"

    elif cbr_score < 75:
        return "High Burnout Risk"

    else:
        return "Severe Burnout Risk"


# ---------------------------------------------------------
# SECTION 4: Example Simulation
# ---------------------------------------------------------

# Example participant data
EE = 78   # Emotional Exhaustion
DP = 60   # Depersonalization
PA = 35   # Personal Accomplishment
SM = 7    # Social Media Hours/Day
FI = 65   # Financial Insecurity

# Intervention engagement scores
CBT = 0.8
MBSR = 0.7
EX = 0.6
SS = 0.9

# Compute CBR
cbr_score = calculate_cbr(EE, DP, PA, SM, FI)

# Compute IRP
irp_score = calculate_irp(CBT, MBSR, EX, SS)

# Classification
risk_level = classify_burnout(cbr_score)

# ---------------------------------------------------------
# OUTPUT
# ---------------------------------------------------------

print("------ IBAC FRAMEWORK RESULTS ------")
print(f"Composite Burnout Risk (CBR): {cbr_score}")
print(f"Burnout Classification: {risk_level}")
print(f"Intervention Recovery Probability (IRP): {irp_score}")
