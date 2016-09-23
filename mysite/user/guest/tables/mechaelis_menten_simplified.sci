{
  "SciSheets_Class": "<class 'scisheets.ui.dt_table.DTTable'>",
  "_columns": [
    {
      "SciSheets_Class": "<class 'scisheets.core.column.Column'>",
      "_asis": true,
      "_cells": [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6"
      ],
      "_formula": null,
      "_name": "row"
    },
    {
      "SciSheets_Class": "<class 'scisheets.core.column.Column'>",
      "_asis": false,
      "_cells": [
        0.01,
        0.05,
        0.12,
        0.2,
        0.5,
        1.0
      ],
      "_formula": null,
      "_name": "S"
    },
    {
      "SciSheets_Class": "<class 'scisheets.core.column.Column'>",
      "_asis": false,
      "_cells": [
        0.11,
        0.19,
        0.21,
        0.22,
        0.21,
        0.24
      ],
      "_formula": null,
      "_name": "V"
    },
    {
      "SciSheets_Class": "<class 'scisheets.core.column.Column'>",
      "_asis": false,
      "_cells": [
        0.229,
        NaN,
        NaN,
        NaN,
        NaN,
        NaN
      ],
      "_formula": "V_MAX, K_M = MM(S,V)",
      "_name": "V_MAX"
    },
    {
      "SciSheets_Class": "<class 'scisheets.core.column.Column'>",
      "_asis": false,
      "_cells": [
        0.011,
        NaN,
        NaN,
        NaN,
        NaN,
        NaN
      ],
      "_formula": null,
      "_name": "K_M"
    }
  ],
  "_epilogue_formula": "# Prologue\nimport math as mt\nimport numpy as np\nfrom os import listdir\nfrom os.path import isfile, join\nimport pandas as pd\nimport scipy as sp\nfrom numpy import nan  # Must follow sympy import \n",
  "_filepath": "/home/ubuntu/SciSheets/mysite/user/guest/tables/mechaelis_menten_simplified.pcl",
  "_hidden_columns": [],
  "_is_evaluate_formulas": true,
  "_name": "MechaelisMenton",
  "_prologue_formula": "# Prologue\nimport math as mt\nimport numpy as np\nfrom os import listdir\nfrom os.path import isfile, join\nimport pandas as pd\nimport scipy as sp\nfrom numpy import nan  # Must follow sympy import \n"
}