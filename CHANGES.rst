0.2.0 (unreleased)
------------------

- Add support for serialization and deserialization of input_units_equivalencies
  for astropy models. [#37]
- Bugfix for units_mapping schema's property name conflicts. Changes:
  - ``inputs`` to ``unit_inputs``
  - ``outputs`` to ``unit_outputs``

0.1.2 (2021-12-14)
------------------

- Fix bug in Table deserializer when meta is absent from the ASDF. [#36]

0.1.1 (2021-12-04)
------------------

- Retrieve coordinates schemas from asdf-coordinates-schemas. [#35]

0.1.0 (2021-12-01)
------------------

- Initial release.
