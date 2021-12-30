# Java version action

[![GitHub license](https://img.shields.io/github/license/Daniele-Tentoni/java-version-action)](https://github.com/Daniele-Tentoni/java-version-action/blob/main/LICENSE) [![GitHub issues](https://img.shields.io/github/issues/Daniele-Tentoni/java-version-action)](https://github.com/Daniele-Tentoni/java-version-action/issues) [![Release new version](https://github.com/Daniele-Tentoni/java-version-action/actions/workflows/release.yml/badge.svg)](https://github.com/Daniele-Tentoni/java-version-action/actions/workflows/release.yml) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/8ebc15210eff4ce0b068d1bd16d1f983)](https://www.codacy.com/gh/Daniele-Tentoni/java-version-action/dashboard?utm_source=github.com&utm_medium=referral&utm_content=Daniele-Tentoni/java-version-action&utm_campaign=Badge_Grade) [![Codacy Badge](https://app.codacy.com/project/badge/Coverage/8ebc15210eff4ce0b068d1bd16d1f983)](https://www.codacy.com/gh/Daniele-Tentoni/java-version-action/dashboard?utm_source=github.com&utm_medium=referral&utm_content=Daniele-Tentoni/java-version-action&utm_campaign=Badge_Coverage) [![semantic-release: angular](https://img.shields.io/badge/semantic--release-angular-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)

Action made for Laboratory of Software Systems at University of Bologna Engineering and Computer Science Double Degree.

Use in tandem with [My Setup Java Version Action](https://github.com/Daniele-Tentoni/my-setup-java-action).

## Usage

### Basic (and only)

This code come from My Setup Java Version [action.yml](https://github.com/Daniele-Tentoni/my-setup-java-action/blob/e9ab6f947f57f3eb7394a29e2e6c78f81830be59/action.yml#L12)

```yaml
steps:
  # You can refer to this step using the java-version id.
  - name: Get the latest java version supported
    id: java-version
    uses: daniele-tentoni/java-version-action@2

  # So you can use it in another steps.
  - name: Setup Java
    id: setup-java
    uses: actions/setup-java@v2.5.0
    with:
      distribution: "adopt"
      java-version: ${{ steps.java-version.outputs.java-version }}
```
