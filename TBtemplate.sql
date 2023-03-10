/*****************************************************/
/** <Ctrl + Shift + M> : 템플릿매개변수값지정 사용	**/
/*****************************************************/
USE [<UseDatabase,,RCV_KOSCOM>]
GO

/****** Object:  Table [dbo].[<Table_Name,,TableName>]    Script Date: 2021-09-08 오후 1:55:29 ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[<Table_Name,,TableName>]') AND type in (N'U'))
DROP TABLE [dbo].[<Table_Name,,TableName>]
GO
/****** Object:  Table [dbo].[<Table_Name,,TableName>]    Script Date: 2021-09-08 오후 1:55:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

/****** FileName : dbo.<Table_Name,,TableName>.Table.sql ******/
CREATE TABLE [dbo].[<Table_Name,,TableName>](
	[STD_DATE] [date] NOT NULL,
	[FILE_ID] [char](36) NOT NULL,
	[FILE_CD] [int] NOT NULL,



	[INS_ID] [varchar](20) NULL,
	[INS_IP] [varchar](15) NULL,
	[INS_DTM] [datetime] NULL,
 CONSTRAINT [PK_<Table_Name,,TableName>] PRIMARY KEY CLUSTERED 
(
	[STD_DATE] ASC,
	[FILE_ID] ASC,
	[FILE_CD] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'<Table_Desc,,TableDesc>' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'<Table_Name,,TableName>'
GO
