## [2.0.1](https://github.com/Daniele-Tentoni/java-version-action/compare/2.0.0...2.0.1) (2022-11-02)


### Bug Fixes

* **cli:** add an help 'subcommand' ([c5920b2](https://github.com/Daniele-Tentoni/java-version-action/commit/c5920b22d9c7fcbff77a0a62e9dac80279c4e850))
* support new format of gradle compatibility page ([0aab55e](https://github.com/Daniele-Tentoni/java-version-action/commit/0aab55efa17bc23e88a04d8d6992f526b79e258f))

# [2.0.0](https://github.com/Daniele-Tentoni/java-version-action/compare/1.0.2...2.0.0) (2021-12-30)


### Bug Fixes

* add test_dir_name local var. ([b066642](https://github.com/Daniele-Tentoni/java-version-action/commit/b0666427ac5877e86142e04357ee555cf3e9d06b))
* codacy multiline docstrings. ([b3c2dc0](https://github.com/Daniele-Tentoni/java-version-action/commit/b3c2dc0beb1e9bf50a7e7aa036e20ba1d8009720))
* codacy multilines python docstring. ([4bc91e6](https://github.com/Daniele-Tentoni/java-version-action/commit/4bc91e61941e0d1b5bb36695744b5c25ad167137))
* correct the path of main script. ([e1bacd9](https://github.com/Daniele-Tentoni/java-version-action/commit/e1bacd98e294cec9d7061591345a1aed58336259))
* define explicitly utils imported. ([a12100d](https://github.com/Daniele-Tentoni/java-version-action/commit/a12100d40ccabf32e75026ced0f39e87ddb763f1))
* install action in main dir. ([d810aa2](https://github.com/Daniele-Tentoni/java-version-action/commit/d810aa25dd3d864554c909f84a4c539aac65bf7e))
* move codacy report to pull_request_target workflow. ([de613a3](https://github.com/Daniele-Tentoni/java-version-action/commit/de613a37319a8e0ff82793f4039e556ef48a669d))
* right check set variables. ([8e1bbd7](https://github.com/Daniele-Tentoni/java-version-action/commit/8e1bbd7032f08c3576c715dc75365489153d654d))
* use camel-case repo ref. ([26797d6](https://github.com/Daniele-Tentoni/java-version-action/commit/26797d68539f0ad47933c3882d1ebc3aec36f644))
* use correct folder for executables. ([655abe9](https://github.com/Daniele-Tentoni/java-version-action/commit/655abe9d4cf89e61f80ad3b07b92519e477b9af7))
* use suggested name for secret. ([8394150](https://github.com/Daniele-Tentoni/java-version-action/commit/839415024f31817acca749809bae028bab79478c))
* use the correct script. ([346da16](https://github.com/Daniele-Tentoni/java-version-action/commit/346da163a3fe3c4140c6b57aae202fc3f881ffb3))
* W0622 redefined buildint type. ([e62dcd6](https://github.com/Daniele-Tentoni/java-version-action/commit/e62dcd60a2b921a33c36b59a0b3b2ead4ad4face))


### Features

* clean script remove tmp folder too. ([4a98d17](https://github.com/Daniele-Tentoni/java-version-action/commit/4a98d17e215e3cf4277be76fcd7a18cd062cd73a))
* New main dir runner. ([8830193](https://github.com/Daniele-Tentoni/java-version-action/commit/883019361ebfe0d9f4ec619ec7247950a22ae429))
* refactor the code in test and script. ([d068def](https://github.com/Daniele-Tentoni/java-version-action/commit/d068def8637e4274de58dcb412f275df9cc6a677))
* versioner package runnable. ([3e3eeb5](https://github.com/Daniele-Tentoni/java-version-action/commit/3e3eeb5f80c337109b69c1e24e2aab8694218492))


### Performance Improvements

* new versioner package. ([c045bb2](https://github.com/Daniele-Tentoni/java-version-action/commit/c045bb2e44e2e983687a7bcc48851511b2b8e70f))


### BREAKING CHANGES

* Now the action have inside a versioner package with all business logic inside. Refer to that in your code.

## [1.0.2](https://github.com/Daniele-Tentoni/java-version-action/compare/1.0.1...1.0.2) (2021-12-22)


### Bug Fixes

* add a beatiful badge to README. ([f0e19d2](https://github.com/Daniele-Tentoni/java-version-action/commit/f0e19d29d2d72d7d63e0468cd22940e8bebe651e))
* add a new .gitignore ([0dde03e](https://github.com/Daniele-Tentoni/java-version-action/commit/0dde03e501378e52e7c6bb0c51248e56410e66e8))
* ignore node modules folder. ([1d57bb6](https://github.com/Daniele-Tentoni/java-version-action/commit/1d57bb65afa0d70397abd8be66145edeb39c6733))
* install node packages. ([11e0ee0](https://github.com/Daniele-Tentoni/java-version-action/commit/11e0ee0b3288362c762f7d8be3a7777732d01022))
* missed to checkout the repo -_- ([324ed82](https://github.com/Daniele-Tentoni/java-version-action/commit/324ed820cd292e0e1fdf178662c508599146a271))
* move codacy report to pull_request_target workflow. ([ba52c08](https://github.com/Daniele-Tentoni/java-version-action/commit/ba52c08a8b36d7771adbe00164b4ce3d9588cb3d))
* move wrapper versioning to another function ([66d9f6e](https://github.com/Daniele-Tentoni/java-version-action/commit/66d9f6e39ca4514a20d6d7d11eea812d107644c4))
* multiline docstring start in new line. ([e4fa3b5](https://github.com/Daniele-Tentoni/java-version-action/commit/e4fa3b520d8f98acced60a6da3c4149052eb6939))
* remove committed ignored file. ([e10fc10](https://github.com/Daniele-Tentoni/java-version-action/commit/e10fc10659172ef70ce42556ff5315caf5ae5127))
* remove trailing whitespace. ([177b16c](https://github.com/Daniele-Tentoni/java-version-action/commit/177b16cc23a521240f77a524ce62473252f41b30))
* remove trailing whitespaces. ([75cf0b4](https://github.com/Daniele-Tentoni/java-version-action/commit/75cf0b402955c055e703b7ad2d448d3dab1be22f))
* right check set variables. ([e587330](https://github.com/Daniele-Tentoni/java-version-action/commit/e5873301aeea19edfebbce3bf9ca7b8a10faddb4))
* use suggested name for secret. ([c2a6cfa](https://github.com/Daniele-Tentoni/java-version-action/commit/c2a6cfa1ef94c4b3ce5621f8871c45710d7bf322))

## [1.0.1](https://github.com/Daniele-Tentoni/java-version-action/compare/1.0.0...1.0.1) (2021-12-18)


### Bug Fixes

* add gnupl ([e9920d1](https://github.com/Daniele-Tentoni/java-version-action/commit/e9920d1bb4012bc3a88c66598ecb85b19d9741ad))

# 1.0.0 (2021-12-17)


### Bug Fixes

* add a beatiful badge to README. ([b150451](https://github.com/Daniele-Tentoni/java-version-action/commit/b150451e88d749f3634fa3e59073f7fae9de2c61))
* add a new .gitignore ([a7d5ca4](https://github.com/Daniele-Tentoni/java-version-action/commit/a7d5ca4355dfe37395eef68a92447bb29cff1c56))
* add more complex script for windows runner. ([e9d63c6](https://github.com/Daniele-Tentoni/java-version-action/commit/e9d63c6eb902ef282eda0917fde47b5194fe334b))
* add semantic release github token to secrets. ([0348073](https://github.com/Daniele-Tentoni/java-version-action/commit/034807343ff33e52b9972e1fc3fe89195f4c9bf4))
* add the right extension to reusable workflow. ([ee85313](https://github.com/Daniele-Tentoni/java-version-action/commit/ee853134526325638c828966a4570c9c4654ac73))
* create .gitignore file. ([c68895c](https://github.com/Daniele-Tentoni/java-version-action/commit/c68895ce8b6437ff7cbd8f9d17001d03db1c72c2))
* fix workflow ticks. ([2f17f17](https://github.com/Daniele-Tentoni/java-version-action/commit/2f17f1717511173446e4838e714a0fa63ee8ef47))
* install dep in the right place. ([d641a1c](https://github.com/Daniele-Tentoni/java-version-action/commit/d641a1c6aaedddeb212444a1f7d11cb227be3130))
* install dependancies before running. ([f651d47](https://github.com/Daniele-Tentoni/java-version-action/commit/f651d47c3fbc9a78d065b8c7059279e8df9053a2))
* install dependancies in test workflow. ([5af8aa4](https://github.com/Daniele-Tentoni/java-version-action/commit/5af8aa4b6d3cbe4fbb42affc35fc5876dc3c68d8))
* install python. ([ed54f95](https://github.com/Daniele-Tentoni/java-version-action/commit/ed54f956ba16085db12b876b31d48b1e89687ca1))
* missing then ([beaf2a4](https://github.com/Daniele-Tentoni/java-version-action/commit/beaf2a4b526ed657c2307d30b408b9742719a8a5))
* missing then ([c193ab8](https://github.com/Daniele-Tentoni/java-version-action/commit/c193ab813fc44e366d5bb73869faee2f86373c1f))
* remove a 'magic string' ([f96d722](https://github.com/Daniele-Tentoni/java-version-action/commit/f96d7221c2018aab5da12a9a43146c59f2877d02))
* remove committed ignored file. ([59e6d93](https://github.com/Daniele-Tentoni/java-version-action/commit/59e6d9327ff485ed68d900f12d20b4bda076fc18))
* remove dependabot ([b3cf549](https://github.com/Daniele-Tentoni/java-version-action/commit/b3cf5493e8dc71299a4c83a418b94e95f27aeece))
* remove deprecated python version. ([4c95bf0](https://github.com/Daniele-Tentoni/java-version-action/commit/4c95bf0b3855151f5df5a95eb86139a9ad398932))
* remove main reference in test command. ([ffd13d4](https://github.com/Daniele-Tentoni/java-version-action/commit/ffd13d49a41de5b2d089860c20ce239056345351))
* remove trailing white space ([35371bd](https://github.com/Daniele-Tentoni/java-version-action/commit/35371bd62cc63979294cd6bfb4942678022a2047))
* rename test script workflow ([f4f4436](https://github.com/Daniele-Tentoni/java-version-action/commit/f4f44362d753353a8534f373f8e5db15256e87ae))
* run command correctly inside a bash. ([6fc5886](https://github.com/Daniele-Tentoni/java-version-action/commit/6fc588681e6984ef13aa267e319a309ce09c747c))
* run python3 interpreter instead only on python. ([6277d72](https://github.com/Daniele-Tentoni/java-version-action/commit/6277d726f2257301233fe92d0c00edca96304ab5))
* try another type of output results. ([b9bc1c5](https://github.com/Daniele-Tentoni/java-version-action/commit/b9bc1c5bcba91aa3312e6108fc2de6a8c2118efd))
* try to output correct result by runner.os ([e98982e](https://github.com/Daniele-Tentoni/java-version-action/commit/e98982e789f8a1572fbab6dd707cf647b9db8fe0))
* try to output correct result by runner.os ([35be9e5](https://github.com/Daniele-Tentoni/java-version-action/commit/35be9e52d3315e7b3781ca75bff4cc113d4b7519))
* update test action to match real properties. ([c15ab08](https://github.com/Daniele-Tentoni/java-version-action/commit/c15ab0858aaeeb564a7517821635b8c04a1ef84e))
* use -eq operator. ([08b1bf0](https://github.com/Daniele-Tentoni/java-version-action/commit/08b1bf0954b61a85e6c6618f46484f3e51863f38))
* use github reference in renovate config ([2f8e2c6](https://github.com/Daniele-Tentoni/java-version-action/commit/2f8e2c6400cf8912aa436c174b9e6e7aed39c01d))
* use prepopulated github token. ([2fffe7b](https://github.com/Daniele-Tentoni/java-version-action/commit/2fffe7b8b9de82cb60b7272ec44aced6dca0fce7))


### Features

* add release branch. ([6bea526](https://github.com/Daniele-Tentoni/java-version-action/commit/6bea5263adad848c877b8ecd14aa47932a8c9335))
* add renovate configuration. ([bb96e3d](https://github.com/Daniele-Tentoni/java-version-action/commit/bb96e3da3dd5f4e1df5d52caabad8af7093a7d18))
* create action file. ([0626a75](https://github.com/Daniele-Tentoni/java-version-action/commit/0626a75f772071aae9512ca46357bd9355e6b448))
* create test action workflow. ([f0d10f1](https://github.com/Daniele-Tentoni/java-version-action/commit/f0d10f158d7eb25830e2c510efbe9ce784945f5a))
* make tests more powerful. ([84a3c7f](https://github.com/Daniele-Tentoni/java-version-action/commit/84a3c7f0765b652eece41b78b0151058990e184d))
* make the main script runnable. ([b7d5f2d](https://github.com/Daniele-Tentoni/java-version-action/commit/b7d5f2d1689229db8b1d4a22a283bbd97d9562fb))
* separate release from tests workflows. ([9b93de9](https://github.com/Daniele-Tentoni/java-version-action/commit/9b93de9ec838cd64fb2b6a3fbd2246c72ad38e31))
* use my new renovate config repo. ([b006a04](https://github.com/Daniele-Tentoni/java-version-action/commit/b006a0455ce1d792993b691333cefaac92367a0d))
