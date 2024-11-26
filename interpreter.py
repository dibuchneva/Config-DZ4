import csv
import struct
import argparse


class Interpreter:
    def __init__(self, binary_file, result_file, memory_range):
        self.binary_file = binary_file
        self.result_file = result_file
        self.memory = [0] * 256
        self.memory_range = memory_range

    def run(self):
        with open(self.binary_file, 'rb') as file:
            while command := file.read(6):
                args = struct.unpack("BBBBBB", command)
                self.execute_command(args)
        
        # Запись результата в формате CSV
        with open(self.result_file, mode='w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["address", "value"])  # Заголовки столбцов
            for i in range(*self.memory_range):
                csv_writer.writerow([i, self.memory[i]])

    def execute_command(self, args):
        opcode, op1, op2, op3, op4, op5 = args

        match opcode:
            case 19:
                self.memory[op1] = op2
            case 28:
                address = self.memory[op2] + op3
                self.memory[op1] = self.memory[address]
            case 7:
                address = self.memory[op1]
                self.memory[address] = self.memory[op2]
            case 30:
                # Побитовый сдвиг вправо
                # op1 (D) = результат, op2 (C) = операнд 2, op3 (B) = адрес результата
                reg_result = op1  # Адрес для результата
                reg_op2 = self.memory[op2]     # Адрес операнда 2
                reg_op1 = self.memory[op3]     # Адрес операнда 1
                
                self.memory[reg_result] = reg_op1 >> reg_op2  # Сдвиг вправо
                print(reg_op1 >> reg_op2)
            case _:
                raise ValueError(f"Unknown opcode: {opcode}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="путь к входному файлу")
    parser.add_argument("output_file", help="путь к выходному файлу")
    parser.add_argument("--memory_range", nargs=2, type=int, help="диапазон памяти для вывода результата")

    args = parser.parse_args()

    interpreter = Interpreter(args.input_file, args.output_file, tuple(args.memory_range))
    interpreter.run()