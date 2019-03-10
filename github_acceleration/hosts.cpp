/**
 * 网上提供的github加速方法,封装后需要管理员权限
 */
#include <stdio.h>
int main(int argc, char const *argv[]) {
  // FILE *input = fopen("hosts.txt","r");
  FILE *hosts = fopen("C:/Windows/System32/drivers/etc/hosts","a");
  fprintf(hosts, "%s\n", "\n# GitHub Start  updated 15-1-2019");
  fprintf(hosts, "%s\n", "192.30.253.118 gist.github.com");
  fprintf(hosts, "%s\n", "151.101.112.133 assets-cdn.github.com");
  fprintf(hosts, "%s\n", "151.101.184.133 raw.githubusercontent.com");
  fprintf(hosts, "%s\n", "151.101.112.133 gist.githubusercontent.com");
  fprintf(hosts, "%s\n", "151.101.184.133 cloud.githubusercontent.com");
  fprintf(hosts, "%s\n", "151.101.112.133 camo.githubusercontent.com");
  fprintf(hosts, "%s\n", "151.101.112.133 avatars0.githubusercontent.com");
  fprintf(hosts, "%s\n", "151.101.112.133 avatars1.githubusercontent.com");
  fprintf(hosts, "%s\n", "151.101.184.133 avatars2.githubusercontent.com");
  fprintf(hosts, "%s\n", "151.101.12.133 avatars3.githubusercontent.com");
  fprintf(hosts, "%s\n", "151.101.12.133 avatars4.githubusercontent.com");
  fprintf(hosts, "%s\n", "151.101.184.133 avatars5.githubusercontent.com");
  fprintf(hosts, "%s\n", "151.101.184.133 avatars6.githubusercontent.com");
  fprintf(hosts, "%s\n", "151.101.184.133 avatars7.githubusercontent.com");
  fprintf(hosts, "%s\n", "151.101.12.133 avatars8.githubusercontent.com");
  fprintf(hosts, "%s\n\n", "# GitHub End");
  fclose(hosts);

  return 0;
}
