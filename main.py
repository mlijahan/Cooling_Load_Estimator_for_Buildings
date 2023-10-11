import numpy as np
import psycopg2
import math
import scipy
import scipy.interpolate
import pandas as pd




""" Calculation of Wheel dozers Production, pollutant emission and Cost"""

"""Production and Rimpull of Track type dozers Calculation"""

try:
    connection = psycopg2.connect(database="Earthwork",
                                  user="postgres",
                                  password="Magool@123",
                                  host="localhost",
                                  port="5432")


    class Activity:

        def activity(self):
            self.main_activity_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                                       '14', '15',
                                       '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                                       '28',
                                       '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
                                       '41',
                                       '42', '43']
            self.equipment_package = [['Front End Shovel'], ['Dozer', 'Scraper', 'Backhoe', 'Excavator'],
                                      ['Dozer', 'Excavator'],
                                      ['Dozer'], ['Grader'], ['Dozer', 'Excavator'],
                                      ['Dozer', 'Grader', 'Scraper'],
                                      ['Dozer', 'Scraper'], ['Dozer', 'Loader', 'Scraper', 'Dump Truck'],
                                      ['Grader'],
                                      ['Backhoe', 'Excavator'], ['Loader', 'Backhoe', 'Excavator'],
                                      ['Backhoe', 'Excavator'],
                                      ['Dozer', 'Loader', 'Grader', 'Dump Truck'],
                                      ['Dozer', 'Loader', 'Grader', 'Dump Truck'],
                                      ['Grader'], ['Dozer', 'Grader', 'Dump Truck', 'Backhoe', 'Excavator'],
                                      ['Dozer', 'Grader', 'Dump Truck'], ['Backhoe', 'Excavator'],
                                      ['Dozer', 'Loader'],
                                      ['Scraper'],
                                      ['Dump Truck'], ['Dozer', 'Grader'],
                                      ['Dozer', 'Loader', 'Grader', 'Scraper', 'Dump Truck'],
                                      ['Loader', 'Dump Truck'], ['Excavator'], ['Backhoe'],
                                      ['Dozer', 'Loader', 'Backhoe', 'Excavator'],
                                      ['Backhoe', 'Excavator'], ['Excavator'], ['Backhoe', 'Excavator'],
                                      ['Loader', 'Dump Truck', 'Excavator'],
                                      ['Dozer', 'Loader', 'Dump Truck', 'Excavator'],
                                      ['Dozer', 'Loader', 'Dump Truck', 'Excavator'],
                                      ['Dozer', 'Loader', 'Dump Truck', 'Excavator'],
                                      ['Dozer', 'Loader', 'Dump Truck', 'Excavator'],
                                      ['Dozer', 'Scraper'], ['Dozer', 'Loader'], ['Excavator'],
                                      ['Dozer', 'Grader', 'Dump Truck'],
                                      ['Dozer', 'Scraper', 'Excavator'], ['Dozer', 'Grader', 'Excavator'],
                                      ['Dozer']]

        def select_activit(self):
            self.chosed = input("Please insert activity:\n(1) 'Excavating above grade'\
                \n(2) 'Excavating below grade'\n(3) 'Grubbing'\n(4)'Heavy ripping'\n(5) 'Light ripping'\
                \n(6) 'Tree stump removal'\n(7) 'Topsoil removal/storage'\n(8) 'Rough cutting'\n(9) 'Rough filling'\
                \n(10) 'Finish grading'\n(11) 'Foundation excavation'\n(12) 'Foundation backfilling'\
                \n(13) 'Footing excavation'\n(14) 'Road base construction'\n(15) 'Temporary road'\
                \n(16) 'Haul road maintenance'\n(17) 'Culvert placement'\n(18) 'Earth berm or dam construction'\
                \n(19) 'Drainage ditch maintenance'\n(20) 'Haul less than 500 ft'\n(21) 'Haul 500 ft to 2 miles'\
                \n(22) 'Haul over 2 miles'\n(23) 'Soil windrowing'\n(24) 'Soil spreading'\n(25) 'Excess loose soil removal'\
                \n(26) 'Deep trench excavation'\n(27) 'Shallow trench excavation'\n(28) 'Trench backfilling'\
                \n(29) 'Utility pipe placing — small'\n(30) 'Utility pipe placing — large'\n(31) 'Trench box placement,movement'\
                \n(32) 'trash or debris removal'\n(33) 'Rock removal' \n(34) 'Asphalt paving removal' \n(35) 'Concrete removal'\
                \n(36) 'Structure demo'\n(37) 'Assisting scrapers'\n(38) 'Towing other equipment'\n(39) 'Concrete placement bucket'\
                \n(40) 'Crane pad construction'\n(41) 'Crane pad construction'\n(42) 'Benching'\n(43) 'Side sloping'\n\n")
            self.activity_package = dict(zip(self.main_activity_list, self.equipment_package))
            for k, v in self.activity_package.items():
                if k == self.chosed:
                    print(v)
                    break
            else:
                input("Please insert a new main activity:\n")

        def subactivity(self):
            self.subactivity_volume_unit_machine = []
            n = int(input(
                "Enter ID number of subactivity it's name, volume (m3), machine type which do that:\n\n"))
            for i in range(0, n):
                ele = [input(), int(input()),
                       input("\n(a) 'Dozer'\n(b) 'Loader'\n(c) 'Grader'\n")]
                self.subactivity_volume_unit_machine.append(ele)
                print(self.subactivity_volume_unit_machine)
            # self.subii = [x[3] for x in self.subactivity_volume_unit_machine]
            # if self.subii[0] == 'a':
            #     if self.subii[4] < 100:

        def volume_subactivity(self):
            self.toatal_valume_or_area = [x[1] for x in self.subactivity_volume_unit_machine]
            # print(self.toatal_valume_or_area)
            return (self.toatal_valume_or_area)

        def hauling_material_type(self):
            self.cur = connection.cursor()
            self.cur.execute(f"SELECT matrial_type FROM weight_material ")
            self.result_surface = self.cur.fetchall()
            print(self.result_surface)
            self.material_type = input("Please select a material type:\n")
            self.cur.execute(f"SELECT * FROM weight_material WHERE matrial_type ={self.material_type}")
            self.result_density = self.cur.fetchall()
            return (self.result_density)

        def surface_type(self):
            self.cur = connection.cursor()
            self.cur.execute(f"SELECT type_surface FROM rolling_resistance ")
            self.result_surface = self.cur.fetchall()
            print(self.result_surface)
            self.surface_type = input("Please select a surface type:\n")
            self.cur.execute(f"SELECT * FROM rolling_resistance WHERE type_surface ={self.surface_type}")
            self.result_rr = self.cur.fetchall()
            return (self.result_rr)

        def fill_factor_wheel_loader(self):
            self.cur = connection.cursor()
            self.cur.execute(f"SELECT material FROM bucket_fill_factor ")
            self.result_fill = self.cur.fetchall()
            print(self.result_fill)
            self.material = input("Please select a material for filling bucket:\n")
            self.min_max_fillfactor = input("Please insert fill factor type:\n(a) 'minimum'\n(b) 'maximum':\n")
            if self.min_max_fillfactor == "a":
                self.cur.execute(f"SELECT wheel_loader_min_percent FROM bucket_fill_factor WHERE material ={self.material}")
                self.result_fills = self.cur.fetchall()
                # print(self.result_fill)
                return (self.result_fill)
            if self.min_max_fillfactor == "b":
                self.cur.execute(f"SELECT wheel_loader_max_percent FROM bucket_fill_factor WHERE material ={self.material}")
                self.result_fills= self.cur.fetchall()
                # print(self.result_fill)
                return (self.result_fills)



        def fill_factor_track_loader(self):
            self.cur = connection.cursor()
            self.cur.execute(f"SELECT Material FROM Bucket_fill_factor ")
            self.result_fill = self.cur.fetchall()
            self.material = input("Please select a material for filling bucket:\n")
            self.min_max_fillfactor = input("Please insert fill factor type:\n(a) 'minimum'\n(b) 'maximum':\n")
            if self.min_max_fillfactor == "a":
                self.cur.execute(f"SELECT track_loader_min_percent FROM Bucket_fill_factor WHERE Material ={ self.material}")
                self.result_fill_min = self.cur.fetchall()
                return (self.result_fill_min)
            if self.min_max_fillfactor == "b":
                self.cur.execute(f"SELECT track_loader_max_percent FROM Bucket_fill_factor WHERE Material ={ self.material}")
                self.result_fill_max = self.cur.fetchall()
                return (self.result_fill_max)

    class Excavators(Activity):

        def Excavators_features(self):
            super().activity()
            super().select_activit()
            super().subactivity()
            self.all_excavators = []
            self.all_excavator_speeds = []
            self.all_excavator_consumption = []
            self.costs_input_excavator = []
            self.cur = connection.cursor()
            self.cur.execute(f"SELECT excavetor_id, excavetor_models, bucket_capacity_max_m3,stick_length_m, maximum_digging_depth,\
                                maximum_cutting_height, manufacture,year_of_operation FROM excavators")
            result_models = self.cur.fetchall()
            print(result_models)
            self.model = input("Please select the first track Excavator model ID:\n")
            self.cur = connection.cursor()
            self.cur.execute(f"SELECT excavetor_id, excavetor_models , flywheel_power_hp , operating_weight_kg ,\
                            bucket_capacity_max_m3,  maximum_digging_depth, maximum_cutting_height,\
                             cycle_time_min, max_drawbarpull_kn FROM excavators WHERE excavetor_id ={self.model}")
            self.result = self.cur.fetchall()
            self.all_excavators.append(self.result)
            print(self.all_excavators)
            self.cur.execute(f"SELECT excavetor_id, excavetor_models, max_travel_speed_lo_kmh,\
                        max_travel_speed_hi_kmh FROM excavators WHERE  excavetor_id ={self.model}")
            self.results = self.cur.fetchall()
            self.all_excavator_speeds.append(self.results)
            print(self.all_excavator_speeds)
            self.cur.execute(f"SELECT excavetor_id, excavetor_models, delivered_price_dollars,\
                                sales_tax_percent, interest_percent, insurance_percent, tax_percent, year_of_operation,\
                                capacity_crankcase_galon, hours_between_lubricating_changes FROM excavators WHERE  excavetor_id ={self.model}")
            self.resultss = self.cur.fetchall()
            self.costs_input_excavator.append(self.resultss)
            print(self.costs_input_excavator)
            ques = input("Do you want to select another model?")
            while ques == 'YES':
                self.cur = connection.cursor()
                self.cur.execute(f"SELECT excavetor_id, excavetor_models, bucket_capacity_max_m3,stick_length_m, maximum_digging_depth,\
                                maximum_cutting_height, manufacture,year_of_operation FROM excavators")
                result_models = self.cur.fetchall()
                print(result_models)
                self.model = input("Please select another excavator model ID:\n")
                self.cur = connection.cursor()
                self.cur.execute(f"SELECT excavetor_id, excavetor_models , flywheel_power_hp , operating_weight_kg ,\
                            bucket_capacity_max_m3,  maximum_digging_depth, maximum_cutting_height,\
                             cycle_time_min, max_drawbarpull_kn FROM excavators WHERE excavetor_id ={self.model}")
                self.result = self.cur.fetchall()
                self.all_excavators.append(self.result)
                print(self.all_excavators)
                self.cur.execute(f"SELECT excavetor_id, excavetor_models, max_travel_speed_lo_kmh,\
                        max_travel_speed_hi_kmh FROM excavators WHERE  excavetor_id ={self.model}")
                self.results = self.cur.fetchall()
                self.all_excavator_speeds.append(self.results)
                print(self.all_excavator_speeds)
                self.cur.execute(f"SELECT excavetor_id, excavetor_models, delivered_price_dollars,\
                                sales_tax_percent, interest_percent, insurance_percent, tax_percent, year_of_operation,\
                                capacity_crankcase_galon, hours_between_lubricating_changes FROM excavators WHERE  excavetor_id ={self.model}")
                self.resultss = self.cur.fetchall()
                self.costs_input_excavator.append(self.resultss)
                print(self.costs_input_excavator)
                ques = input("Do you want to select another excavator model?")
            quess = input("Do you want to estimate cost for each model?")
            if quess == 'YES':
                self.models = [[x[0] for x in self.result] for self.result in self.all_excavators]
                print(self.models)
                self.cost_input_excavatorS = []
                for model in self.models:
                    self.cost_input_excavator = []
                    for name in model:
                        self.cost_input_excavator.append(float(input("Please insert price of per gallon of fuel $:\n")))
                        self.cost_input_excavator.append(int(input("Please insert cost of lubricating ($):\n\n")))
                        self.cost_input_excavator.append(int(input("Please operator wage per hour($):\n\n")))
                        print(self.cost_input_excavator)
                    self.cost_input_excavatorS.append(self.cost_input_excavator)
                    print(self.cost_input_excavatorS)

        @property
        def modelnames(self):
            self.modelname = [[x[1] for x in self.result] for self.result in self.all_excavators]
            self.modelnamer = [item for sublist in self.modelname for item in sublist]
            return (self.modelnamer)

        @property
        def modelcodes(self):
            self.modelcoderr = [[x[0] for x in self.result] for self.result in self.all_excavators]
            self.modelcoderN = [item for sublist in self.modelcoderr for item in sublist]
            self.modelcoderS = [str(elem) for elem in self.modelcoderN]
            self.modelcoder = [i +'/'+ j for i, j in zip(self.modelcoderS, self.modelnamer)]
            return (self.modelcoder)

        @property
        def horspower_track(self):
            self.horsepower = [[x[2] for x in self.result] for self.result in self.all_excavators]
            self.horesspower = np.array(self.horsepower)
            self.horsepowerr = [item for sublist in self.horesspower for item in sublist]
            return (self.horsepowerr)

        @property
        def horsepowerr_height_temp(self):
            self.T0 = float(input("Please insert mean of temp of job site in c:\n\n"))
            self.Tc = 288.6
            self.T0_K = 288.6 + self.T0
            self.T0_Tc = self.T0_K / self.Tc
            self.root_T0_Tc = math.sqrt(self.T0_Tc)
            self.p0 = float(input("Please insert mean of height of job site in m:\n\n"))
            self.Pc = 76
            self.pc_p0 = np.round(self.p0 / self.Pc, 2)
            self.tc0 = np.round(1 / self.root_T0_Tc, 2)
            self.real_horsepowers = self.horesspower * self.pc_p0 * self.tc0
            self.real_horsepowerr = [item for sublist in self.real_horsepowers for item in sublist]
            self.real_horsepower = np.array(self.real_horsepowerr)
            return (self.real_horsepower)


        @property
        def operating_weight(self):
            self.operating_weights = [[x[3] for x in self.result] for self.result in self.all_excavators]
            self.operatingweight= [item for sublist in self.operating_weights for item in sublist]
            self.operating_weights_track = np.array(self.operatingweight)
            self.operatingweight_trackdozer = self.operating_weights_track * 0.4536
            return (self.operatingweight_trackdozer)

        @property
        def bucket_capacity(self):
            self.bladecap = [[x[4] for x in self.result] for self.result in self.all_excavators]
            self.bladecaps = [item for sublist in self.bladecap for item in sublist]
            self.bladecapaci = np.array(self.bladecaps)
            return (self.bladecapaci)

        @property
        def fill_factor_loader(self):
            super().fill_factor_wheel_loader()
            self.fills_factor =[item for sublist in self.result_fills for item in sublist]
            self.fill_factor = np.array(self.fills_factor)
            return (self.fill_factor)


        @property
        def Percent_optimum_height(self):
            self.diggung_cutting = []
            self.angle = []
            self.cutting_load = [[x[6] for x in self.result] for self.result in self.all_excavators]
            self.cutting_loads = [item for sublist in self.cutting_load for item in sublist]
            self.cutting_loadss = np.array(self.cutting_loads) * 0.5
            self.noo = float(input("please insert average height of excavation(mm):\n"))
            self.n_angle = self.angle.append(float(input("please insert angle of swing(degrees):\n")))
            self.diggingcuttingg = (np.round((self.noo /self.cutting_loadss)*100))
            self.diggingcuttings = sorted(self.diggingcuttingg)
            self.x_degree = np.array([45, 60, 75, 90, 120, 150, 180])
            self.y_optheight = np.array([40, 60, 80, 100, 120, 140, 160])
            self.datas = np.array([[0.93, 1.1, 1.22, 1.26, 1.2, 1.12, 1.03],
                                  [0.89, 1.03, 1.12, 1.16, 1.11, 1.04, 0.96],
                                  [0.85, 0.96, 1.04, 1.07, 1.03, 0.97, 0.9],
                                  [0.8, 0.91, 0.98, 1, 0.97, 0.91, 0.85],
                                  [0.72, 0.81, 0.86, 0.88, 0.86, 0.81, 0.75],
                                  [0.65, 0.73, 0.77, 0.79, 0.77, 0.73, 0.67],
                                  [0.59, 0.66, 0.69, 0.71, 0.7, 0.66, 0.62]])

            self.Table_to_Interpolate = pd.DataFrame(self.datas, index=self.x_degree, columns=self.y_optheight)
            self.sp = scipy.interpolate.RectBivariateSpline(self.x_degree, self.y_optheight, self.datas, kx=1, ky=1, s=0)
            scipy.interpolate.RectBivariateSpline(self.x_degree, self.y_optheight, self.datas, kx=1, ky=1, s=0)
            self.Results = pd.DataFrame(self.sp(self.diggingcuttings, self.angle), index=self.diggingcuttings, columns= self.angle,)
            self.Resultss = self.Results.values.tolist()
            self.results = np.round((self.Resultss),2)
            self.result = [item for sublist in self.results for item in sublist]
            self.dict1 = dict(zip(self.diggingcuttings, self.result))
            self.Results =[]
            for i in self.diggingcuttingg:
                for key, value in self.dict1.items():
                    if i == key:
                        self.Results.append(value)
            self.Result = np.array(self.Results)
            return (self.Result)

        @property
        def time_productivity(self):
            self.time_calc = []
            self.soil_in_bucket_type = input("please insert type of material in the bucket:\n(a) Sand,Gravel,Soft Soil\n(b) Common Earth,Soft Clay,Average Soil\n(c) Hard Clay,Stiff Soil\n\n")
            for i in self.bucket_capacity:
                if i < 0.76:
                    if self.soil_in_bucket_type == 'a':
                        self.time_calciulation = 0.25
            for i in self.bucket_capacity:
                if 0.76 <= i <= 1.72:
                    if self.soil_in_bucket_type == 'a':
                        self.time_calciulation = 0.3
            for i in self.bucket_capacity:
                if i > 1.72:
                    if self.soil_in_bucket_type == 'a':
                        self.time_calciulation = 0.4

            for i in self.bucket_capacity:
                if i <= 0.76:
                    if self.soil_in_bucket_type == 'b':
                        self.time_calciulation = 0.3
            for i in self.bucket_capacity:
                if 0.95 <= i <= 1.72:
                    if self.soil_in_bucket_type == 'b':
                        self.time_calciulation = 0.383
            for i in self.bucket_capacity:
                if i > 1.72:
                    if self.soil_in_bucket_type == 'b':
                        self.time_calciulation = 0.5

            for i in self.bucket_capacity:
                if i <= 0.76:
                    if self.soil_in_bucket_type == 'c':
                        self.time_calciulation = 0.383
            for i in self.bucket_capacity:
                if 0.95 <= i <= 1.72:
                    if self.soil_in_bucket_type == 'c':
                        self.time_calciulation = 0.467
            for i in self.bucket_capacity:
                if i > 1.72:
                    if self.soil_in_bucket_type == 'c':
                        self.time_calciulation = 0.6
            self.time_pd = [[x[7] for x in self.result] for self.result in self.all_excavators]
            self.time_prd = [item for sublist in self.time_pd for item in sublist]
            for i in self.time_prd:
                if i != 0:
                    self.time_calc.append(i)
                else:
                    self.time_calc.append(self.time_calciulation)
            return(np.array(self.time_calc))


        @property
        def real_productivity(self, efi = 50):
            self.reals_productivity = (self.bucket_capacity * efi * self.fill_factor_loader * self.Percent_optimum_height) / self.time_productivity
            print(np.round(self.reals_productivity, 2))
            return (np.round(self.reals_productivity, 2))

        @property
        def depreciation_value(self):
            self.delivered_pricexs = []
            self.delivered_pricexs.append([[x[2] for x in self.resultss] for self.resultss in self.costs_input_excavator])
            self.sale_taxs = []
            self.sale_taxs.append([[x[3] for x in self.resultss] for self.resultss in self.costs_input_excavator])
            self.price_sale_tax = (np.array(self.delivered_pricexs)) * ((np.array(self.sale_taxs)) / 100)
            self.price_after_sale_tax = (np.array(self.delivered_pricexs)) + (self.price_sale_tax)
            self.net_value_depreciation = self.price_after_sale_tax - self.price_sale_tax
            return (self.net_value_depreciation)

        @property
        def depreciation(self, expected_use = 20000):
            self.depreciations = self.depreciation_value / expected_use
            return (self.depreciations)

        @property
        def useful_life(self, expected_use = 20000, expected_use_annually = 1590):
            self.usefull_lifes = expected_use / expected_use_annually
            return (np.round(self.usefull_lifes))

        @property
        def interest_cost(self, expected_use_annually = 1590):
            self.interest_costx = []
            self.interest_costx.append([[x[4] for x in self.resultss] for self.resultss in self.costs_input_excavator])
            self.int_cost = self.useful_life + 1
            self.intt_cost = 2 * self.useful_life
            self.inttt_cost = self.int_cost / self.intt_cost
            self.dep_int_cost = self.depreciation_value * (np.array(self.interest_costx) / 100)
            self.dep_int_cosSt = self.dep_int_cost * self.inttt_cost
            self.interest_cosSts = self.dep_int_cosSt /  expected_use_annually
            return (np.round(self.interest_cosSts, 2))

        @property
        def insurance_cost(self, expected_use_annually =1590):
            self.insurance_costx = []
            self.insurance_costx.append([[x[5] for x in self.resultss] for self.resultss in self.costs_input_excavator])
            self.ins_cost = self.useful_life + 1
            self.inss_cost = 2 * self.useful_life
            self.insss_cost = self.ins_cost / self.inss_cost
            self.dep_ins_cost = self.depreciation_value * ((np.array(self.insurance_costx)) / 100)
            self.dep_ins_cosSt = self.dep_ins_cost * self.insss_cost
            self.insurance_costs = self.dep_ins_cosSt / expected_use_annually
            return (np.round(self.insurance_costs, 2))

        @property
        def taxes_cost(self, expected_use_annually =1590):
            self.tx_costx = []
            self.tx_costx.append([[x[6] for x in self.resultss] for self.resultss in self.costs_input_excavator])
            self.tx_cost = self.useful_life + 1
            self.txx_cost = 2 * self.useful_life
            self.txxx_cost = self.tx_cost / self.txx_cost
            self.dep_txt_cost = self.depreciation_value * ((np.array(self.tx_costx)) / 100)
            self.dep_txt_cosSt = self.dep_txt_cost * self.txxx_cost
            self.taxes_costs = self.dep_txt_cosSt / expected_use_annually
            return (np.round(self.taxes_costs, 2))

        @property
        def total_hourly_ownership_cost(self):
            self.total_hourly_ownership_costt = self.depreciation + self.interest_cost + self.insurance_cost + self.taxes_cost
            self.total_hourly_ownership_costts = [item for sublist in self.total_hourly_ownership_costt for item in
                                                  sublist]
            self.total_hourly_ownership_costs = [item for sublist in self.total_hourly_ownership_costts for item in
                                                 sublist]
            return (np.round(self.total_hourly_ownership_costs))

        @property
        def year_of_operationn(self):
            self.year_of_operation = []
            self.year_of_operation.append(
                [[int(x[7]) for x in self.resultss] for self.resultss in self.costs_input_excavator])
            return (self.year_of_operation)

        @property
        def yeardigitt(self):
            self.yeardigiit = []
            self.nn = [[int(x[7]) for x in self.resultss] for self.resultss in self.costs_input_excavator]
            for [n] in self.nn:
                self.yeardigiit.append(sum(range(n + 1)))
            self.yeardigit = [[x] for x in self.yeardigiit]
            return (self.yeardigit)

        @property
        def hourly_repair_cost(self, Lifetime_repair_cost_factor=0.6, expected_use_annually = 1590):
            self.Lifetime_repair_cost = Lifetime_repair_cost_factor * self.depreciation_value
            self.year_digits = (np.array(self.year_of_operationn)) / self.yeardigitt
            self.life = self.Lifetime_repair_cost / expected_use_annually
            self.Hourl_yrepair_cost = self.year_digits * self.life
            self.Hourl_yrepair_cost1 = [item for sublist in self.Hourl_yrepair_cost for item in sublist]
            self.Hourl_yrepair_cost2 = [item for sublist in self.Hourl_yrepair_cost1 for item in sublist]
            return (np.round(self.Hourl_yrepair_cost2, 2))

        @property
        def manual_fuel_consumption_factor(self):
            self.work_condidion = []
            self.work_condidion.append(input("Please insert work condition:\n(a) 'Favorable'\n(b) 'Average'\n(c) 'Unfavorable'\n\n "))
            self.max_fuel_consumption_factor = []
            for self.work_condidions in self.work_condidion:
                if self.work_condidions == 'a':
                    self.max_fuel_consumption_factor.append(0.34)

                elif self.work_condidions == 'b':
                    self.max_fuel_consumption_factor.append(0.42)

                else:
                    self.max_fuel_consumption_factor.append(0.51)
            return (np.array(self.max_fuel_consumption_factor))

        @property
        def manual_load_factor(self):
            self.load_factor = []
            self.load_factor.append(input("Please insert excavator application:\n(a) 'low'\n(b) 'medium'\n(c) 'high'\n\n "))
            self.max_load_factor = []
            for self.load_factors in self.load_factor:
                if self.load_factors == 'a':
                    self.max_load_factor.append(0.4)

                elif self.load_factors == 'b':
                    self.max_load_factor.append(0.6)

                else:
                    self.max_load_factor.append(0.8)
            return (np.array(self.max_load_factor))

        @property
        def manual_fuel_consumption_cost(self):
            self.fuel_cost = []
            for self.cost_input_track in self.cost_input_excavatorS:
                self.fuel_cost.append(self.cost_input_track[0])
            self.manual_fuel_consumption_costs = self.manual_fuel_consumption_factor * self.manual_load_factor * self.fuel_cost * self.real_horsepowerr
            return (self.manual_fuel_consumption_costs)

        @property
        def Lubricating_oil_cost(self):
            self.engin_crankcase = []
            self.engin_crankcase.append([[x[8] for x in self.resultss] for self.resultss in self.costs_input_excavator])
            self.engin_crankcases1 = [item for sublist in self.engin_crankcase for item in sublist]
            self.engin_crankcases2 = [item for sublist in self.engin_crankcases1 for item in sublist]
            self.hours_between_change = []
            self.hours_between_change.append( [[x[9] for x in self.resultss] for self.resultss in self.costs_input_excavator])
            self.hours_between_change1 = [item for sublist in self.hours_between_change for item in sublist]
            self.hours_between_change2 = [item for sublist in self.hours_between_change1 for item in sublist]
            self.lubricant_cost = []
            for self.cost_input_wheel in self.cost_input_excavatorS:
                self.lubricant_cost.append(self.cost_input_wheel[1])
            self.quantity_of_oil_required = self.real_horsepowerr * np.array(self.max_load_factor)
            self.quantity_of_oil_requiredd = 0.006 * self.quantity_of_oil_required
            self.quantity_of_oil_requireds = self.quantity_of_oil_requiredd / 7.4
            self.que = (np.array(self.engin_crankcases2)) / (np.array(self.hours_between_change2))
            self.Lubricating_Oil_Cost = self.quantity_of_oil_requireds + self.que
            self.Lubricating_Cost = self.Lubricating_Oil_Cost * self.lubricant_cost
            self.lub_cost = np.round(self.Lubricating_Cost, 2)
            return (self.lub_cost)

        @property
        def operating_cost_per_hour(self):
            self.operating_costs_per_hour = self.hourly_repair_cost + self.manual_fuel_consumption_cost + self.Lubricating_oil_cost
            return (np.round(self.operating_costs_per_hour, 2))

        @property
        def operator_wage_per_hour(self):
            self.operator_wage_cost = []
            for self.cost_input_wheel in self.cost_input_excavatorS:
                self.operator_wage_cost.append(self.cost_input_wheel[2])
            return (self.operator_wage_cost)

        @property
        def total_cost_per_hour(self):
            self.total_hourly_cost = self.total_hourly_ownership_cost + self.operating_cost_per_hour + self.operator_wage_per_hour
            print(np.round(self.total_hourly_cost, 2))
            return (np.round(self.total_hourly_cost, 2))

        def realprodactivity_cost(self):
            self.realprodactivity_costs = self.real_productivity / self.total_cost_per_hour
            print(self.realprodactivity_costs)
            return (self.realprodactivity_costs)

        def create_linetext_capacity(self):
            self.dictmodel_bucketcapacity = dict(zip(self.modelcoder, self.bucket_capacity))
            with open('best_ex_capacity.txt', 'w') as file:
                for k in self.dictmodel_bucketcapacity.keys():
                    file.write("{}\t{}\n".format(k, self.dictmodel_bucketcapacity[k]))

        def create_linetext_loadtime(self):
            self.time_production = np.array(self.time_calc)
            self.dictmodel_timeproduction = dict(zip(self.modelcoder, self.time_production))
            with open('best_ex_loadtime.txt', 'w') as file:
                for k in self.dictmodel_timeproduction.keys():
                    file.write("{}\t{}\n".format(k, self.dictmodel_timeproduction[k]))

        def create_linetext_production(self):
            self.dictmodel_productivity = dict(zip(self.modelcoder, self.reals_productivity))
            with open('best_ex_production.txt', 'w') as file:
                for k in self.dictmodel_productivity.keys():
                    file.write("{}\t{}\n".format(k, self.dictmodel_productivity[k]))

        def create_linetext_cost(self):
            self.dictmodel_costs = dict(zip(self.modelcoder, self.total_hourly_cost))
            print(self.dictmodel_costs)
            with open('best_ex_cost.txt', 'w') as file:
                for k in self.dictmodel_costs.keys():
                    file.write("{}\t{}\n".format(k, self.dictmodel_costs[k]))


        def creat_linstext(self):
            super().volume_subactivity()
            self.volumee = self.volume_subactivity()
            print(self.volumee)
            self.volumeestr = '\n'.join([str(elem) for elem in self.volumee])
            print(self.volumeestr)
            self.modelsname = self.modelnamer
            print(self.modelsname)
            self.modelcodess = self.modelcoder
            print(self.modelcodess)
            # listToStrt = '\n'.join([str(elem) for elem in self.modelsname])
            # print(listToStrt)
            self.production = np.round(self.reals_productivity)
            # self.production = int(self.productions)
            print(self.production)
            # listToStrt1 = '\n'.join([str(elem) for elem in self.production])
            # print(listToStrt1)
            self.cost = np.round(self.total_hourly_cost)
            # self.cost = int(self.costs)
            print(self.cost)
            # listToStrt2 = ' '.join([str(elem) for elem in self.cost])
            # print(listToStrt2)
            self.maxptoc = np.round(self.realprodactivity_costs, 2)
            # self.maxptoc = int(self.maxptocs)
            print(self.maxptoc)
            # listToStrt3 = ' '.join([str(elem) for elem in self.maxptoc])
            # print(listToStrt3)

        def solution(self):
            self.dictmodel_maxptoc = dict(zip(self.modelcodess, self.maxptoc))
            for key, value in self.dictmodel_maxptoc.items():
                if value == max(self.maxptoc):
                    self.modelmax = key
                    print(self.modelmax)
            self.dictmodel_pr = dict(zip(self.modelcodess, self.production))
            for key, value in self.dictmodel_pr.items():
                if key == self.modelmax:
                    self.pdmax = value
                    print(self.pdmax)
            self.dictmodel_cost = dict(zip(self.modelcodess, self.cost))
            for key, value in self.dictmodel_cost.items():
                if key == self.modelmax:
                    self.costmax = value
                    print(self.costmax)
            self.dictmodel_maxptoc = dict(zip(self.modelcodess, self.maxptoc))
            for key, value in self.dictmodel_maxptoc.items():
                if value == min(self.maxptoc):
                    self.modelmin = key
                    print(self.modelmin)
            self.dictmodel_pr = dict(zip(self.modelcodess, self.production))
            for key, value in self.dictmodel_pr.items():
                if key == self.modelmin:
                    self.pdmin = value
                    print(self.pdmin)
            self.dictmodel_cost = dict(zip(self.modelcodess, self.cost))
            for key, value in self.dictmodel_cost.items():
                if key == self.modelmin:
                    self.costmin = value
                    print(self.costmin)
            self.indexmodels = [self.modelcodess.index(i) + 1 for i in self.modelcodess]
            self.dictcodemodel_indexmodels = dict(zip(self.modelcodess, self.indexmodels))
            for key, value in self.dictcodemodel_indexmodels.items():
                if key == self.modelmax:
                    self.indexmax = value
                    print(self.indexmax)
            self.dictcodemodel_indexmodels = dict(zip(self.modelcodess, self.indexmodels))
            for key, value in self.dictcodemodel_indexmodels.items():
                if key == self.modelmin:
                    self.indexmin = value
                    print(self.indexmin)
            self.hrmax = np.round(self.volumee / self.pdmax)
            self.listToStrt2 = ' '.join([str(elem) for elem in self.hrmax])
            print(self.listToStrt2)
            self.hrmin = 0

        def creat_text(self):
            nums = str(len(self.modelname))
            print(nums)
            volume = self.volumeestr
            print(volume)
            modelcodemax = self.indexmax
            print(modelcodemax)
            modelcodemin = self.indexmin
            print(modelcodemin)
            nmax = str(self.listToStrt2)
            print(nmax)
            nmin = str(self.hrmin)
            print(nmin)
            pdmax = str(self.pdmax)
            print(pdmax)
            pdmin = str(self.pdmin)
            print(pdmin)
            costmax = str(self.costmax)
            print(costmax)
            costmin = str(self.costmin)
            print(costmin)
            f = ['n:', 'c:']
            g = [nums, volume]
            lines = [f, g]
            lie = ["begin data"]
            w = ["end data"]
            ind = ["index", "nb", "pd", "cost"]
            sol = ["sol:"]
            model = [modelcodemax, modelcodemin]
            numbers = [nmax, nmin]
            prdctons = [pdmax, pdmin]
            costss = [costmax, costmin]
            solu = [model, numbers, prdctons, costss]
            e = self.modelcodess
            b = self.production
            a = self.cost
            c = [e, a, b]

            with open('readnew.txt', 'w') as file:
                for line in zip(*lines):
                    file.write("\n{0} {1}\n".format(*line))
                for x in lie:
                    file.write("\n{0}\n".format(x))
                for x in zip(*c):
                    file.write("{0}\t{1}\t{2}\n".format(*x))
                for x in w:
                    file.write("{0}\n".format(x))
                for x in ind:
                    file.write("\t{0}".format(x))
                for x in sol:
                    file.write("\n{0}\n".format(x))
                for x in zip(*solu):
                    file.write("\t{0}\t{1}\t{2}\t{3}\n".format(*x))

    C = Activity()
    F = Excavators()
    F.Excavators_features()
    F.modelnames
    F.modelcodes
    F.horspower_track
    F.horsepowerr_height_temp
    F.realprodactivity_cost()
    F.create_linetext_capacity()
    F.create_linetext_loadtime()
    F.create_linetext_production()
    F.create_linetext_cost()
    F.creat_linstext()
    F.solution()
    F.creat_text()






    print("Selecting from database succeeded...")
    connection.close()
except:
    connection.rollback()
    print("Selecting from database failed...")
