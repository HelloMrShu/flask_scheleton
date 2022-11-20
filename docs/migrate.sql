 CREATE TABLE `user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT comment '主键',
  `name` varchar(32) NOT NULL DEFAULT '' comment '用户名',
  `email` varchar(128) not null default '' COMMENT '邮箱',
  `status` tinyint(4) unsigned not null default '0' COMMENT '状态 0-正常 1-失效',
  `created_at` timestamp NOT NULL DEFAULT '1970-02-01 00:00:00' COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '用户表';
