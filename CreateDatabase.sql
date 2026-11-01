IF DB_ID(N'CoreBanking0606') IS NULL
    CREATE DATABASE [CoreBanking0606]
GO
USE [CoreBanking0606]
GO

/****** Object:  Table [dbo].[account]    Script Date: 11/1/2026 7:24:53 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[account](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[account_number] [varchar](20) NOT NULL,
	[opening_date] [date] NOT NULL,
	[customer_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

SET QUOTED_IDENTIFIER ON
GO

/****** Object:  Table [dbo].[customer]    Script Date: 11/1/2026 7:24:54 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[customer](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[first_name] [nvarchar](50) NOT NULL,
	[last_name] [nvarchar](50) NOT NULL,
	[mobile] [varchar](15) NOT NULL,
	[password] [varchar](32) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

/****** Object:  Table [dbo].[employee]    Script Date: 11/1/2026 7:24:54 PM ******/
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

/****** Object:  Table [dbo].[employee_status]    Script Date: 11/1/2026 7:24:54 PM ******/
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

/****** Object:  Table [dbo].[otp]    Script Date: 11/1/2026 7:24:54 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[otp](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[phone] [varchar](15) NOT NULL,
	[code] [varchar](6) NOT NULL,
	[created_at] [datetime] NOT NULL,
	[expires_at] [datetime] NOT NULL,
	[is_used] [bit] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

/****** Object:  Table [dbo].[performance_logger]    Script Date: 11/1/2026 7:24:54 PM ******/
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

/****** Object:  Table [dbo].[transaction_type]    Script Date: 11/1/2026 7:24:54 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[transaction_type](
	[id] [smallint] NOT NULL,
	[title] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

/****** Object:  Table [dbo].[transactions]    Script Date: 11/1/2026 7:24:54 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[transactions](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[account_id] [int] NOT NULL,
	[amount] [numeric](18, 2) NOT NULL,
	[transaction_type_id] [smallint] NOT NULL,
	[created_at] [datetime] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

SET IDENTITY_INSERT [dbo].[account] ON 

INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (1, N'6037000001', CAST(N'2026-10-16' AS Date), 1)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (2, N'6037000002', CAST(N'2026-10-03' AS Date), 2)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (3, N'6037000003', CAST(N'2026-09-20' AS Date), 3)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (4, N'6037000004', CAST(N'2026-09-07' AS Date), 4)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (5, N'6037000005', CAST(N'2026-08-25' AS Date), 5)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (6, N'6037000006', CAST(N'2026-08-12' AS Date), 6)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (7, N'6037000007', CAST(N'2026-07-30' AS Date), 7)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (8, N'6037000008', CAST(N'2026-07-17' AS Date), 8)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (9, N'6037000009', CAST(N'2026-07-04' AS Date), 9)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (10, N'6037000010', CAST(N'2026-06-21' AS Date), 10)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (11, N'6037000011', CAST(N'2026-06-08' AS Date), 11)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (12, N'6037000012', CAST(N'2026-05-26' AS Date), 12)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (13, N'6037000013', CAST(N'2026-05-13' AS Date), 13)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (14, N'6037000014', CAST(N'2026-04-30' AS Date), 14)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (15, N'6037000015', CAST(N'2026-04-17' AS Date), 15)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (16, N'6037000016', CAST(N'2026-04-04' AS Date), 16)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (17, N'6037000017', CAST(N'2026-03-22' AS Date), 17)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (18, N'6037000018', CAST(N'2026-03-09' AS Date), 18)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (19, N'6037000019', CAST(N'2026-02-24' AS Date), 19)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (20, N'6037000020', CAST(N'2026-02-11' AS Date), 20)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (21, N'6037000021', CAST(N'2026-01-29' AS Date), 21)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (22, N'6037000022', CAST(N'2026-01-16' AS Date), 22)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (23, N'6037000023', CAST(N'2026-01-03' AS Date), 23)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (24, N'6037000024', CAST(N'2025-12-21' AS Date), 24)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (25, N'6037000025', CAST(N'2025-12-08' AS Date), 25)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (26, N'6037000026', CAST(N'2025-11-25' AS Date), 26)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (27, N'6037000027', CAST(N'2025-11-12' AS Date), 27)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (28, N'6037000028', CAST(N'2025-10-30' AS Date), 28)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (29, N'6037000029', CAST(N'2025-10-17' AS Date), 29)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (30, N'6037000030', CAST(N'2025-10-04' AS Date), 30)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (32, N'1000000001', CAST(N'2026-11-01' AS Date), 2)
INSERT [dbo].[account] ([id], [account_number], [opening_date], [customer_id]) VALUES (33, N'1000000002', CAST(N'2026-11-01' AS Date), 13)
SET IDENTITY_INSERT [dbo].[account] OFF
GO

SET IDENTITY_INSERT [dbo].[customer] ON 

INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (1, N'Ali', N'Ahmadi', N'09120000001', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (2, N'Sara', N'Ahmadi', N'09120000002', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (3, N'Reza', N'Ahmadi', N'09120000003', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (4, N'Maryam', N'Ahmadi', N'09120000004', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (5, N'Hassan', N'Ahmadi', N'09120000005', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (6, N'Neda', N'Ahmadi', N'09120000006', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (7, N'Ali', N'Karimi', N'09120000007', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (8, N'Sara', N'Karimi', N'09120000008', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (9, N'Reza', N'Karimi', N'09120000009', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (10, N'Maryam', N'Karimi', N'09120000010', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (11, N'Hassan', N'Karimi', N'09120000011', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (12, N'Neda', N'Karimi', N'09120000012', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (13, N'Ali', N'Rezaei', N'09120000013', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (14, N'Sara', N'Rezaei', N'09120000014', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (15, N'Reza', N'Rezaei', N'09120000015', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (16, N'Maryam', N'Rezaei', N'09120000016', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (17, N'Hassan', N'Rezaei', N'09120000017', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (18, N'Neda', N'Rezaei', N'09120000018', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (19, N'Ali', N'Hosseini', N'09120000019', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (20, N'Sara', N'Hosseini', N'09120000020', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (21, N'Reza', N'Hosseini', N'09120000021', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (22, N'Maryam', N'Hosseini', N'09120000022', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (23, N'Hassan', N'Hosseini', N'09120000023', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (24, N'Neda', N'Hosseini', N'09120000024', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (25, N'Ali', N'Moradi', N'09120000025', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (26, N'Sara', N'Moradi', N'09120000026', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (27, N'Reza', N'Moradi', N'09120000027', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (28, N'Maryam', N'Moradi', N'09120000028', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (29, N'Hassan', N'Moradi', N'09120000029', N'e10adc3949ba59abbe56e057f20f883e')
INSERT [dbo].[customer] ([id], [first_name], [last_name], [mobile], [password]) VALUES (30, N'Neda', N'Moradi', N'09120000030', N'e10adc3949ba59abbe56e057f20f883e')
SET IDENTITY_INSERT [dbo].[customer] OFF
GO

SET IDENTITY_INSERT [dbo].[employee] ON 

INSERT [dbo].[employee] ([id], [first_name], [last_name], [mobile], [user_name], [password], [employee_status_id], [role_id]) VALUES (1, N'zahra', N'salimzadeh', N'09120000000', N'z.salimzadeh', N'e10adc3949ba59abbe56e057f20f883e', 2, 2)
SET IDENTITY_INSERT [dbo].[employee] OFF
GO

SET IDENTITY_INSERT [dbo].[employee_status] ON 

INSERT [dbo].[employee_status] ([id], [title]) VALUES (1, N'Pending')
INSERT [dbo].[employee_status] ([id], [title]) VALUES (2, N'Active')
INSERT [dbo].[employee_status] ([id], [title]) VALUES (3, N'Deactive')
SET IDENTITY_INSERT [dbo].[employee_status] OFF
GO

INSERT [dbo].[transaction_type] ([id], [title]) VALUES (1, N'Deposit')
INSERT [dbo].[transaction_type] ([id], [title]) VALUES (2, N'Withdraw')
GO

SET IDENTITY_INSERT [dbo].[transactions] ON 

INSERT [dbo].[transactions] ([id], [account_id], [amount], [transaction_type_id], [created_at]) VALUES (1, 32, CAST(5000000.00 AS Numeric(18, 2)), 1, CAST(N'2026-11-01T11:51:56.070' AS DateTime))
INSERT [dbo].[transactions] ([id], [account_id], [amount], [transaction_type_id], [created_at]) VALUES (2, 32, CAST(1500000.00 AS Numeric(18, 2)), 2, CAST(N'2026-11-01T11:51:56.070' AS DateTime))
INSERT [dbo].[transactions] ([id], [account_id], [amount], [transaction_type_id], [created_at]) VALUES (3, 32, CAST(2000000.00 AS Numeric(18, 2)), 1, CAST(N'2026-11-01T11:51:56.070' AS DateTime))
INSERT [dbo].[transactions] ([id], [account_id], [amount], [transaction_type_id], [created_at]) VALUES (4, 33, CAST(700000.00 AS Numeric(18, 2)), 1, CAST(N'2026-11-01T11:51:56.127' AS DateTime))
SET IDENTITY_INSERT [dbo].[transactions] OFF
GO

SET ANSI_PADDING ON
GO

/****** Object:  Index [UQ__account__AF91A6ADC86C4B94]    Script Date: 11/1/2026 7:24:54 PM ******/
ALTER TABLE [dbo].[account] ADD UNIQUE NONCLUSTERED 
(
	[account_number] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO

ALTER TABLE [dbo].[employee] ADD  CONSTRAINT [DF_employee_role]  DEFAULT ((1)) FOR [role_id]
GO

ALTER TABLE [dbo].[transactions] ADD  DEFAULT (getdate()) FOR [created_at]
GO

ALTER TABLE [dbo].[account]  WITH CHECK ADD FOREIGN KEY([customer_id])
REFERENCES [dbo].[customer] ([id])
GO

ALTER TABLE [dbo].[employee]  WITH CHECK ADD FOREIGN KEY([employee_status_id])
REFERENCES [dbo].[employee_status] ([id])
GO

ALTER TABLE [dbo].[transactions]  WITH CHECK ADD FOREIGN KEY([account_id])
REFERENCES [dbo].[account] ([id])
GO

ALTER TABLE [dbo].[transactions]  WITH CHECK ADD FOREIGN KEY([transaction_type_id])
REFERENCES [dbo].[transaction_type] ([id])
GO
