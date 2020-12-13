package com.article.finder;

import ch.qos.logback.core.net.SyslogOutputStream;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.jdbc.core.JdbcTemplate;

import javax.sql.DataSource;
import java.sql.*;

@SpringBootApplication
public class ArticleFinderApplication {

	private DataSource dataSource;
	private JdbcTemplate jdbcTemplate;

	ArticleFinderApplication(DataSource dataSource){
		this.dataSource = dataSource;
		jdbcTemplate = new JdbcTemplate(dataSource);
	}


	public static void main(String[] args) {
		SpringApplication.run(ArticleFinderApplication.class, args);
		System.out.println("started");
	}

	/*@Override
	public void run(String... args) throws Exception{
		System.out.println(dataSource);


		final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
		final String DB_URL = "jdbc:mysql://localhost/articlefinder";

		//  Database credentials
		final String USER = "root";
		final String PASS = "root";

			Connection conn = null;
			Statement stmt = null;
			try{
				//STEP 2: Register JDBC driver
				//Class.forName("com.mysql.jdbc.Driver");

				//STEP 3: Open a connection
				System.out.println("Connecting to a selected database...");
				conn = DriverManager.getConnection(DB_URL, USER, PASS);
				System.out.println("Connected database successfully...");

				//STEP 4: Execute a query
				System.out.println("Creating statement...");
				stmt = conn.createStatement();

				String sql = "SELECT * FROM pdf";
				ResultSet rs = stmt.executeQuery(sql);
				//STEP 5: Extract data from result set
				while(rs.next()){
					//Retrieve by column name
					int id  = rs.getInt("id");
					String filename = rs.getString("filename");
					//String tex = rs.getString("last");

					//Display values
					System.out.print("ID: " + id);
					System.out.println(", File: " + filename);
				}
				rs.close();
			}catch(SQLException se){
				//Handle errors for JDBC
				se.printStackTrace();
			}catch(Exception e){
				//Handle errors for Class.forName
				e.printStackTrace();
			}finally{
				//finally block used to close resources
				try{
					if(stmt!=null)
						conn.close();
				}catch(SQLException se){
				}// do nothing
				try{
					if(conn!=null)
						conn.close();
				}catch(SQLException se){
					se.printStackTrace();
				}//end finally try
			}//end try
			System.out.println("Goodbye!");
		//end main
	}*/

	}


