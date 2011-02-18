import FWCore.ParameterSet.Config as cms

tauIDFactorizationCoefficients = cms.untracked.PSet(
factorizationSourceName = cms.untracked.string('QCD_Pt80to120_TuneZ2_Winter10'),

tauIDFactorizationByPt_signalAnalysisTauSelectionShrinkingConeCutBased_Coefficients = cms.untracked.vdouble( *(
  1e-99, 1e-99, 0.026862, 0.0071599, 0.00665102, 0.0047976, 0.00573457, 0.00520081, 0.00265856, 0.00424028, 0.0031881, 1e-99
) ),

tauIDFactorizationByPt_signalAnalysisTauSelectionShrinkingConeCutBased_CoefficientUncertainty = cms.untracked.vdouble( *(
  1e-99, 1e-99, 0.005727, 0.00206689, 0.00161311, 0.0011994, 0.00125139, 0.00122584, 0.00100484, 0.00122406, 0.00184065, 0.00763359
) ),

tauIDFactorizationByEta_signalAnalysisTauSelectionShrinkingConeCutBased_Coefficients = cms.untracked.vdouble( *(
  1e-99, 1e-99, 0.00294985, 0.00540541, 0.010101, 0.00886263, 0.0116959, 0.00595238, 0.00463392, 0.00691057, 0.00642398, 0.00601751, 0.00595238, 0.00576992, 0.00586042, 0.00430108, 0.00294118, 1e-99, 0.00324149, 0.00688073, 0.0103093, 0.00515464, 1e-99, 0.00976562, 0.00925926, 1e-99
) ),

tauIDFactorizationByEta_signalAnalysisTauSelectionShrinkingConeCutBased_CoefficientUncertainty = cms.untracked.vdouble( *(
  0.00840336, 0.0075188, 0.00294985, 0.0038222, 0.00505051, 0.00361815, 0.00477483, 0.00420897, 0.00207235, 0.00167606, 0.00262258, 0.00181435, 0.00179471, 0.00144248, 0.00176698, 0.00215054, 0.00120073, 0.00221729, 0.00229208, 0.00397259, 0.00389654, 0.00364488, 0.00497512, 0.00436732, 0.00925926, 1e-99
) ),

tauIDFactorizationByPtVsEta_signalAnalysisTauSelectionShrinkingConeCutBased_Coefficients = cms.untracked.vdouble( *(
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 0.0169492, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0689655, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.05, 0.0196078, 1e-99, 1e-99, 1e-99, 0.0238095, 1e-99, 0.0322581, 1e-99, 1e-99,
  1e-99, 1e-99, 0.03125, 1e-99, 0.00869565, 0.00854701, 0.00952381, 1e-99, 0.0169492, 0.0153846, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 0.0144928, 0.0240964, 0.0289855, 1e-99, 0.0175439, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 0.0188679, 1e-99, 1e-99, 1e-99, 1e-99, 0.0243902, 1e-99, 1e-99,
  1e-99, 1e-99, 0.025, 0.0138889, 1e-99, 1e-99, 0.0110497, 1e-99, 1e-99, 0.00657895, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0245902, 0.0075188, 0.015444, 0.00315457, 1e-99, 0.0124378, 0.0030303, 0.00289855, 0.00787402, 1e-99,
  1e-99, 1e-99, 0.0333333, 0.0153846, 1e-99, 0.0142857, 1e-99, 1e-99, 1e-99, 0.0166667, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0181818, 0.0163934, 0.00540541, 0.00757576, 0.00325733, 0.00333333, 0.00793651, 0.00406504, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0178571, 0.0070922, 0.00540541, 0.00408163, 0.00900901, 0.00671141, 0.00438596, 0.00381679, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0352941, 0.00555556, 0.00716846, 0.00479616, 0.00232558, 0.00677201, 0.00288184, 0.00229885, 0.0148148, 1e-99,
  1e-99, 1e-99, 0.0454545, 0.015625, 1e-99, 0.00369004, 0.0124611, 0.00307692, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0322581, 1e-99, 1e-99, 1e-99, 0.013245, 0.00671141, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0147059, 1e-99, 0.00454545, 0.00320513, 0.00292398, 1e-99, 0.00420168, 0.00361011, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.037037, 1e-99, 1e-99, 1e-99, 1e-99, 0.0126582, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0625, 1e-99, 0.0363636, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 0.0102041, 0.0254237, 0.016, 1e-99, 0.0128205, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 0.0322581, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 0.0277778, 0.0144928, 0.0206186, 0.00854701, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.166667, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99
) ),

tauIDFactorizationByPtVsEta_signalAnalysisTauSelectionShrinkingConeCutBased_CoefficientUncertainty = cms.untracked.vdouble( *(
  1e-99, 1e-99, 0.2, 0.0833333, 0.0909091, 0.0344828, 0.0625, 0.0454545, 0.111111, 0.0909091, 0.25, 1e-99,
  1e-99, 1e-99, 0.333333, 0.0909091, 0.0588235, 0.0344828, 0.0384615, 0.0434783, 0.0833333, 0.1, 0.5, 1e-99,
  1e-99, 1e-99, 0.0714286, 0.03125, 0.0238095, 0.015873, 0.0169492, 0.0208333, 0.03125, 0.0227273, 0.2, 1e-99,
  1e-99, 1e-99, 0.048766, 0.0333333, 0.0192308, 0.015625, 0.0196078, 0.0166667, 0.030303, 0.0243902, 0.111111, 1,
  1e-99, 1e-99, 0.05, 0.0196078, 0.02, 0.0142857, 0.0144928, 0.0238095, 0.0185185, 0.0322581, 0.166667, 0.333333,
  1e-99, 1e-99, 0.03125, 0.0136986, 0.00869565, 0.00854701, 0.00952381, 0.0113636, 0.0169492, 0.0153846, 0.0454545, 1,
  1e-99, 1e-99, 0.0384615, 0.0212766, 0.0144928, 0.0144928, 0.0170387, 0.0204958, 0.016129, 0.0175439, 0.0344828, 0.5,
  1e-99, 1e-99, 0.125, 0.0416667, 0.0188679, 0.0175439, 0.02, 0.0208333, 0.0263158, 0.0243902, 0.0666667, 0.5,
  1e-99, 1e-99, 0.025, 0.0138889, 0.00813008, 0.00641026, 0.00781333, 0.00636943, 0.00704225, 0.00657895, 0.0208333, 0.125,
  1e-99, 1e-99, 0.0141971, 0.0075188, 0.00772201, 0.00315457, 0.00246305, 0.00556236, 0.0030303, 0.00289855, 0.00787402, 0.0526316,
  1e-99, 1e-99, 0.0333333, 0.0153846, 0.0117647, 0.0101015, 0.00657895, 0.00632911, 0.00735294, 0.0117851, 0.025, 0.125,
  1e-99, 1e-99, 0.0181818, 0.0115919, 0.00540541, 0.00535687, 0.00325733, 0.00333333, 0.00561196, 0.00406504, 0.0125, 0.0588235,
  1e-99, 1e-99, 0.0178571, 0.0070922, 0.00540541, 0.00408163, 0.00520135, 0.00474568, 0.00438596, 0.00381679, 0.010989, 0.111111,
  1e-99, 1e-99, 0.0203771, 0.00555556, 0.00506887, 0.0033914, 0.00232558, 0.00390982, 0.00288184, 0.00229885, 0.0104757, 0.0454545,
  1e-99, 1e-99, 0.0262432, 0.0110485, 0.00478469, 0.00369004, 0.00623053, 0.00307692, 0.00431034, 0.004329, 0.0114943, 0.142857,
  1e-99, 1e-99, 0.0322581, 0.0140845, 0.0103093, 0.00724638, 0.00936565, 0.00671141, 0.00833333, 0.00793651, 0.0263158, 0.111111,
  1e-99, 1e-99, 0.0147059, 0.00719424, 0.00454545, 0.00320513, 0.00292398, 0.00295858, 0.00420168, 0.00361011, 0.0108696, 0.0714286,
  1e-99, 1e-99, 0.0833333, 0.027027, 0.0181818, 0.0153846, 0.0147059, 0.0131579, 0.0196078, 0.0149254, 0.0555556, 0.5,
  1e-99, 1e-99, 0.037037, 0.0163934, 0.010989, 0.0104167, 0.00934579, 0.0126582, 0.0175439, 0.0135135, 0.05, 0.2,
  1e-99, 1e-99, 0.0625, 0.0212766, 0.025713, 0.0138889, 0.0125, 0.0151515, 0.0344828, 0.0238095, 0.037037, 0.5,
  1e-99, 1e-99, 0.0285714, 0.0102041, 0.0146784, 0.0113137, 0.0102041, 0.0128205, 0.015625, 0.0208333, 0.0666667, 1e-99,
  1e-99, 1e-99, 0.0588235, 0.0204082, 0.015625, 0.0166667, 0.0228099, 0.0188679, 0.027027, 0.0285714, 0.0909091, 1e-99,
  1e-99, 1e-99, 0.25, 0.0714286, 0.0294118, 0.0238095, 0.0357143, 0.0285714, 0.05, 0.047619, 0.333333, 1e-99,
  1e-99, 1e-99, 0.0833333, 0.0277778, 0.0144928, 0.0145795, 0.00854701, 0.0119048, 0.0238095, 0.0243902, 0.0714286, 1e-99,
  1e-99, 1e-99, 0.166667, 0.333333, 0.0526316, 0.05, 0.05, 0.05, 0.111111, 0.125, 0.333333, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99
) ),

tauIDFactorizationByPt_signalAnalysisTauSelectionShrinkingConeTaNCBased_Coefficients = cms.untracked.vdouble( *(
  1e-99, 1e-99, 0.037851, 0.0131265, 0.0086072, 0.0053973, 0.0054615, 0.00751228, 0.00835549, 0.00706714, 0.0042508, 1e-99
) ),

tauIDFactorizationByPt_signalAnalysisTauSelectionShrinkingConeTaNCBased_CoefficientUncertainty = cms.untracked.vdouble( *(
  1e-99, 1e-99, 0.00679825, 0.00279858, 0.00183506, 0.00127216, 0.00122123, 0.00147328, 0.0017814, 0.00158026, 0.0021254, 0.00763359
) ),

tauIDFactorizationByEta_signalAnalysisTauSelectionShrinkingConeTaNCBased_Coefficients = cms.untracked.vdouble( *(
  1e-99, 0.0075188, 0.00294985, 0.0027027, 0.0151515, 0.00738552, 0.0194932, 0.00892857, 0.0111214, 0.00934959, 0.00856531, 0.0071116, 0.00919913, 0.00973675, 0.00745871, 0.00752688, 0.00392157, 0.00221729, 0.00972447, 0.00688073, 0.0147275, 0.0128866, 0.00497512, 0.00585938, 1e-99, 1e-99
) ),

tauIDFactorizationByEta_signalAnalysisTauSelectionShrinkingConeTaNCBased_CoefficientUncertainty = cms.untracked.vdouble( *(
  0.00840336, 0.0075188, 0.00294985, 0.0027027, 0.00618558, 0.00330291, 0.00616428, 0.00515491, 0.00321047, 0.00194953, 0.00302829, 0.0019724, 0.00223112, 0.00187384, 0.00199342, 0.00284489, 0.00138648, 0.00221729, 0.00397, 0.00397259, 0.00465726, 0.00576306, 0.00497512, 0.00338291, 0.00925926, 1e-99
) ),

tauIDFactorizationByPtVsEta_signalAnalysisTauSelectionShrinkingConeTaNCBased_Coefficients = cms.untracked.vdouble( *(
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 0.0434783, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0714286, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0344828, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.1, 0.0392157, 1e-99, 1e-99, 1e-99, 0.0238095, 1e-99, 0.0322581, 1e-99, 1e-99,
  1e-99, 1e-99, 0.03125, 1e-99, 1e-99, 1e-99, 0.00952381, 0.0113636, 0.0169492, 0.0153846, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0384615, 1e-99, 0.0144928, 1e-99, 0.0240964, 0.0434783, 0.016129, 0.0350877, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 0.0188679, 1e-99, 1e-99, 0.0208333, 1e-99, 0.0243902, 1e-99, 1e-99,
  1e-99, 1e-99, 0.025, 0.0138889, 0.0162602, 0.00641026, 0.0110497, 1e-99, 0.0211268, 0.0131579, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0245902, 0.0225564, 0.011583, 0.00315457, 0.00492611, 0.0174129, 0.0030303, 0.0057971, 0.00787402, 1e-99,
  1e-99, 1e-99, 1e-99, 0.0307692, 1e-99, 0.0142857, 1e-99, 1e-99, 0.00735294, 0.025, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0363636, 0.0163934, 0.00540541, 1e-99, 0.00651466, 0.00333333, 0.00793651, 0.00813008, 0.0125, 1e-99,
  1e-99, 1e-99, 0.0178571, 0.0070922, 0.0162162, 0.0122449, 0.00600601, 1e-99, 0.0175439, 0.0114504, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0588235, 0.0166667, 0.00716846, 0.0119904, 1e-99, 0.00902935, 0.0144092, 0.00229885, 0.0148148, 1e-99,
  1e-99, 1e-99, 0.0454545, 0.015625, 0.00956938, 0.00738007, 0.00623053, 0.00307692, 0.00431034, 0.004329, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0967742, 1e-99, 1e-99, 1e-99, 0.013245, 0.0134228, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0147059, 0.00719424, 0.00909091, 0.00320513, 0.00292398, 0.00295858, 1e-99, 0.00361011, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 0.0196078, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0740741, 0.0163934, 0.010989, 1e-99, 1e-99, 0.0126582, 0.0175439, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.125, 1e-99, 1e-99, 1e-99, 1e-99, 0.0151515, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0285714, 0.0204082, 0.0254237, 0.016, 0.0102041, 0.0128205, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0588235, 1e-99, 1e-99, 0.0166667, 0.0322581, 1e-99, 0.027027, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 0.0714286, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 0.0277778, 0.0144928, 1e-99, 0.00854701, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99
) ),

tauIDFactorizationByPtVsEta_signalAnalysisTauSelectionShrinkingConeTaNCBased_CoefficientUncertainty = cms.untracked.vdouble( *(
  1e-99, 1e-99, 0.2, 0.0833333, 0.0909091, 0.0344828, 0.0625, 0.0454545, 0.111111, 0.0909091, 0.25, 1e-99,
  1e-99, 1e-99, 0.333333, 0.0909091, 0.0588235, 0.0344828, 0.0384615, 0.0434783, 0.0833333, 0.1, 0.5, 1e-99,
  1e-99, 1e-99, 0.0714286, 0.03125, 0.0238095, 0.015873, 0.0169492, 0.0208333, 0.03125, 0.0227273, 0.2, 1e-99,
  1e-99, 1e-99, 0.0344828, 0.0333333, 0.0192308, 0.015625, 0.0196078, 0.0166667, 0.030303, 0.0243902, 0.111111, 1,
  1e-99, 1e-99, 0.0707107, 0.0277297, 0.02, 0.0142857, 0.0144928, 0.0238095, 0.0185185, 0.0322581, 0.166667, 0.333333,
  1e-99, 1e-99, 0.03125, 0.0136986, 0.00869565, 0.00854701, 0.00952381, 0.0113636, 0.0169492, 0.0153846, 0.0454545, 1,
  1e-99, 1e-99, 0.0384615, 0.0212766, 0.0144928, 0.0144928, 0.0170387, 0.0251022, 0.016129, 0.0248108, 0.0344828, 0.5,
  1e-99, 1e-99, 0.125, 0.0416667, 0.0188679, 0.0175439, 0.02, 0.0208333, 0.0263158, 0.0243902, 0.0666667, 0.5,
  1e-99, 1e-99, 0.025, 0.0138889, 0.0114977, 0.00641026, 0.00781333, 0.00636943, 0.0121975, 0.00930404, 0.0208333, 0.125,
  1e-99, 1e-99, 0.0141971, 0.0130229, 0.00668745, 0.00315457, 0.00348328, 0.00658147, 0.0030303, 0.00409917, 0.00787402, 0.0526316,
  1e-99, 1e-99, 0.0333333, 0.0217571, 0.0117647, 0.0101015, 0.00657895, 0.00632911, 0.00735294, 0.0144338, 0.025, 0.125,
  1e-99, 1e-99, 0.025713, 0.0115919, 0.00540541, 0.00378788, 0.00460656, 0.00333333, 0.00561196, 0.00574884, 0.0125, 0.0588235,
  1e-99, 1e-99, 0.0178571, 0.0070922, 0.00936244, 0.0070696, 0.00424689, 0.0033557, 0.00877193, 0.00661088, 0.010989, 0.111111,
  1e-99, 1e-99, 0.0263067, 0.0096225, 0.00506887, 0.00536227, 0.00232558, 0.00451467, 0.006444, 0.00229885, 0.0104757, 0.0454545,
  1e-99, 1e-99, 0.0262432, 0.0110485, 0.00676657, 0.0052185, 0.00440565, 0.00307692, 0.00431034, 0.004329, 0.0114943, 0.142857,
  1e-99, 1e-99, 0.0558726, 0.0140845, 0.0103093, 0.00724638, 0.00936565, 0.00949137, 0.00833333, 0.00793651, 0.0263158, 0.111111,
  1e-99, 1e-99, 0.0147059, 0.00719424, 0.00642824, 0.00320513, 0.00292398, 0.00295858, 0.00420168, 0.00361011, 0.0108696, 0.0714286,
  1e-99, 1e-99, 0.0833333, 0.027027, 0.0181818, 0.0153846, 0.0147059, 0.0131579, 0.0196078, 0.0149254, 0.0555556, 0.5,
  1e-99, 1e-99, 0.0523783, 0.0163934, 0.010989, 0.0104167, 0.00934579, 0.0126582, 0.0175439, 0.0135135, 0.05, 0.2,
  1e-99, 1e-99, 0.0883883, 0.0212766, 0.0181818, 0.0138889, 0.0125, 0.0151515, 0.0344828, 0.0238095, 0.037037, 0.5,
  1e-99, 1e-99, 0.0285714, 0.0144308, 0.0146784, 0.0113137, 0.0102041, 0.0128205, 0.015625, 0.0208333, 0.0666667, 1e-99,
  1e-99, 1e-99, 0.0588235, 0.0204082, 0.015625, 0.0166667, 0.0228099, 0.0188679, 0.027027, 0.0285714, 0.0909091, 1e-99,
  1e-99, 1e-99, 0.25, 0.0714286, 0.0294118, 0.0238095, 0.0357143, 0.0285714, 0.05, 0.047619, 0.333333, 1e-99,
  1e-99, 1e-99, 0.0833333, 0.0277778, 0.0144928, 0.0103093, 0.00854701, 0.0119048, 0.0238095, 0.0243902, 0.0714286, 1e-99,
  1e-99, 1e-99, 0.166667, 0.333333, 0.0526316, 0.05, 0.05, 0.05, 0.111111, 0.125, 0.333333, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99
) ),

tauIDFactorizationByPt_signalAnalysisTauSelectionHPSTauBased_Coefficients = cms.untracked.vdouble( *(
  1e-99, 1e-99, 0.00256035, 0.00166826, 0.00131752, 0.00110742, 0.0020145, 0.0020562, 0.0013089, 0.00744879, 0.00952381, 1e-99
) ),

tauIDFactorizationByPt_signalAnalysisTauSelectionHPSTauBased_CoefficientUncertainty = cms.untracked.vdouble( *(
  1e-99, 1e-99, 0.000967722, 0.000630541, 0.000537877, 0.00055371, 0.000900914, 0.00118715, 0.0013089, 0.00372439, 0.00952381, 0.0909091
) ),

tauIDFactorizationByEta_signalAnalysisTauSelectionHPSTauBased_Coefficients = cms.untracked.vdouble( *(
  1e-99, 1e-99, 1e-99, 0.00302115, 0.00534759, 1e-99, 0.00209205, 0.00645161, 1e-99, 0.00218055, 0.00348028, 0.00231616, 0.00175953, 0.0019685, 0.00280741, 0.00120482, 0.000523834, 1e-99, 0.00175439, 1e-99, 0.00156986, 1e-99, 1e-99, 0.00626305, 1e-99, 1e-99
) ),

tauIDFactorizationByEta_signalAnalysisTauSelectionHPSTauBased_CoefficientUncertainty = cms.untracked.vdouble( *(
  0.00917431, 0.00840336, 0.00315457, 0.00302115, 0.00378132, 0.00159744, 0.00209205, 0.00456198, 0.000996016, 0.000975171, 0.00200934, 0.00115808, 0.00101587, 0.000880342, 0.00125551, 0.00120482, 0.000523834, 0.00246305, 0.00175439, 0.00251256, 0.00156986, 0.00278552, 0.00531915, 0.00361597, 0.00980392, 1e-99
) ),

tauIDFactorizationByPtVsEta_signalAnalysisTauSelectionHPSTauBased_Coefficients = cms.untracked.vdouble( *(
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0181818, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 0.0123457, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 0.333333, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 0.0333333, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 0.0126582, 1e-99, 1e-99, 1e-99, 1e-99, 0.166667, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.00677966, 0.00233645, 0.00195312, 1e-99, 1e-99, 0.00657895, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.00990099, 1e-99, 1e-99, 0.0060241, 1e-99, 1e-99, 1e-99, 0.0384615, 1e-99, 1e-99,
  1e-99, 1e-99, 0.00507614, 0.00302115, 0.00243902, 0.00327869, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 0.003003, 0.0027027, 1e-99, 0.00429185, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0031746, 0.00217391, 1e-99, 1e-99, 1e-99, 1e-99, 0.00847458, 0.0144928, 0.0769231, 1e-99,
  1e-99, 1e-99, 0.0045045, 0.00266667, 1e-99, 0.00291545, 0.00892857, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 0.010101, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 0.00242131, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 0.025, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 0.00671141, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 0.00862069, 0.0111111, 0.015625, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99
) ),

tauIDFactorizationByPtVsEta_signalAnalysisTauSelectionHPSTauBased_CoefficientUncertainty = cms.untracked.vdouble( *(
  1e-99, 1e-99, 0.0769231, 0.037037, 0.04, 0.0454545, 0.0769231, 0.2, 0.333333, 1, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0909091, 0.04, 0.0285714, 0.047619, 0.0833333, 0.2, 0.142857, 0.333333, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0294118, 0.0135135, 0.0144928, 0.0204082, 0.0222222, 0.0384615, 0.111111, 0.0909091, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0181818, 0.0151515, 0.0147059, 0.0192308, 0.0232558, 0.037037, 0.0833333, 0.142857, 1, 1e-99,
  1e-99, 1e-99, 0.0133333, 0.0123457, 0.0121951, 0.0169492, 0.025, 0.05, 0.0833333, 0.333333, 1, 1,
  1e-99, 1e-99, 0.00943396, 0.00675676, 0.00746269, 0.010989, 0.0147059, 0.0277778, 0.0416667, 0.0625, 0.5, 1,
  1e-99, 1e-99, 0.0138889, 0.00934579, 0.00980392, 0.011236, 0.0227273, 0.0333333, 0.047619, 0.111111, 0.333333, 1,
  1e-99, 1e-99, 0.0243902, 0.015873, 0.0126582, 0.0188679, 0.037037, 0.0344828, 0.0909091, 0.166667, 1, 1e-99,
  1e-99, 1e-99, 0.00719424, 0.00465116, 0.00507614, 0.00546448, 0.00826446, 0.0138889, 0.0227273, 0.037037, 0.2, 1,
  1e-99, 1e-99, 0.00479394, 0.00233645, 0.00195312, 0.00238095, 0.00340136, 0.00657895, 0.00970874, 0.0135135, 0.0666667, 1e-99,
  1e-99, 1e-99, 0.00990099, 0.00571429, 0.00537634, 0.0060241, 0.00925926, 0.0151515, 0.0344828, 0.0384615, 0.25, 1,
  1e-99, 1e-99, 0.00507614, 0.00302115, 0.00243902, 0.00327869, 0.00465116, 0.00724638, 0.0144928, 0.0204082, 0.0833333, 1,
  1e-99, 1e-99, 0.00473934, 0.003003, 0.0027027, 0.00314465, 0.00429185, 0.00819672, 0.0175439, 0.0204082, 0.0833333, 1e-99,
  1e-99, 1e-99, 0.0031746, 0.00217391, 0.00175439, 0.00211864, 0.00319489, 0.00478469, 0.00847458, 0.0144928, 0.0769231, 1,
  1e-99, 1e-99, 0.0045045, 0.00266667, 0.00265957, 0.00291545, 0.00631345, 0.00826446, 0.0185185, 0.0185185, 0.0909091, 1,
  1e-99, 1e-99, 0.00943396, 0.00595238, 0.00540541, 0.00671141, 0.010101, 0.0149254, 0.027027, 0.0625, 0.333333, 1e-99,
  1e-99, 1e-99, 0.00408163, 0.00242131, 0.00229885, 0.00314465, 0.00429185, 0.00714286, 0.015625, 0.0208333, 0.1, 0.333333,
  1e-99, 1e-99, 0.0196078, 0.0125, 0.0105263, 0.0136986, 0.0238095, 0.027027, 0.0714286, 0.1, 0.25, 1e-99,
  1e-99, 1e-99, 0.0102041, 0.00806452, 0.00833333, 0.0117647, 0.0138889, 0.025, 0.0555556, 0.0909091, 0.5, 1e-99,
  1e-99, 1e-99, 0.0144928, 0.0116279, 0.0113636, 0.0153846, 0.025, 0.0454545, 0.0625, 0.0909091, 1, 1e-99,
  1e-99, 1e-99, 0.00840336, 0.00606061, 0.00671141, 0.0116279, 0.0149254, 0.0434783, 0.0769231, 0.0769231, 0.5, 1e-99,
  1e-99, 1e-99, 0.0153846, 0.012987, 0.0135135, 0.0169492, 0.0243902, 0.0434783, 0.0833333, 0.125, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0357143, 0.02, 0.0227273, 0.037037, 0.0588235, 0.0714286, 0.333333, 0.2, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0181818, 0.00925926, 0.00862069, 0.0111111, 0.015625, 0.04, 0.0833333, 0.125, 1, 1e-99,
  1e-99, 1e-99, 0.0909091, 0.0588235, 0.030303, 0.0588235, 0.142857, 0.1, 0.5, 0.333333, 0.5, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99
) ),

tauIDFactorizationByPt_signalAnalysisTauSelectionCaloTauCutBased_Coefficients = cms.untracked.vdouble( *(
  1e-99, 1e-99, 0.0535714, 0.0156627, 0.0151172, 0.00958144, 0.00554939, 0.00836282, 0.00545331, 0.0033359, 0.00262467, 0.00263852
) ),

tauIDFactorizationByPt_signalAnalysisTauSelectionCaloTauCutBased_CoefficientUncertainty = cms.untracked.vdouble( *(
  1e-99, 1e-99, 0.0116902, 0.00434404, 0.0033803, 0.00219813, 0.00143285, 0.00164008, 0.00136333, 0.000925212, 0.00117379, 0.00263852
) ),

tauIDFactorizationByEta_signalAnalysisTauSelectionCaloTauCutBased_Coefficients = cms.untracked.vdouble( *(
  1e-99, 1e-99, 0.00946372, 0.0114943, 0.0131579, 0.0045977, 0.0195122, 0.00877193, 0.00614754, 0.00720396, 0.00622084, 0.00792303, 0.00668693, 0.00869565, 0.00591716, 0.00694444, 0.00503919, 0.00221729, 0.00553506, 0.013544, 0.0111111, 0.0132979, 0.00534759, 0.0103306, 0.00990099, 1e-99
) ),

tauIDFactorizationByEta_signalAnalysisTauSelectionCaloTauCutBased_CoefficientUncertainty = cms.untracked.vdouble( *(
  0.00892857, 0.00806452, 0.00546388, 0.00574713, 0.00588439, 0.00325107, 0.0068986, 0.00506448, 0.00250972, 0.00180099, 0.00311042, 0.00211752, 0.00201619, 0.00185392, 0.00197239, 0.00283506, 0.00167973, 0.00221729, 0.00319567, 0.00552932, 0.00496904, 0.00594699, 0.00534759, 0.00461998, 0.00990099, 1e-99
) ),

tauIDFactorizationByPtVsEta_signalAnalysisTauSelectionCaloTauCutBased_Coefficients = cms.untracked.vdouble( *(
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 0.0384615, 1e-99, 0.0181818, 1e-99, 1e-99, 0.0185185, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0869565, 0.0666667, 0.037037, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 0.0714286, 1e-99, 1e-99, 0.0172414, 0.0178571, 1e-99, 1e-99, 0.0384615, 1e-99,
  1e-99, 1e-99, 0.2, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.222222, 1e-99, 1e-99, 0.0238095, 1e-99, 0.0508475, 0.0434783, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 0.0344828, 1e-99, 1e-99, 0.0144928, 1e-99, 0.0196078, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0357143, 1e-99, 0.016129, 0.0107527, 0.00735294, 1e-99, 1e-99, 0.0111111, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0212766, 0.0116279, 0.023622, 0.0106383, 0.00687285, 0.012012, 0.00285714, 0.00209644, 0.00362319, 1e-99,
  1e-99, 1e-99, 1e-99, 0.0322581, 1e-99, 1e-99, 1e-99, 0.01, 1e-99, 0.0135135, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 0.015873, 0.019802, 0.0180723, 0.00395257, 0.00318471, 0.00743494, 0.00802139, 0.00581395, 1e-99,
  1e-99, 1e-99, 0.0454545, 1e-99, 0.00869565, 0.0134228, 0.00434783, 0.0147601, 0.003861, 1e-99, 0.00632911, 1e-99,
  1e-99, 1e-99, 0.0465116, 0.0344828, 0.0135135, 0.0121457, 1e-99, 0.0097561, 0.0124688, 0.0018018, 0.00363636, 0.0172414,
  1e-99, 1e-99, 0.0740741, 0.0333333, 1e-99, 0.0234375, 0.00490196, 1e-99, 1e-99, 0.003367, 1e-99, 1e-99,
  1e-99, 1e-99, 0.133333, 1e-99, 0.0163934, 1e-99, 1e-99, 0.0155039, 0.00763359, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0645161, 0.0135135, 0.0169492, 0.00492611, 0.00420168, 0.00699301, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 0.0140845, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0588235, 1e-99, 1e-99, 0.0166667, 1e-99, 1e-99, 0.0142857, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 0.0384615, 0.0294118, 1e-99, 0.0149254, 0.0273973, 0.02, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0526316, 1e-99, 0.0416667, 0.0140845, 0.0144928, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.111111, 1e-99, 1e-99, 1e-99, 0.0212766, 0.0169492, 0.0192308, 0.015625, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 0.0333333, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 0.0606061, 0.0212766, 0.0190476, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.25, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99
) ),

tauIDFactorizationByPtVsEta_signalAnalysisTauSelectionCaloTauCutBased_CoefficientUncertainty = cms.untracked.vdouble( *(
  1e-99, 1e-99, 0.5, 0.142857, 0.142857, 0.0714286, 0.0714286, 0.0625, 0.0666667, 0.0384615, 0.1, 1,
  1e-99, 1e-99, 1, 0.142857, 0.142857, 0.0526316, 0.0625, 0.0555556, 0.0625, 0.037037, 0.0909091, 0.5,
  1e-99, 1e-99, 0.142857, 0.0833333, 0.0384615, 0.037037, 0.0181818, 0.0188679, 0.0196078, 0.0185185, 0.04, 0.142857,
  1e-99, 1e-99, 0.0614875, 0.0666667, 0.037037, 0.025, 0.0163934, 0.0185185, 0.0232558, 0.0163934, 0.047619, 0.333333,
  1e-99, 1e-99, 0.125, 0.0505076, 0.0344828, 0.0188679, 0.0172414, 0.0178571, 0.0163934, 0.0181818, 0.0384615, 0.166667,
  1e-99, 1e-99, 0.141421, 0.0526316, 0.027027, 0.015625, 0.0169492, 0.0140845, 0.0181818, 0.0116279, 0.04, 0.111111,
  1e-99, 1e-99, 0.157135, 0.04, 0.025, 0.0238095, 0.015625, 0.0293568, 0.0307438, 0.012987, 0.027027, 0.0909091,
  1e-99, 1e-99, 0.125, 0.0769231, 0.0344828, 0.0294118, 0.025641, 0.0144928, 0.0172414, 0.0196078, 0.0277778, 0.2,
  1e-99, 1e-99, 0.0357143, 0.0294118, 0.016129, 0.0107527, 0.00735294, 0.00666667, 0.00649351, 0.00785674, 0.00862069, 0.0434783,
  1e-99, 1e-99, 0.0212766, 0.0116279, 0.0136382, 0.00752241, 0.00485984, 0.00600601, 0.00285714, 0.00209644, 0.00362319, 0.0217391,
  1e-99, 1e-99, 0.111111, 0.0322581, 0.0333333, 0.0192308, 0.0119048, 0.01, 0.00862069, 0.0095555, 0.0175439, 0.0625,
  1e-99, 1e-99, 0.0416667, 0.015873, 0.0140021, 0.010434, 0.00395257, 0.00318471, 0.0052573, 0.00463115, 0.00581395, 0.0322581,
  1e-99, 1e-99, 0.0454545, 0.0142857, 0.00869565, 0.00949137, 0.00434783, 0.00738007, 0.003861, 0.00294985, 0.00632911, 0.03125,
  1e-99, 1e-99, 0.0328887, 0.0199086, 0.0095555, 0.00701235, 0.00326797, 0.00487805, 0.00557623, 0.0018018, 0.00363636, 0.0172414,
  1e-99, 1e-99, 0.0523783, 0.0235702, 0.00884956, 0.0135316, 0.00490196, 0.00381679, 0.00403226, 0.003367, 0.00657895, 0.0333333,
  1e-99, 1e-99, 0.0942809, 0.0294118, 0.0163934, 0.0113636, 0.00884956, 0.0109629, 0.00763359, 0.00526316, 0.010989, 0.0833333,
  1e-99, 1e-99, 0.0456198, 0.0135135, 0.0119849, 0.00492611, 0.00420168, 0.0049448, 0.00381679, 0.00273973, 0.00595238, 0.0243902,
  1e-99, 1e-99, 0.125, 0.0357143, 0.0333333, 0.0238095, 0.0169492, 0.0169492, 0.0140845, 0.0105263, 0.0188679, 0.166667,
  1e-99, 1e-99, 0.0588235, 0.04, 0.02, 0.0166667, 0.0111111, 0.0121951, 0.0142857, 0.01, 0.0243902, 0.142857,
  1e-99, 1e-99, 0.1, 0.0384615, 0.0294118, 0.0144928, 0.0149254, 0.0193728, 0.02, 0.016129, 0.0238095, 0.1,
  1e-99, 1e-99, 0.0526316, 0.0243902, 0.0294628, 0.0140845, 0.0144928, 0.0212766, 0.0192308, 0.0131579, 0.0454545, 0.2,
  1e-99, 1e-99, 0.111111, 0.0384615, 0.0294118, 0.0208333, 0.0212766, 0.0169492, 0.0192308, 0.015625, 0.0333333, 0.142857,
  1e-99, 1e-99, 0.333333, 0.142857, 0.0714286, 0.0526316, 0.0333333, 0.0238095, 0.037037, 0.0344828, 0.0666667, 1,
  1e-99, 1e-99, 0.125, 0.0909091, 0.042855, 0.0212766, 0.0134687, 0.0120482, 0.016129, 0.0113636, 0.025641, 0.125,
  1e-99, 1e-99, 0.25, 1, 0.333333, 0.05, 0.0666667, 0.0769231, 0.0666667, 0.047619, 0.142857, 0.5,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99
) ),

tauIDFactorizationByPt_signalAnalysisTauSelectionCombinedHPSTaNCBased_Coefficients = cms.untracked.vdouble( *(
  1e-99, 1e-99, 0.00221566, 0.000797024, 0.00125723, 0.000621504, 0.00087604, 0.00148368, 1e-99, 0.00376648, 1e-99, 1e-99
) ),

tauIDFactorizationByPt_signalAnalysisTauSelectionCombinedHPSTaNCBased_CoefficientUncertainty = cms.untracked.vdouble( *(
  1e-99, 1e-99, 0.000904538, 0.000460162, 0.00056225, 0.00043947, 0.000619454, 0.00104912, 0.00130548, 0.0026633, 0.00970874, 0.0714286
) ),

tauIDFactorizationByEta_signalAnalysisTauSelectionCombinedHPSTaNCBased_Coefficients = cms.untracked.vdouble( *(
  1e-99, 1e-99, 1e-99, 0.00327869, 0.00294985, 1e-99, 0.00236967, 0.00348432, 1e-99, 0.00096432, 0.00249066, 0.00188088, 0.00126263, 0.000844595, 0.00188324, 1e-99, 1e-99, 1e-99, 0.00192678, 1e-99, 1e-99, 1e-99, 1e-99, 0.00678733, 1e-99, 1e-99
) ),

tauIDFactorizationByEta_signalAnalysisTauSelectionCombinedHPSTaNCBased_CoefficientUncertainty = cms.untracked.vdouble( *(
  0.00952381, 0.00869565, 0.0033557, 0.00327869, 0.00294985, 0.00171527, 0.00236967, 0.00348432, 0.00111732, 0.000681877, 0.00176116, 0.00108593, 0.000892812, 0.000597219, 0.00108729, 0.00132979, 0.000579039, 0.00262467, 0.00192678, 0.00271003, 0.00172117, 0.00316456, 0.00625, 0.00391867, 0.010101, 1e-99
) ),

tauIDFactorizationByPtVsEta_signalAnalysisTauSelectionCombinedHPSTaNCBased_Coefficients = cms.untracked.vdouble( *(
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0169492, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 0.25, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 0.0416667, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 0.0140845, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0035461, 1e-99, 0.00225225, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.00909091, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 0.0416667, 1e-99, 1e-99,
  1e-99, 1e-99, 0.00487805, 1e-99, 0.00301205, 0.00338983, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 0.00314465, 0.00303951, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.00306748, 0.00236967, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.00446429, 0.00292398, 1e-99, 1e-99, 0.00537634, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 0.0277778, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 0.01, 0.0116279, 0.0163934, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99
) ),

tauIDFactorizationByPtVsEta_signalAnalysisTauSelectionCombinedHPSTaNCBased_CoefficientUncertainty = cms.untracked.vdouble( *(
  1e-99, 1e-99, 0.0769231, 0.0434783, 0.04, 0.05, 0.0769231, 0.142857, 0.25, 1e-99, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0833333, 0.0384615, 0.0344828, 0.05, 0.0769231, 0.2, 0.142857, 0.333333, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0277778, 0.0163934, 0.015625, 0.0208333, 0.0227273, 0.0416667, 0.111111, 0.0909091, 1, 1e-99,
  1e-99, 1e-99, 0.0169492, 0.0175439, 0.015873, 0.0208333, 0.0294118, 0.04, 0.0833333, 0.2, 1, 1,
  1e-99, 1e-99, 0.0149254, 0.0136986, 0.015873, 0.0166667, 0.03125, 0.04, 0.0833333, 0.25, 1, 0.5,
  1e-99, 1e-99, 0.00884956, 0.00826446, 0.00819672, 0.0123457, 0.0149254, 0.0294118, 0.0434783, 0.047619, 1, 1e-99,
  1e-99, 1e-99, 0.012987, 0.00970874, 0.0123457, 0.015873, 0.027027, 0.0416667, 0.047619, 0.0909091, 0.25, 1,
  1e-99, 1e-99, 0.0277778, 0.015625, 0.0140845, 0.0222222, 0.037037, 0.0384615, 0.125, 0.125, 0.5, 1e-99,
  1e-99, 1e-99, 0.0078125, 0.00537634, 0.00561798, 0.00621118, 0.00952381, 0.015873, 0.0227273, 0.0434783, 0.166667, 1,
  1e-99, 1e-99, 0.0035461, 0.00261097, 0.00225225, 0.00274725, 0.003663, 0.00675676, 0.00980392, 0.0151515, 0.0833333, 1e-99,
  1e-99, 1e-99, 0.00909091, 0.00671141, 0.00588235, 0.00775194, 0.00869565, 0.0149254, 0.03125, 0.0416667, 0.166667, 1,
  1e-99, 1e-99, 0.00487805, 0.00321543, 0.00301205, 0.00338983, 0.00507614, 0.00775194, 0.0144928, 0.0204082, 0.125, 1e-99,
  1e-99, 1e-99, 0.00440529, 0.00314465, 0.00303951, 0.00380228, 0.00480769, 0.00833333, 0.0163934, 0.0212766, 0.0909091, 1e-99,
  1e-99, 1e-99, 0.00306748, 0.00236967, 0.00199203, 0.00239808, 0.00334448, 0.00515464, 0.00847458, 0.012987, 0.0909091, 0.5,
  1e-99, 1e-99, 0.00446429, 0.00292398, 0.003003, 0.00357143, 0.00537634, 0.00917431, 0.0185185, 0.0192308, 0.1, 0.333333,
  1e-99, 1e-99, 0.00934579, 0.00680272, 0.00636943, 0.00724638, 0.011236, 0.0175439, 0.025641, 0.0714286, 0.25, 1e-99,
  1e-99, 1e-99, 0.00411523, 0.00287356, 0.00276243, 0.00319489, 0.00454545, 0.00847458, 0.0163934, 0.0212766, 0.0833333, 0.333333,
  1e-99, 1e-99, 0.0188679, 0.015625, 0.0113636, 0.0131579, 0.0243902, 0.0344828, 0.0769231, 0.0833333, 0.2, 1e-99,
  1e-99, 1e-99, 0.0126582, 0.00793651, 0.00877193, 0.0138889, 0.0166667, 0.0277778, 0.0526316, 0.1, 0.333333, 1e-99,
  1e-99, 1e-99, 0.015873, 0.0114943, 0.012987, 0.015873, 0.030303, 0.0666667, 0.0555556, 0.0833333, 1, 1e-99,
  1e-99, 1e-99, 0.00892857, 0.00793651, 0.00689655, 0.0125, 0.0153846, 0.0357143, 0.0769231, 0.0909091, 1, 1e-99,
  1e-99, 1e-99, 0.02, 0.0138889, 0.0153846, 0.0208333, 0.025641, 0.0434783, 0.1, 0.111111, 1e-99, 1e-99,
  1e-99, 1e-99, 0.04, 0.03125, 0.0285714, 0.0357143, 0.0526316, 0.0909091, 0.25, 0.166667, 1e-99, 1e-99,
  1e-99, 1e-99, 0.0196078, 0.00980392, 0.01, 0.0116279, 0.0163934, 0.0434783, 0.0909091, 0.142857, 1, 1e-99,
  1e-99, 1e-99, 0.1, 0.047619, 0.0357143, 0.05, 0.166667, 0.125, 0.5, 0.5, 0.5, 1e-99,
  1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99, 1e-99
) ),

)