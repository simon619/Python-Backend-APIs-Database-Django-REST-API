import json
import requests


class Node:

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.next = None


class MergeSort:

    def __int__(self):
        pass

    def get_the_middle(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right_head = slow.next
        slow.next = None
        return head, right_head

    def divide(self, head):
        if not head.next or not head:
            return head
        else:
            left_head, right_head = self.get_the_middle(head)
            left = self.divide(left_head)
            right = self.divide(right_head)
            return self.merging(left, right)

    def merging(self, link1, link2):
        current_node, head = None, None
        while link1 and link2:
            if link1.number < link2.number:
                if not head:
                    head = link1
                    current_node = head
                else:
                    current_node.next = link1
                    current_node = current_node.next
                link1 = link1.next
            else:
                if not head:
                    head = link2
                    current_node = head
                else:
                    current_node.next = link2
                    current_node = current_node.next
                link2 = link2.next

        while link1:
            if not current_node and not head:
                head = link1
                current_node = head
            else:
                current_node.next = link1
                current_node = current_node.next
            link1 = link1.next

        while link2:
            if not current_node and not head:
                head = link2
                current_node = link2
            else:
                current_node.next = link2
                current_node = current_node.next
            link2 = link2.next

        return head

    def create_linked_list(self, head, name, number):
        if not head.name or not head.number:
            head.name, head.number = name, number
            return head
        else:
            header, current_node = head, head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(name, number)
            return header

    def print_linked_list(self, head):
        counter = 0
        current_node = head
        while current_node:
            counter += 1
            print(f'Package Name: [{current_node.name}], Used in Last 30days: [{current_node.number}] Times')
            current_node = current_node.next
        print(f'Length of sorted data: {counter}')

    def do_everything_in_real_time(self, root):
        r = requests.get('https://formulae.brew.sh/api/formula.json')  # All packages
        all_packages_info_json = r.json()
        print(f'Length of data: {len(all_packages_info_json)}')

        # number = len(all_packages_info_json) - (len(all_packages_info_json) - 30)
        for i in range(len(all_packages_info_json)):
            current_package_name = all_packages_info_json[i]['name']
            print(current_package_name)

            current_url = f'https://formulae.brew.sh/api/formula/{current_package_name}.json'
            req = requests.get(current_url)
            current_package_json = req.json()

            days_30 = current_package_json['analytics']['install_on_request']['30d'][current_package_name]
            days_90 = current_package_json['analytics']['install_on_request']['90d'][current_package_name]
            days_365 = current_package_json['analytics']['install_on_request']['365d'][current_package_name]

            root = self.create_linked_list(root, current_package_name, (days_90 + days_30 + days_365))

        sorted = self.divide(root)
        self.print_linked_list(sorted)


if __name__ == '__main__':
    obj = MergeSort()
    root = Node(None, None)
    # [Uncomment this for fetching from local drive]
    # with open('package_data.json', 'r') as f:
    #     data = json.load(f)
    # print(f'Length of data: {len(data)}')
    # for i in range(len(data)):
    #     root = obj.create_linked_list(root, data[i]['name'], data[i]['analytics']['30d'])
    # print('')
    # sorted = obj.divide(root)
    # obj.print_linked_list(sorted)

    # [Uncomment this for fetching from web api]
    obj.do_everything_in_real_time(root)



