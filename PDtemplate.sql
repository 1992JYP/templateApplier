/**  <Ctrl + Shift + M> 을 사용하세요 **/
/** 쿼리 -> 템플릿매개변수값지정 매뉴를 사용하세요 **/

USE [<UseDatabase,,COMM>]
GO

IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = OBJECT_ID(N'[<Procedure_Owner,,dbo>].[<Procedure_Name,sysname,ProcedureName>]') AND OBJECTPROPERTY(ID, N'ISPROCEDURE') = 1)
DROP PROCEDURE <Procedure_Owner,,dbo>.[<Procedure_Name,sysname,ProcedureName>]
GO

SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

/******************************************************************************************
파일명 : <Procedure_Owner,,dbo>.<Procedure_Name,sysname,ProcedureName>.StoredProcedure.sql

<Create_Date,,> <Author,,Name> : <Description,,>

******************************************************************************************/
--<UseDatabase,,COMM>.<Procedure_Owner,,dbo>.<Procedure_Name,sysname,ProcedureName>
CREATE    PROC [<Procedure_Owner,,dbo>].[<Procedure_Name,sysname,ProcedureName>]
				 @CURR_DATE		DATE
				
AS
   
    SET NOCOUNT ON

	SELECT 'EDIT'
	
	
	
GO
