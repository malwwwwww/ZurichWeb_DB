USE [zurich_db]
GO

/****** Object:  Table [dbo].[NO_BREAKS]    Script Date: 24/07/2025 02:11:34 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[NO_BREAKS](
	[ID_BREAK] [varchar](10) NOT NULL,
	[ESTADO] [varchar](20) NOT NULL,
	[RAZON_SOCIAL] [varchar](100) NOT NULL,
	[MARCA] [varchar](50) NULL,
	[MODELO] [varchar](50) NULL,
	[NUM_SERIE] [varchar](50) NULL,
	[OBSERVATIONS] [text] NULL,
	[DOCUMENTOS] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[ID_BREAK] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO


