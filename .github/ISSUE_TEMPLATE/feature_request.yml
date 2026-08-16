name: "✨ Feature Request"
description: "Suggest a new tool, panel submodule, or layout adjustment"
title: "[Feature]: "
labels: ["enhancement"]
body:
  - type: textarea
    id: problem
    attributes:
      label: "Is your feature request related to a problem?"
      description: "A clear description of what the limitation is."
      placeholder: "e.g., The current Color & Effects suite lacks a specific conversion feature..."
    validations:
      required: false

  - type: textarea
    id: solution
    attributes:
      label: "Describe the Proposed Solution"
      description: "Provide a detailed breakdown of the visual panel component or parameter update you want added."
      placeholder: "e.g., Add a sub-cog view under effects_cogs to manage localized convolution matrices dynamically..."
    validations:
      required: true

  - type: dropdown
    id: architectural-target
    attributes:
      label: "Target Architectural Module"
      description: "Which part of the MagickStudio layout does this change affect?"
      options:
        - "Geometry Suite (geometry.py)"
        - "Color & Effects Core (effects.py)"
        - "Mass Batch Processing Engine (batch.py)"
        - "Diagnostics Log Console (raw.py)"
        - "Documentation / Help Panel (documentation.py)"
        - "General App Container / Styling Guide"
    validations:
      required: true

  - type: textarea
    id: alternatives
    attributes:
      label: "Describe alternatives you've considered"
      description: "Any alternative solutions or features you've evaluated."

  - type: checkboxes
    id: contribution-intent
    attributes:
      label: "Contribution Check"
      options:
        - label: "I am willing to submit a Pull Request to implement this feature myself."
          required: false
