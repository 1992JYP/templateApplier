/**  <Ctrl + Shift + M> 을 사용하세요 **/
/** 쿼리 -> 템플릿매개변수값지정 매뉴를 사용하세요 **/

USE [A]
GO

IF EXISTS (SELECT * FROM DBO.SYSOBJECTS WHERE ID = OBJECT_ID(N'[SD].[DSAFDAS]') AND OBJECTPROPERTY(ID, N'ISPROCEDURE') = 1)
DROP PROCEDURE SD.[DSAFDAS]
GO

SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

/******************************************************************************************
파일명 : SD.DSAFDAS.StoredProcedure.sql

DSHASDh ASHASHd : ASHAHADS

******************************************************************************************/
--A.SD.DSAFDAS
CREATE    PROC [SD].[DSAFDAS]
				 @CURR_DATE		DATE
				
AS
   
    SET NOCOUNT ON

	SELECT 'EDIT'
	
	
	
GO
