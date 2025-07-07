# ¡LEEME!

QExports es una carpeta donde se exportan los archivos QTF de QPAD.
Generalmente un QTF se estructura asi:



<QTF>

\[Doc] \* Indicador de Documento

  \[Meta] \* Sección Meta

    Font=Arial \* Fuente del documento

    Size=12p \* Tamaño del documento

  \[/Meta] \* Cierre de Meta

  \[Body] \* Cuerpo del documento

    \[P align=center] \* Alineacion

      <bold>Bienvenido a QPad</bold> \* <bold> es referente a **NEGRITA**

    \[/P]

    \[P]

      <italic>Este es un ejemplo</italic> de <underline>documento</underline> en <strikeout>QTF</strikeout>.

    \[/P]

    \[List type=ul]

      \[Item]<def>Elemento uno</Item>

      \[Item]<def>Elemento dos</Item

    \[/List] 

    \[Table]

      \[Row]

        \[Cell header]<def>Nombre</Cell>

        \[Cell header]<def>Edad</Cell>

      \[/Row]

      \[Row]

        \[Cell]<def>Juan</Cell>

        \[Cell]<def>30</Cell>

      \[/Row]

    \[/Table]

  \[/Body]

\[/Doc]
</QTF>

