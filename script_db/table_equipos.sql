USE [zurich_db]
GO

/****** Object:  Table [dbo].[EQUIPOS]    Script Date: 24/07/2025 02:10:16 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[EQUIPOS](
	[ID_EQUIPO] [varchar](10) NOT NULL,
	[ESTADO] [varchar](20) NOT NULL,
	[RAZON_SOCIAL] [varchar](100) NOT NULL,
	[UBICACION] [varchar](100) NULL,
	[TIPO_EQUIPO] [varchar](50) NULL,
	[SITUACION] [varchar](50) NULL,
	[PROVEEDOR] [varchar](100) NULL,
	[MARCA] [varchar](50) NULL,
	[MODELO] [varchar](50) NULL,
	[SERIE] [varchar](50) NULL,
	[LINEA_TEL] [varchar](20) NULL,
	[IMEI] [varchar](20) NULL,
	[COMPANIA] [varchar](50) NULL,
	[PROCESADOR] [varchar](50) NULL,
	[RAM_1] [varchar](20) NULL,
	[RAM_2] [varchar](20) NULL,
	[DISCO_1] [varchar](20) NULL,
	[DISCO_2] [varchar](20) NULL,
	[SISTEMA_OPERATIVO] [varchar](50) NULL,
	[OBSERVATIONS] [text] NULL,
	[MAC_WIFI1] [varchar](17) NULL,
	[MAC_WIFI2] [varchar](17) NULL,
	[MAC_ETHERNET1] [varchar](17) NULL,
	[MAC_ETHERNET2] [varchar](17) NULL,
	[DEPARTAMENTO_ASIGNADO] [varchar](50) NULL,
	[FECHA_ALTA] [datetime] NULL,
	[FOTO] [varchar](255) NULL,
	[DOCUMENTOS] [varchar](255) NULL,
	[ANTIVIRUS] [varchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[ID_EQUIPO] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO


