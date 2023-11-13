while True:
    try:
        def dec_to_bin(ipdeccode):
            result_ip_bin = ".".join(format(int(x), "08b") for x in ipdeccode.split("."))
            return result_ip_bin


        ip_dec = input("$:-Enter IP-Address for conversion in BIN-conde ==> ")
        ip_bin_result = dec_to_bin(ip_dec)
        print(f"---->Your IP-Address in BIN-code:\n        {ip_bin_result} = {ip_dec}")


        def subnet_mask_to_bin(masktobin):
            result_mask_to_bin = ".".join(format(int(x), "08b") for x in masktobin.split("."))
            return result_mask_to_bin


        mask_to_bin = input("$:-Enter Subnet mask ==> ")
        mask_to_bin_result = subnet_mask_to_bin(mask_to_bin)
        print(f"---->Your subnet mask in BIN-code:\n        {mask_to_bin_result} = {mask_to_bin}")


        def count_zeros(BINstr):
            count = BINstr.count('0')
            return count


        bin_str = mask_to_bin_result
        zero_count = count_zeros(bin_str)
        print(f"------------>How many zeros in the subnet mask BIN-code:\n                {zero_count}")

        math1 = 2 ** zero_count
        math2 = math1 - 2
        print(f"-------------------->Number of IP addresses in the network:\n                        {math2}")


        def logical_and_with_dots(BINstr1, BINstr2):
            parts1 = BINstr1.split('.')
            parts2 = BINstr2.split('.')

            if len(parts1) != len(parts2):
                raise ValueError("!!!The number of octets does not match!!!")

            result_parts = []
            for part1, part2 in zip(parts1, parts2):
                if len(part1) != len(part2):
                    raise ValueError("!!!String lengths do not match!!!")

                result_part = ""
                for bit1, bit2 in zip(part1, part2):
                    if bit1 == '1' and bit2 == '1':
                        result_part += '1'
                    else:
                        result_part += '0'
                result_parts.append(result_part)

            result0 = '.'.join(result_parts)
            return result0


        bin_str1 = ip_bin_result
        bin_str2 = mask_to_bin_result
        result = logical_and_with_dots(bin_str1, bin_str2)
        print(f"---------------------------->Result of logical multiplication:\n                                {result}")


        def bin_to_dec(ipbin):
            result_ip_dec = ".".join(str(int(x, 2)) for x in ipbin.split("."))
            return result_ip_dec


        ip_bin = result
        ip_dec_result = bin_to_dec(ip_bin)
        print(f"---------------------------->It's Your Network address:\n                        {ip_dec_result}")


        def increment_last_digit(ipdec):
            octets = ipdec.split('.')
            last_octet = int(octets[-1]) + 1
            octets[-1] = str(last_octet)
            result_ip = '.'.join(octets)
            return result_ip


        first_ip_address = ip_dec_result
        new_ip = increment_last_digit(first_ip_address)
        print(f"-------------------->First address in network:\n                {new_ip}")


        def last_ip_address(lastip):
            octets = lastip.split('.')
            last_octet = int(octets[-1]) + math2
            octets[-1] = str(last_octet)
            result_ip = '.'.join(octets)
            return result_ip


        last_ip = ip_dec_result
        last_ip_in_network = last_ip_address(last_ip)
        print(f"------------>Last ip address:\n        {last_ip_in_network}")


        def broadcast_ip_address(lastip):
            octets = lastip.split('.')
            last_octet = int(octets[-1]) + math2 + 1
            octets[-1] = str(last_octet)
            result_ip = '.'.join(octets)
            return result_ip


        broadcast = ip_dec_result
        broadcast_ip_address_in_network = broadcast_ip_address(broadcast)
        print(f"---->Broadcast ip address:\n{broadcast_ip_address_in_network}\n")

        with open("outputdata.txt", "a") as file:
            file.write(f"---->Your IP-Address in BIN-code:\n        {ip_bin_result} = {ip_dec}\n")
            file.write(f"---->Your subnet mask in BIN-code:\n        {mask_to_bin_result} = {mask_to_bin}\n")
            file.write(f"------------>How many zeros in the subnet mask BIN-code:\n                {zero_count}\n")
            file.write(f"-------------------->Number of IP addresses in the network:\n                        {math2}\n")
            file.write(f"---------------------------->Result of logical multiplication:\n                                {result}\n")
            file.write(f"---------------------------->It's Your Network address:\n                        {ip_dec_result}\n")
            file.write(f"-------------------->First address in network:\n                {new_ip}\n")
            file.write(f"------------>Last ip address:\n        {last_ip_in_network}\n")
            file.write(f"---->Broadcast ip address:\n{broadcast_ip_address_in_network}\n")
            file.write("\n")  # Добавляем пустую строку для разделения записей в файле

    except ValueError:
        print(f"ERROR: {ValueError}. TRY AGAIN")
