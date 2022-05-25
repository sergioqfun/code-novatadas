{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled2.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNuGOeYTkuiFem0L2Lj/YUP",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sergioqfun/code-novatadas/blob/main/conversordemoneda1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wB-Rbw8_4gUJ",
        "outputId": "c107641f-cbb7-4ba9-d0b6-b15a2d428040"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Tienes dinero \n",
            "Nosotros la convertimos \n",
            "1 - pesos colombianos\n",
            "2 - pesos argentinos\n",
            "3 - pesos mexicanos\n",
            "Elige una opción: 3\n",
            "¿cuanto pesosmexicanostienes?;  676786786786\n",
            "Tienes  $20508690508.667dolares\n"
          ]
        }
      ],
      "source": [
        "def conversor (tipo_pesos, valor_dolar):\n",
        "  pesos = input(\"¿cuanto pesos\" + tipo_pesos + \"tienes?;  \") \n",
        "  pesos = float(pesos)\n",
        "  dolares = pesos / valor_dolar \n",
        "  dolares = round(dolares, 3)\n",
        "  dolares = str(dolares)\n",
        "  print(\"Tienes  $\" + dolares + \"dolares\")\n",
        "\n",
        "menu = \"\"\"\n",
        "Tienes dinero \n",
        "Nosotros la convertimos \n",
        "1 - pesos colombianos\n",
        "2 - pesos argentinos\n",
        "3 - pesos mexicanos\n",
        "Elige una opción: \"\"\"\n",
        "\n",
        "opción = int(input(menu))\n",
        "\n",
        "if opción == 1:\n",
        "  conversor(\"colombianos\", 3888 )\n",
        "elif opción == 2:\n",
        "  conversor(\"argentinos\", 79)\n",
        "elif opción == 3:\n",
        "  conversor(\"mexicanos\", 33)\n",
        "else:\n",
        "  print(\"ingresa una opción valida\") \n"
      ]
    }
  ]
}