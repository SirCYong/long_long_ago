
__author__ = 'Yong_li'
import re

# For test only
EMPTY_CONFIG_XML = '''<?xml version='1.0' encoding='UTF-8'?>
<project>
  <description>yongli job description.</description>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <scm class="hudson.plugins.git.GitSCM" plugin="git@3.0.1">
    <configVersion>2</configVersion>
    <userRemoteConfigs>
      <hudson.plugins.git.UserRemoteConfig>
        <url>ssh://git@192.168.6.115:7999/tmp/testcase.git</url>
        <credentialsId>5d6159e0-7183-4d07-a90e-4eccd8a2e3d7</credentialsId>
      </hudson.plugins.git.UserRemoteConfig>
    </userRemoteConfigs>
    <branches>
      <hudson.plugins.git.BranchSpec>
        <name>*/master</name>
      </hudson.plugins.git.BranchSpec>
    </branches>
    <doGenerateSubmoduleConfigurations>false</doGenerateSubmoduleConfigurations>
    <gitTool>git-2.7.2</gitTool>
    <submoduleCfg class="list"/>
    <extensions/>
  </scm>
  <assignedNode>yonglirunhost</assignedNode>
  <canRoam>false</canRoam>
  <disabled>false</disabled>
  <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
  <jdk>(System)</jdk>
  <triggers>
    <hudson.triggers.TimerTrigger>
      <spec>H/12 * * * *</spec>
    </hudson.triggers.TimerTrigger>
  </triggers>
  <concurrentBuild>false</concurrentBuild>
  <builders>
    <hudson.tasks.Shell>
      <command>yonglishell1</command>
    </hudson.tasks.Shell>
    <hudson.tasks.Shell>
      <command>yonglishell2</command>
    </hudson.tasks.Shell>
  </builders>
  <publishers>
    <hudson.tasks.junit.JUnitResultArchiver plugin="junit@1.18">
      <testResults>yonglijunittestreport</testResults>
      <keepLongStdio>false</keepLongStdio>
      <healthScaleFactor>80.0</healthScaleFactor>
      <allowEmptyResults>false</allowEmptyResults>
    </hudson.tasks.junit.JUnitResultArchiver>
    <hudson.tasks.Mailer plugin="mailer@1.18">
      <recipients>zhuangyongli@iscs.com.cn</recipients>
      <dontNotifyEveryUnstableBuild>false</dontNotifyEveryUnstableBuild>
      <sendToIndividuals>false</sendToIndividuals>
    </hudson.tasks.Mailer>
  </publishers>
  <buildWrappers/>
</project>'''


def two_platform_jobs_xml(args):
    return _jenkins_configuration_file(args, 'ios'), _jenkins_configuration_file(args, 'android')
    pass


def _jenkins_configuration_file(args, platform):
    """
    XML configuration creator
    :param args: parameters about
    :type args: dict
    :param platform: ios or android only
    :type platform:str
    :return: XML configuration creator
    :rtype: str
    """
    if re.findall('ios', platform, flags=re.IGNORECASE):
        run_host = args['iOS_Run_Host']
    else:
        run_host = args['android_run_host']
    TEMPLATE_CONFIG_XML = '''<?xml version='1.0' encoding='UTF-8'?>
    <project>
      <description>{}</description>
      <keepDependencies>false</keepDependencies>
      <properties/>
      <scm class="hudson.plugins.git.GitSCM" plugin="git@3.0.1">
        <configVersion>2</configVersion>
        <userRemoteConfigs>
          <hudson.plugins.git.UserRemoteConfig>
            <url>ssh://git@192.168.6.115:7999/tmp/testcase.git</url>
            <credentialsId>5d6159e0-7183-4d07-a90e-4eccd8a2e3d7</credentialsId>
          </hudson.plugins.git.UserRemoteConfig>
        </userRemoteConfigs>
        <branches>
          <hudson.plugins.git.BranchSpec>
            <name>*/master</name>
          </hudson.plugins.git.BranchSpec>
        </branches>
        <doGenerateSubmoduleConfigurations>false</doGenerateSubmoduleConfigurations>
        <gitTool>git-2.7.2</gitTool>
        <submoduleCfg class="list"/>
        <extensions/>
      </scm>
      <assignedNode>{}</assignedNode>
      <canRoam>false</canRoam>
      <disabled>false</disabled>
      <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
      <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
      <jdk>(System)</jdk>
      <triggers>
        <hudson.triggers.TimerTrigger>
          <spec>{}</spec>
        </hudson.triggers.TimerTrigger>
      </triggers>
      <concurrentBuild>false</concurrentBuild>
      <builders>
        <hudson.tasks.Shell>
          <command>{}</command>
        </hudson.tasks.Shell>
        <hudson.tasks.Shell>
          <command>{}</command>
        </hudson.tasks.Shell>
      </builders>
      <publishers>
        <hudson.tasks.junit.JUnitResultArchiver plugin="junit@1.18">
          <testResults>{}</testResults>
          <keepLongStdio>false</keepLongStdio>
          <healthScaleFactor>{}</healthScaleFactor>
          <allowEmptyResults>false</allowEmptyResults>
        </hudson.tasks.junit.JUnitResultArchiver>
        <hudson.tasks.Mailer plugin="mailer@1.18">
          <recipients>{}</recipients>
          <dontNotifyEveryUnstableBuild>false</dontNotifyEveryUnstableBuild>
          <sendToIndividuals>false</sendToIndividuals>
        </hudson.tasks.Mailer>
      </publishers>
      <buildWrappers/>
    </project>'''.format('AutomationToolCreatedJob', run_host, args['time_trigger_cycle'], args['build_shell_1'],
                         args['build_shell_2'], args['junit_test_reporter'], args['pass_threshold'], args['recipient'])
    return TEMPLATE_CONFIG_XML
