import boto3
# import pprint
from time import sleep

import serial

matching_name = 'Eric'
# pp = pprint.PrettyPrinter(indent=2)

serial_device = '/dev/tty.usbmodem1411'
serial_speed = 9600

class EmrWatcher:
    def __init__(self, matching_name, serial_device, serial_speed):
        self.matching_name = matching_name.lower()
        self.client = boto3.client('emr')

        self.serial_client = serial.Serial(serial_device, serial_speed)

    def watch(self):
        while True:
            result = self.__check_clusters()
            print result

            if result == True:
                byteString = '1'
            else:
                byteString = '0'
            self.serial_client.write(byteString)

            sleep(60)

    def __check_clusters(self):
        clusters = self.__emr_clusters()
        for cluster in clusters['Clusters']:
            cluster_name_matches = self.__cluster_name_matches(cluster)
            if cluster_name_matches:
                return True
            cluster_tags_match = self.__cluster_tags_match(cluster)
            if cluster_tags_match:
                return True
        return False

    def __cluster_name_matches(self, cluster):
        if self.matching_name in cluster['Name'].lower():
            return True
        else:
            return False

    def __cluster_tags_match(self, cluster):
        cluster_description = self.__emr_cluster_description(cluster)
        cluster_tags = self.__emr_cluster_tags(cluster_description)
        tags_string = self.__cluster_tags_string(cluster_tags)
        if self.matching_name in tags_string.lower():
            return True
        else:
            return False

    def __cluster_tags_string(self, cluster_tags):
        tag_values = [d['Value'] for d in cluster_tags]
        return "".join(tag_values)

    def __emr_cluster_description(self, cluster):
        return self.client.describe_cluster(
            ClusterId=cluster['Id']
        )

    def __emr_cluster_tags(self, cluster_description):
        return cluster_description['Cluster']['Tags'];

    def __emr_clusters(self):
        return self.client.list_clusters(
            ClusterStates=[
                'STARTING', 'BOOTSTRAPPING', 'RUNNING', 'WAITING'
            ]
        )

emr_watcher = EmrWatcher(matching_name, serial_device, serial_speed)
emr_watcher.watch()
