while True:
    try:
        def dec_to_bin(ip_dec):
            result_ip_bin = ".".join(format(int(x), "08b") for x in ip_dec.split("."))
            return result_ip_bin

        ip_dec = input("Enter IP-Address for conversion in BIN-conde: ")
        ip_bin_result = dec_to_bin(ip_dec)
        print(f"\nYour IP-Address in BIN-code:\n{ip_bin_result}\n{ip_dec}")


        def subnet_mask_to_bin(mask_to_bin):
            result_mask_to_bin = ".".join(format(int(x), "08b") for x in mask_to_bin.split("."))
            return result_mask_to_bin

        mask_to_bin = input("\nEnter Subnet mask: ")
        mask_to_bin_result = subnet_mask_to_bin(mask_to_bin)
        print(f"\nYour subnet mask in BIN-code:\n{mask_to_bin_result}\n{mask_to_bin}")


        def logical_and_with_dots(bin_str1, bin_str2):
            parts1 = bin_str1.split('.')
            parts2 = bin_str2.split('.')

            if len(parts1) != len(parts2):
                raise ValueError("Длины строк не совпадают")

            result_parts = []
            for part1, part2 in zip(parts1, parts2):
                if len(part1) != len(part2):
                    raise ValueError("Длины строк не совпадают")

                result_part = ""
                for bit1, bit2 in zip(part1, part2):
                    if bit1 == '1' and bit2 == '1':
                        result_part += '1'
                    else:
                        result_part += '0'
                result_parts.append(result_part)

            result = '.'.join(result_parts)
            return result

        bin_str1 = ip_bin_result
        bin_str2 = mask_to_bin_result
        result = logical_and_with_dots(bin_str1, bin_str2)
        print(f"\nResult of logical multiplication:\n{result}\n")


        def bin_to_dec(ip_bin):
            result_ip_dec = ".".join(str(int(x, 2)) for x in ip_bin.split("."))
            return result_ip_dec

        ip_bin = result
        ip_dec_result = bin_to_dec(ip_bin)
        print(f"It's Your Network address:\n{ip_dec_result}\n")


        def increment_last_digit(ip_dec):
            octets = ip_dec.split('.')
            last_octet = int(octets[-1]) + 1
            octets[-1] = str(last_octet)
            result_ip = '.'.join(octets)
            return result_ip

        ip_dec = ip_dec_result
        new_ip = increment_last_digit(ip_dec)
        print(f"First address in network:\n{new_ip}\n")


    except ValueError:
        print("ERROR!!! TRY AGAIN")