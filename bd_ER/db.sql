-- department table
CREATE TABLE IF NOT EXISTS department (
  department_id INT NOT NULL,
  department varchar(50) NOT NULL,
  PRIMARY KEY (department_id)
);

-- state table
CREATE TABLE IF NOT EXISTS state (
  state_id INT NOT NULL,
  state varchar(50) NOT NULL,
  PRIMARY KEY (state_id)
);

-- city table
CREATE TABLE IF NOT EXISTS city (
  city_id INT NOT NULL,
  city varchar(50) NOT NULL,
  state_id INT NOT NULL,
  PRIMARY KEY (city_id),
  CONSTRAINT fk_state
      FOREIGN KEY(state_id) 
	  REFERENCES state(state_id)
);

-- address table
CREATE TABLE IF NOT EXISTS address (
  address_id INT NOT NULL,
  address varchar(50) NOT NULL,
  zip INT NULL,  
  city_id INT NOT NULL,
  PRIMARY KEY (address_id),
  CONSTRAINT fk_city
      FOREIGN KEY(city_id) 
	  REFERENCES city(city_id)
);

-- company table
CREATE TABLE IF NOT EXISTS company (
  company_id INT NOT NULL,
  company_name varchar(250) NOT NULL,
  phone1 varchar(50) NOT NULL,
  phone2 varchar(50) NULL,  
  address_id INT NOT NULL,
  department_id INT NOT NULL,
  PRIMARY KEY (company_id),
  CONSTRAINT fk_address
      FOREIGN KEY(address_id) 
	  REFERENCES address(address_id),
  CONSTRAINT fk_department
      FOREIGN KEY(department_id) 
	  REFERENCES department(department_id)  
);

-- employees table
CREATE TABLE IF NOT EXISTS employees (
    employees_id INT NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,    
    email VARCHAR(50) NOT NULL,
    company_id INT NOT NULL,
    PRIMARY KEY (employees_id),
    CONSTRAINT fk_company FOREIGN KEY (company_id)
        REFERENCES company (company_id)
);