USE [zurich_db]
GO  

/****** Object:  Table [dbo].[CLOUD]    Script Date: 03/07/2025 05:40:38 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CLOUD](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[ID_EMPLEADO] [float] NULL,
	[ESTADO] [nvarchar](255) NULL,
	[USUARIO] [nvarchar](255) NULL,
	[CONTRASENA] [nvarchar](255) NULL,
	[ACCESO] [nvarchar](255) NULL,
	[ADICIONALES] [nvarchar](255) NULL,
	[CARPETA_PERSONAL] [nvarchar](255) NULL,
	[PERMISOS] [nvarchar](255) NULL,
	[CARPETA1] [nvarchar](255) NULL,
	[PERMISO1] [nvarchar](255) NULL,
	[CARPETA2] [nvarchar](255) NULL,
	[PERMISO2] [nvarchar](255) NULL,
	[CARPETA3] [nvarchar](255) NULL,
	[PERMISO3] [nvarchar](255) NULL,
	[CARPETA4] [nvarchar](255) NULL,
	[PERMISO4] [nvarchar](255) NULL,
	[CARPETA5] [nvarchar](255) NULL,
	[PERMISO5] [nvarchar](255) NULL,
	[CARPETA6] [nvarchar](255) NULL,
	[PERMISO6] [nvarchar](255) NULL,
	[CARPETA7] [nvarchar](255) NULL,
	[PERMISO7] [nvarchar](255) NULL,
	[CARPETA8] [nvarchar](255) NULL,
	[PERMISO8] [nvarchar](255) NULL,
	[CARPETA9] [nvarchar](255) NULL,
	[PERMISO9] [nvarchar](255) NULL,
	[CARPETA10] [nvarchar](255) NULL,
	[PERMISO10] [nvarchar](255) NULL,
	[SUBCARPETA1] [nvarchar](255) NULL,
	[PERMISO11] [nvarchar](255) NULL,
	[SUBCARPETA2] [nvarchar](255) NULL,
	[PERMISO12] [nvarchar](255) NULL,
	[SUBCARPETA3] [nvarchar](255) NULL,
	[PERMISO13] [nvarchar](255) NULL,
	[SUBCARPETA4] [nvarchar](255) NULL,
	[PERMISO14] [nvarchar](255) NULL,
	[SUBCARPETA5] [nvarchar](255) NULL,
	[PERMISO15] [nvarchar](255) NULL,
	[SUBCARPETA6] [nvarchar](255) NULL,
	[PERMISO16] [nvarchar](255) NULL,
	[SUBCARPETA7] [nvarchar](255) NULL,
	[PERMISO17] [nvarchar](255) NULL,
	[SUBCARPETA8] [nvarchar](255) NULL,
	[PERMISO18] [nvarchar](255) NULL,
	[SUBCARPETA9] [nvarchar](255) NULL,
	[PERMISO19] [nvarchar](255) NULL,
	[SUBCARPETA10] [nvarchar](255) NULL,
	[PERMISO20] [nvarchar](255) NULL,
	[OBSERVACIONES] [nvarchar](255) NULL,
 CONSTRAINT [CLOUD$ID] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO