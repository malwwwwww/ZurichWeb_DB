USE [zurich_db]
GO

/****** Object:  Table [dbo].[TARJETAS]    Script Date: 03/07/2025 05:40:38 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[TARJETAS](
    [ID_TARJETA] [nvarchar](255) NOT NULL,
    [ID_EMPLEADO] [int] NOT NULL,
    [FECHA_ACT] [datetime2](0) NULL,
    [FECHA_BAJA] [datetime2](0) NULL,
    [OBSERVACIONES] [nvarchar](max) NULL,
    [CLAVE] [int] NULL,
    [ESTADO] [nvarchar](255) NULL,
    [SSMA_TimeStamp] [timestamp] NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO