name: "🐛 Bug Report"
description: "Report a bug or unexpected behavior in Magick Studio"
title: "[Bug]: "
labels: ["bug", "triage"]
body:
  - type: markdown
    attributes:
      value: |
        Thank you for reporting a bug! Please fill out this form as accurately as possible to help us debug.
  
  - type: textarea
    id: description
    attributes:
      label: "Bug Description"
      description: "A clear and concise description of what the bug is."
      placeholder: "e.g., The batch processing engine crashes when utilizing a specific custom extension filter..."
    validations:
      required: true

  - type: textarea
    id: reproduction
    attributes:
      label: "Steps to Reproduce"
      description: "Steps to reproduce the behavior."
      placeholder: |
        1. Run 'python main.py'
        2. Click on the 'Geometry' tab
        3. Attempt to use -crop boundary extractions
        4. See error...
    validations:
      required: true

  - type: dropdown
    id: environment-os
    attributes:
      label: "Operating System"
      options:
        - "Windows (Using launch.vbs)"
        - "Windows (Command Line)"
        - "macOS"
        - "Linux"
    validations:
      required: true

  - type: textarea
    id: environment-details
    attributes:
      label: "Environment & Dependencies"
      description: "Provide your environment tool versions."
      value: |
        - Python Version: 3.10+
        - ImageMagick Binary Path Configured: [Yes/No]
        - CustomTkinter Version: 
        - Pillow Version: 
    validations:
      required: true

  - type: textarea
    id: logs
    attributes:
      label: "Diagnostics Log Console / Terminal Output"
      description: "Paste any raw errors from your terminal or the built-in diagnostics log console here."
      render: shell

  - type: checkboxes
    id: checkboxes
    attributes:
      label: "Validation Check"
      options:
        - label: "I have verified that ImageMagick is bound to my System PATH variables."
          required: true
        - label: "I am running Python v3.10 or higher."
          required: true
