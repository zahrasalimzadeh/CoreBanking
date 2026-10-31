USE [master]
GO
/****** Object:  Database [CoreBanking0606]    Script Date: 10/28/2026 12:41:36 AM ******/
CREATE DATABASE [CoreBanking0606]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'CoreBanking0606', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL17.MSSQLSERVER\MSSQL\DATA\CoreBanking0606.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'CoreBanking0606_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL17.MSSQLSERVER\MSSQL\DATA\CoreBanking0606_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [CoreBanking0606] SET COMPATIBILITY_LEVEL = 170
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [CoreBanking0606].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [CoreBanking0606] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [CoreBanking0606] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [CoreBanking0606] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [CoreBanking0606] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [CoreBanking0606] SET ARITHABORT OFF 
GO
ALTER DATABASE [CoreBanking0606] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [CoreBanking0606] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [CoreBanking0606] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [CoreBanking0606] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [CoreBanking0606] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [CoreBanking0606] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [CoreBanking0606] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [CoreBanking0606] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [CoreBanking0606] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [CoreBanking0606] SET  DISABLE_BROKER 
GO
ALTER DATABASE [CoreBanking0606] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [CoreBanking0606] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [CoreBanking0606] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [CoreBanking0606] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [CoreBanking0606] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [CoreBanking0606] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [CoreBanking0606] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [CoreBanking0606] SET RECOVERY FULL 
GO
ALTER DATABASE [CoreBanking0606] SET  MULTI_USER 
GO
ALTER DATABASE [CoreBanking0606] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [CoreBanking0606] SET DB_CHAINING OFF 
GO
ALTER DATABASE [CoreBanking0606] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [CoreBanking0606] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [CoreBanking0606] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [CoreBanking0606] SET OPTIMIZED_LOCKING = OFF 
GO
ALTER DATABASE [CoreBanking0606] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'CoreBanking0606', N'ON'
GO
ALTER DATABASE [CoreBanking0606] SET QUERY_STORE = ON
GO
ALTER DATABASE [CoreBanking0606] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [CoreBanking0606]
GO
/****** Object:  Table [dbo].[employee]    Script Date: 10/28/2026 12:41:38 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[employee](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[first_name] [varchar](50) NOT NULL,
	[last_name] [varchar](50) NOT NULL,
	[mobile] [varchar](11) NOT NULL,
	[user_name] [varchar](50) NOT NULL,
	[password] [varchar](50) NOT NULL,
	[employee_status_id] [smallint] NOT NULL,
	[role_id] [smallint] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[employee_status]    Script Date: 10/28/2026 12:41:39 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[employee_status](
	[id] [smallint] IDENTITY(1,1) NOT NULL,
	[title] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[performance_logger]    Script Date: 10/28/2026 12:41:39 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[performance_logger](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[function_name] [varchar](100) NOT NULL,
	[execution_time] [decimal](18, 10) NOT NULL,
	[call_date_time] [datetime] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[employee] ON 

INSERT [dbo].[employee] ([id], [first_name], [last_name], [mobile], [user_name], [password], [employee_status_id], [role_id]) VALUES (1, N'zahra', N'salimzadeh', N'09100973427', N'z.salimzadeh', N'e10adc3949ba59abbe56e057f20f883e', 2, 1)
SET IDENTITY_INSERT [dbo].[employee] OFF
GO
SET IDENTITY_INSERT [dbo].[employee_status] ON 

INSERT [dbo].[employee_status] ([id], [title]) VALUES (1, N'Pending')
INSERT [dbo].[employee_status] ([id], [title]) VALUES (2, N'Active')
INSERT [dbo].[employee_status] ([id], [title]) VALUES (3, N'Deactive')
SET IDENTITY_INSERT [dbo].[employee_status] OFF
GO
SET IDENTITY_INSERT [dbo].[performance_logger] ON 

INSERT [dbo].[performance_logger] ([id], [function_name], [execution_time], [call_date_time]) VALUES (1, N'get_by_username_password', CAST(0.2002375126 AS Decimal(18, 10)), CAST(N'2026-10-27T15:50:45.353' AS DateTime))
INSERT [dbo].[performance_logger] ([id], [function_name], [execution_time], [call_date_time]) VALUES (2, N'login_button_clicked', CAST(6.1526069641 AS Decimal(18, 10)), CAST(N'2026-10-27T15:50:51.307' AS DateTime))
INSERT [dbo].[performance_logger] ([id], [function_name], [execution_time], [call_date_time]) VALUES (3, N'get_by_username_password', CAST(0.1266455650 AS Decimal(18, 10)), CAST(N'2026-10-27T19:11:27.237' AS DateTime))
INSERT [dbo].[performance_logger] ([id], [function_name], [execution_time], [call_date_time]) VALUES (4, N'login_button_clicked', CAST(1.4684965611 AS Decimal(18, 10)), CAST(N'2026-10-27T19:11:28.563' AS DateTime))
SET IDENTITY_INSERT [dbo].[performance_logger] OFF
GO
ALTER TABLE [dbo].[employee] ADD  CONSTRAINT [DF_employee_role]  DEFAULT ((1)) FOR [role_id]
GO
ALTER TABLE [dbo].[employee]  WITH CHECK ADD FOREIGN KEY([employee_status_id])
REFERENCES [dbo].[employee_status] ([id])
GO
USE [master]
GO
ALTER DATABASE [CoreBanking0606] SET  READ_WRITE 
GO
