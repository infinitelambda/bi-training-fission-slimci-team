{% macro drop_schema(schema=var('CI_SCHEMA')) %}

  {{ log('Statement to run:', info=True) }}

  {% set drop_command -%}
    drop schema if exists {{ target.database }}.{{ schema }};
  {%- endset %}

  {% do log(drop_command, info=True) %}
  {% do run_query(drop_command) %}

  {{ log('Schema dropped successfully', info=True) }}

{% endmacro %}
