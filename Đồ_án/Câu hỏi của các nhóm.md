# Câu hỏi của các nhóm
## Nhóm 1
- Hỏi: Bài toán này ứng dụng trong mảng nào?
- Đáp: Như đã trình bày, BnB giải quyết được 1 số các bài toán tối ưu hóa dùng trong thực tế như: bài toán tìm đường đi với tổng chi phí ngắn nhất, bài toán đồ thị con đầy đủ, bài toán phân công công việc; BnB áp dụng được trong ứng dụng game với bài toán 8-puzzle (có thể dùng BFS, DFS), game Pikachu tìm đường đi ngắn nhất (có thể dùng A*, BnB)
  - Link 8-puzzle: https://www.geeksforgeeks.org/8-puzzle-problem-using-branch-and-bound/
  - Link pikachu: https://cachhoc.net/2014/03/25/thuat-toan-game-pokemon-pikachu/?lang=en
## Nhóm 8
- Hỏi: Ngoài ứng dụng làm game, B&B còn ứng dụng nào không?
- Đáp: BnB giải quyết được 1 số các bài toán tối ưu hóa dùng trong thực tế như: bài toán tìm đường đi với tổng chi phí ngắn nhất, bài toán đồ thị con đầy đủ, bài toán phân công công việc; BnB áp dụng được trong ứng dụng game với bài toán 8-puzzle (có thể dùng BFS, DFS), game Pikachu tìm đường đi ngắn nhất (có thể dùng A*, BnB)
## Nhóm 11
- Hỏi: Nhược điểm tại sao nói thuật toán tốt nhưng kết quả tìm được chưa tối ưu nhất có thể. Giải thích từ chưa tối ưu nhất.
- Đáp: Yêu cầu tính toán phân nhánh nhiều hơn và do đó tính toán kém hiệu quả hơn.
## Nhóm 12
- Hỏi: B&B ứng dụng vào làm game thì ứng dụng như thế nào?
- Đáp: Security Games with Arbitrary Schedules: A Branch and Price Approach (Trò chơi bảo mật với lịch trình tùy ý: PP tiếp cận theo nhánh và giá)
  - Trò chơi bảo mật, là một trò chơi hai người chơi giữa một người phòng thủ và một người tấn công. Chúng tôi áp dụng mô hình trò chơi tấn công-phòng thủ Stacklelberg (attacker-defender Stackelberg games), trong đó người phòng thủ sẽ hành động đầu tiên và người tấn công chọn một chiến lược sau khi quan sát chiến lược của người phòng thủ. Trò chơi Stackelberg phổ biến trong việc lập lập lịch trình ngẫu nhiên cho các hệ thống an ninh tại sân bay, tàu điện ngầm, bến cảng và cơ sở hạ tầng quan trọng khác, ví dụ như để lập lịch trình tuần tra chó và kiểm tra phương tiện hoặc tạo lịch bay cho các cảnh sát trưởng hàng không.
  - Các thuật toán được sử dụng để giải quyết các trò chơi này là tìm lịch trình ngẫu nhiên tối ưu để phân bổ tài nguyên bảo mật cho việc bảo vệ cơ sở hạ tầng. Chúng tôi giới thiệu ASPEN, một phương pháp sử dụng tạo cột (column generation) để tránh đại diện cho không gian chiến lược đầy đủ cho người phòng thủ và sử dụng phương pháp nhánh-cận (branch-n-bound) để tìm kiếm không gian của các chiến lược của người tấn công. ASPEN được đánh giá là pp đầu tiên được biết đến để giải quyết hiệu quả trò chơi bảo mật với lịch trình tùy ý.
  - ASPEN sử dụng nhánh-cận để tìm kiếm trong không gian của các chiến lược có thể có của người tấn công. Ta sử dụng giải pháp ORIGAMI tích hợp vào ASPEN để đưa ra các cận và chọn ra các nhánh. ASPEN giảm thiểu phần thưởng tối đa của người tấn công. Giá trị lớn nhất là cận trên ban đầu của phần thưởng cho người phòng thủ. Nút lá đầu tiên mà ASPEN đánh giá tương ứng với mục tiêu có giá trị tối đa này (tức là cài đặt giá trị tấn công của nó là 1). Giải pháp này là cận dưới của giải pháp tối ưu và thuật toán dừng nếu cận dưới đáp ứng cận trên của ORIGAMI. Nếu không, một cận trên mới từ giải pháp ORIGAMI thu được bằng cách chọn người phòng thủ cao thứ hai từ các mục tiêu trong cuộc tấn công và ASPEN đánh giá nút lá tương ứng. Quá trình tiếp tục cho đến khi đáp ứng cận trên hoặc các nút có sẵn trong cây tìm kiếm đã hết.
    - Link paper: https://www.researchgate.net/publication/221604935_Security_Games_with_Arbitrary_Schedules_A_Branch-and-Price_Approach
## Nhóm 14
- Hỏi: Kể ra những cách để tăng tốc nhánh cận?
- Đáp: 
  - Phân nhánh trên nút có giới hạn nhỏ nhất
    - Tìm kiếm tất cả các nút và tìm nút có giới hạn nhỏ nhất và đặt nó làm nút phân nhánh tiếp theo. Ưu điểm: Nói chung, nó sẽ kiểm tra ít vấn đề con hơn và do đó tiết kiệm thời gian tính toán. Bất lợi: Thông thường nó sẽ yêu cầu nhiều dung lượng hơn.
  - Phân nhánh trên nút mới tạo với giới hạn nhỏ nhất
    - Tìm kiếm các nút mới được tạo và tìm nút có giới hạn nhỏ nhất và đặt nó làm nút phân nhánh tiếp theo. Ưu điểm: Tiết kiệm không gian lưu trữ. Nhược điểm: Yêu cầu tính toán phân nhánh nhiều hơn và do đó tính toán kém hiệu quả hơn
