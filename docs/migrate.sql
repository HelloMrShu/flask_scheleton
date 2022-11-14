CREATE TABLE `user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(64) NOT NULL DEFAULT '' COMMENT '用户名',
  `email` varchar(128) NOT NULL DEFAULT '' COMMENT '邮箱',
  `status` tinyint(4) unsigned NOT NULL DEFAULT 0 COMMENT '状态 0-正常 1-停用',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';

CREATE TABLE `bug_statistics_day` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `username` varchar(64) NOT NULL DEFAULT '' COMMENT '用户名',
  `email` varchar(128) NOT NULL DEFAULT '0' comment '邮箱',
  `bug_count` int(11) unsigned NOT NULL DEFAULT 0 COMMENT 'bug数量',
  `stat_date` timestamp NOT NULL DEFAULT current_timestamp() COMMENT '统计日期',
  `year` int(11) unsigned NOT NULL DEFAULT 0 coment '年',
  `month` tinyint(4) NOT NULL DEFAULT 0 comment '月',
  `project` varchar(64) NOT NULL DEFAULT '' COMMENT '项目名称',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=170 DEFAULT CHARSET=utf8 COMMENT='日统计信息表';
