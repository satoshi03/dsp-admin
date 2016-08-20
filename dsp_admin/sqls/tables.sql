CREATE TABLE media (
  id int primary key not null,
  name varchar(255),
  url varchar(65535),
  PRIMARY KEY (id)
);

CREATE TABLE exclude_media (
  id int auto increment not null,
  media_id int not null REFERENCES media(id),
  campaign_id int not null REFERENCES campaign(id),
  PRIMARY KEY (id)
);

CREATE TABLE client (
  id int auto increment not null,
  name varchar(255),
  address varchar(65535),
  PRIMARY KEY (id)
);

CREATE TABLE product (
  id int auto increment not null,
  client_id int not null REFERENCES client(id),
  PRIMARY KEY (id)
);

CREATE TABLE campaign (
  id int auto increment not null,
  product_id int not null REFERENCES product(id),
  name varchar(255) not null,
  price int not null,
  daily_budget int not null,
  starts_at datetime not null,
  ends_at datetime not null,
  price_type enum('cpc', 'cpm', 'cpa') not null,
  bid_type enum('smooth') not null,
  PRIMARY KEY (id)
);

CREATE TABLE creative (
  id int auto increment not null,
  campaign_id int not null REFERENCES campaign(id),
  title varchar(100) not null,
  url varchar(65535) not null,
  image_url varchar(65535) not null,
  description varchar(255) not null,
  PRIMARY KEY (id)
);
